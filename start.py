import vosk
import sys
import json
import pyaudio
import requests
import pyttsx3  # Import the pyttsx3 library

# Path to the Vosk model directory
vosk_model_path = "C:\\Users\\yuvra\\Downloads\\vosk-model-small-en-us-0.15\\vosk-model-small-en-us-0.15"

# Initialize Vosk model
model_vosk = vosk.Model(vosk_model_path)

# Initialize PyAudio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Initialize pyttsx3 engine
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 200)  # Set speaking rate
tts_engine.setProperty('volume', 1.0) 
voices = tts_engine.getProperty('voices')

# Print available voices for reference (optional)
for idx, voice in enumerate(voices):
    print(f"Voice {idx}: {voice.name} ({voice.id})")

# Change to a specific voice (e.g., female or male)
tts_engine.setProperty('voice', voices[1].id) # Set volume level (1.0 is max)

def recognize_speech():
    rec = vosk.KaldiRecognizer(model_vosk, 16000)
    print("Listening...")
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            if 'text' in result and result['text']:
                return result['text']
    return None

def generate_response(prompt, ollama_host="http://localhost:11434"):
    url = f"{ollama_host}/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama3.2",
        "prompt": prompt,
    }
    try:
        response = requests.post(url, headers=headers, json=data, stream=True)
        print("Raw Response Stream:")  # Debugging line

        final_response = ""
        for line in response.iter_lines(decode_unicode=True):
            if line.strip():  # Skip empty lines
                try:
                    json_obj = json.loads(line)
                    print(json_obj)  # Debugging line
                    final_response += json_obj.get("response", "")
                    if json_obj.get("done", False):  # Stop if "done" is True
                        break
                except json.JSONDecodeError as e:
                    print(f"JSON Decode Error: {e} - Line: {line}")
        
        return final_response.strip()

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return ""

def speak(text):
    if not text:
        print("No text to speak.")
        return
    tts_engine.say(text)
    tts_engine.runAndWait()  # Speak the text

# Main loop
print("Say 'Jarvis' to wake me up.")
while True:
    wake_up_command = recognize_speech()
    if wake_up_command and "jarvis" in wake_up_command.lower():
        print("I'm listening...")
        speak("Yes, how can I assist you?")
        
        # Listen for the next input
        user_input = recognize_speech()
        if user_input:
            print(f"You said: {user_input}")
            response = generate_response(user_input)
            if response:
                print(f"Response from Ollama: {response}")
                speak(response)
            else:
                print("No valid response from Ollama.")
        else:
            print("No speech detected.")
