from tkinter import *
import speech_recognition as sr
import pyttsx3
import time

def main():
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
                SpeakText(myText)
                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("Unknown error occured.")
 
def SpeakText(command):
    engine = pyttsx3.init()
    newVoiceRate = 145
    engine.setProperty('rate',newVoiceRate)
    engine.say(command)
    engine.runAndWait()

main()