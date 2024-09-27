import pyttsx3
import speech_recognition as sr

# Initialize the speech engine
engine = pyttsx3.init()

# Function to make the voice assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the user's voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for symptoms...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"User said: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."

# Voice assistant intro when the website is launched
def voice_assistant_intro():
    speak("Welcome to the comprehensive healthcare diagnosis system. You can describe your symptoms and I will assist you with a diagnosis.")

# Save this file as 'voice_assistant.py'
