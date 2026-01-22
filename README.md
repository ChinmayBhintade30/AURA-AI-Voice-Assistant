# AURA – AI Voice Assistant 🎙️🤖

AURA is a Python-based AI Voice Assistant designed to perform everyday tasks using voice commands.  
It uses Speech Recognition to understand user input and Text-to-Speech to respond back, enabling natural two-way interaction.

---

## 🔹 Features
- Wake word detection ("Jarvis")
- Voice-controlled web browsing
- Play songs using voice commands
- Fetch real-time news headlines
- Two-way voice interaction
- Modular and extensible design

---

## 🔹 Technologies Used
- Python 3
- Speech Recognition (Google STT)
- Text-to-Speech (TTS)
- REST APIs
- HTTP Requests
- Git & GitHub

---

## 🔹 Libraries Used
- `speech_recognition` – Speech to Text
- `pyttsx3` – Text to Speech
- `webbrowser` – Open websites
- `requests` – API calls (NewsAPI)
- `musicLibrary` – Custom module for music mapping

---

## 🔹 Project Structure
AURA/
│── main.py # Core voice assistant logic
│── musicLibrary.py # Song name to URL mapping
│── .gitignore # Ignored files
│── README.md # Project documentation




---

## 🔹 How It Works (Data Flow)

1. User speaks wake word **"Jarvis"**
2. Microphone captures audio
3. Speech Recognition converts audio → text
4. Command is processed using condition logic
5. Task is executed (open site / play song / fetch news)
6. AURA responds using Text-to-Speech

---

## 🔹 Example Commands
Jarvis
open google
play skyfall
news


---

## 🔹 News API Integration
- Uses NewsAPI to fetch live headlines
- Requires an API key from https://newsapi.org
- Headlines are spoken using TTS

---

## 🔹 Installation & Execution

```bash
python -m venv venv
venv\Scripts\activate
pip install SpeechRecognition pyttsx3 pyaudio requests
python main.py



🔹 Key Concepts Implemented

Speech Recognition

Text-to-Speech

API Integration

Dictionaries & String Processing

Exception Handling

Modular Programming

Virtual Environments (venv)

🔹 Future Enhancements

NLP-based command understanding

Offline speech recognition

GUI interface

ChatGPT integration

System-level automation

🔹 Author

Chinmay
Electronics & Telecommunication Engineer
