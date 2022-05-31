import random
import webbrowser
import speech_recognition as sr
import pyttsx3
import requests
import gtts
import os
from playsound import playsound
from logging import exception
from dotenv import load_dotenv
from datetime import datetime
import time

api_key = os.environ['API_KEY']

NAME = "Avery"


def main():
    time.sleep(1)
    print(api_key)
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
    elif "what" in data and "time" in data:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        speakText("Current time is " + current_time)
    elif "find location" in data:
        location = voiceSpeech("What is the location?")
        url = "http://www.google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        print("Result for location " + location)
        speakText("Result for location " + location)
    elif "search" in data:
        search = voiceSpeech("What do you want to search for?")
        print(search)
        url = "http://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        print("Result for " + search)
        speakText("Result for " + search)
    elif "weather" in data:
        # Key in config.py, which is hidden due to .gitignore
        weather = Weather(api_key)
        city = voiceSpeech("What city's weather do you want to search?")
        print(city)
        dict_weather = weather.getWeather(city)
        if dict_weather['success']:
            del dict_weather['success']
            print(dict_weather)
            speakText(str(dict_weather))
        else:
            print("Could not find weather for " + city)
            speakText("Could not find weather for " + city)
    elif "stop" in data or "exit" in data:
        exit()
    else:
        print("Did you say" + data + "?")
        speakText("Did you say" + data + "?")


class Weather:

    KEY = ""

    def __init__(self, key):
        self.KEY = key

    def __callAPI(self, link):
        req = requests.get(link)
        data = req.json()
        return data

    def __convertKtoC(self, temp):
        return round(temp-273.15, 1)

    """
    getWeather takes a location and returns a dictionary
    the dictionary contains whether the API call was successful, if it is successful then it also 
    contains weather description, current temperature, current feels like temperature, and humidity. 
    """

    def getWeather(self, location: str):
        try:
            geo_data = self.__callAPI(
                "http://api.openweathermap.org/geo/1.0/direct?q="+location+"&limit=2&appid="+self.KEY)
            lat = str(geo_data[0]['lat'])
            lon = str(geo_data[0]['lon'])
            api_data = self.__callAPI(
                "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+self.KEY)
            weather = api_data['weather'][0]['description']
            temperature = str(self.__convertKtoC(
                api_data['main']['temp']))+"°C"
            feels_like = str(self.__convertKtoC(
                api_data['main']['feels_like']))+"°C"
            humidity = str(api_data['main']['humidity'])+"%"
            return {'success': True, 'weather': weather, 'temperature': temperature, 'feels like': feels_like, 'humidity': humidity}
        except exception:
            return {'success': False}


main()
