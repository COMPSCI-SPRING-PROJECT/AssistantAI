import subprocess
import webbrowser
import speech_recognition as sr
import pyttsx3
import Weather
import gtts
import os
import Calculator
from playsound import playsound
from logging import exception
from dotenv import load_dotenv
from datetime import datetime
import time

load_dotenv()

api_key = os.getenv('api_key')

NAME = "Avery"

def main():
    time.sleep(1)
    while 1:
        respond(voiceSpeech())


def speakText(command):
    try:
        tts = gtts.gTTS(command)
        audio_file = "test.mp3"
        tts.save(audio_file)
        playsound(audio_file)
        os.remove(audio_file)
    except Exception:
        print("Error with Google-Text-To-Speech")
        print("Switching to offline Text-To-Speech")
        engine = pyttsx3.init()
        voices = engine.getProperty("voices")
        engine.setProperty('voice', voices[1].id)
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
                printSpeak(ask)
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
    calc = Calculator()
    if "what is your name" == data:
        printSpeak("My name is " + NAME)
    elif "what" in data and "time" in data:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        printSpeak("Current Time =", current_time)
    elif "find location" in data:
        location = voiceSpeech("What is the location?")
        url = "http://www.google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        printSpeak("Result for location " + location)
    elif "search" in data:
        search = voiceSpeech("What do you want to search for?")
        print(search)
        url = "http://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        printSpeak("Result for " + search)
        
    elif "weather" in data:
        # Key in config.py, which is hidden due to .gitignore
        weather = Weather.Weather(api_key)
        city = voiceSpeech("What city's weather do you want to search?")
        print(city)
        dict_weather = weather.getWeather(city)
        if dict_weather['success']:
            del dict_weather['success']
            printSpeak(str(dict_weather))
        else:
            printSpeak("Could not find weather for " + city)
    elif "stop" in data or "exit" in data:
        exit()
    elif checkCalc(data, calc):
        printSpeak(calc.fromString(data))
    elif "open" in data:
        data_temp = data.split(" ")[1]
        os.system(data_temp)
        printSpeak("Opened " + data_temp)
    elif "open" in data and "file" in data:
        query_string = data.split(" ")[2]
        local_path = r'C:\Users'
        subprocess.Popen(
            f'explorer /root,"search-ms:query={query_string}&crumb=folder:{local_path}&"')
    else:
        printSpeak("Did you say" + data + "?")


def checkCalc(data, calc):
    for word in data:
        if word in calc.all:
            return True
    return False


def printSpeak(text):
    print(text)
    speakText(text)

main()
