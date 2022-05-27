from tkinter import *
import webbrowser
import speech_recognition as sr
import pyttsx3
import pyaudio
import requests
from datetime import datetime
import time

NAME = "Avery"

def main():
    time.sleep(1)
    while 1:
        respond(voiceSpeech())

def speakText(command):
    engine = pyttsx3.init()
    newVoiceRate = 145
    engine.setProperty('rate', newVoiceRate)
    engine.say(command)
    engine.runAndWait()

def voiceSpeech(ask=False):
    r = sr.Recognizer()
    mic = sr.Microphone()
    try:
        with mic as source:
            if ask:
                print(ask)
                speakText(ask)
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening: ")
            audio = r.listen(source, timeout=4)
            myText = r.recognize_google(audio).lower()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occured.")
    return myText

def respond(data):
    if "what is your name" == data:
        print("My name is " + NAME)
        speakText("My name is " + NAME)
    if "what" in data and "time" in data:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        speakText("Current time is " + current_time)
    if "find location" in data:
        location = voiceSpeech("What is the location?")
        url = "http://www.google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        print("Result for location " + location)
        speakText("Result for location " + location)
    if "search" in data:
        search = voiceSpeech("What do you want to search for?")
        print(search)
        url = "http://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        print("Result for " + search)
        speakText("Result for " + search)
    if "stop" in data or "exit" in data:
        exit()

def weather():
    print("Fill out here")

main()
