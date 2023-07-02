from aip import AipSpeech
import speech_recognition as sr

APP_ID = "35604450"
API_KET = "PqpBNvXfHZH2PZARr5P7zdrK"
SECRET_KEY = "tARVBQcHviHwZe3C1OyU5K5dZZ3wBIaY"

client = AipSpeech(APP_ID, API_KET, SECRET_KEY)
r = sr.Recognizer()

