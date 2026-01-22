import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import musicLibrary


NEWS_API_KEY = "146740d2742746f19bdcbc73c8f22af6" # replace with your key

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

  

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    command = command.lower()

    if "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")

    elif command.startswith("play"):
        try:
            song = command.replace("play", "").strip().lower()
            link = musicLibrary.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        except KeyError:
            speak("Song not found in library")


    elif "news" in command:
        r = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    )

        if r.status_code == 200:
            articles = r.json().get("articles", [])
            speak("Here are the top headlines")
            for article in articles[:5]:
                speak(article["title"])
        else:
            speak("Unable to fetch news")


if __name__ == "__main__":
    speak("Initializing AURA")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)

            wake_word = recognizer.recognize_google(audio)

            if wake_word.lower() == "aura":
                speak("Yes")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    print("Command:", command)
                    process_command(command)

        except sr.WaitTimeoutError:
            pass
        except Exception as e:
            print("Error:", e)
