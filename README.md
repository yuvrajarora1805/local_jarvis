🤖 Jarvis - Your Personal Voice Assistant 🤖
Welcome to Jarvis, a voice-activated assistant that listens to your commands, generates intelligent responses using AI, and speaks back to you. Built using the Vosk speech recognition model, Ollama for AI-powered responses, and pyttsx3 for text-to-speech functionality, Jarvis is here to help you with anything you need—just say "Jarvis" to wake him up!

🚀 Features 🚀
🗣 Speech Recognition: Powered by Vosk, it listens to your voice commands and understands your speech.
🤖 AI Responses: Uses Ollama API to generate intelligent and creative responses to your questions.
🔊 Text-to-Speech: Converts AI-generated responses into speech using pyttsx3, making the assistant interactive.
🕹 Wake-Up Command: Say "Jarvis" to activate the assistant and start a conversation.
💬 Real-Time Interaction: Talks back and responds to your questions or commands with a human-like voice.
🛠 Installation 🛠
Prerequisites
Before running Jarvis, ensure that you have the following installed:

Python 3.6+: Make sure you have Python 3.6 or higher installed.
Vosk Model: Download the Vosk small English model (e.g., vosk-model-small-en-us-0.15).
Ollama API: Set up and run the Ollama API locally. Download from Ollama.
Required Python Libraries: Install the necessary libraries by running:
bash
Copy code
pip install vosk pyaudio requests pyttsx3
Setup Instructions
Download Vosk Model:
Go to Vosk Models and download the vosk-model-small-en-us-0.15 model.
Extract the model and note the path where it's saved.
Update the vosk_model_path variable in the script with the path to your downloaded model.
python
Copy code
vosk_model_path = "C:\\path\\to\\vosk-model-small-en-us-0.15"
Set Up Ollama API:

Download and set up Ollama on your local machine.
Make sure the Ollama API is running at http://localhost:11434.
Update Script for Voice:

pyttsx3 lets you choose a voice. To change the voice, simply update this line in the script:
python
Copy code
tts_engine.setProperty('voice', voices[1].id)  # Select the desired voice index
🚀 How to Run 🚀
Ensure your environment is set up with the necessary Python libraries and dependencies.
Run the script:
bash
Copy code
python voice_assistant.py
Wake up Jarvis:
Say "Jarvis" to wake up the assistant. Then, ask questions like:

"What's the weather like today?"
"Tell me a joke."
"What is the capital of France?"
Jarvis will respond with an AI-generated answer, speaking it aloud through the speakers.

💡 How It Works 💡
Speech Recognition:
The assistant listens to your voice through the microphone using Vosk. It waits for the keyword "Jarvis" to activate.
AI Response Generation:
Once activated, the assistant listens for your input and sends it to the Ollama API. Ollama processes the input and generates a response.
Text-to-Speech:
pyttsx3 converts the response into speech and plays it aloud, so you can hear the answer.
📝 Example Commands 📝
Say: "Jarvis, what's the time?"

Jarvis responds: "The time is 3:45 PM."

Say: "Jarvis, tell me a joke!"

Jarvis responds: "Why don't skeletons fight each other? They don't have the guts!"

Say: "Jarvis, what's the capital of Japan?"

Jarvis responds: "The capital of Japan is Tokyo."

🚨 Troubleshooting 🚨
Error: Ollama server not running
Make sure the Ollama API is running locally on port 11434.

Error: Vosk model not found
Verify that the Vosk model path is correctly set and that the model is downloaded and extracted properly.

Microphone Issues
Ensure that your microphone is working and recognized by your system.

📜 License 📜
This project is licensed under the MIT License. See the LICENSE file for details.

🌟 Contributing 🌟
Feel free to fork the repository, submit issues, and create pull requests. We welcome contributions to improve Jarvis!

🚀 Enjoy your voice assistant, and may Jarvis always be ready to assist you! 🤖
