from tkinter import *
import speech_recognition as sr
import pyttsx3
import pyaudio
import requests
import time

def main():    
    voiceSpeech();
 
def speakText(command):
    engine = pyttsx3.init()
    newVoiceRate = 145
    engine.setProperty('rate',newVoiceRate)
    engine.say(command)
    engine.runAndWait()

def voiceSpeech():
    r = sr.Recognizer()
    mic = sr.Microphone()
    
    while(1):
        try:
            with mic as source:
                r.adjust_for_ambient_noise(source, duration=0.2)
                print("Listening: ")
                audio = r.listen(source,timeout=2)
                
                myText = r.recognize_google(audio)
                myText = myText.lower()
                
                if (myText == "stop"):
                    print("Stop!")
                    break
    
                print("Did you say "+ myText + "?")
                speakText(myText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("Unknown error occured.")

def googleSearch():
    
def weather():
    

main()