# Pip Install speechrecognition
# Pip install Pyaudio
# Pip Install pyttsx3
# Pip install setuptools
import speech_recognition as sr
import pyttsx3


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_data = ""
            voice_data = r.recognize_google(audio)
            print(voice_data)
            return voice_data
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError:
            print("RequestError")
        
