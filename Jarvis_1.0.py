#Author : Kaamil Savla
#creation date : 
#code : Virtual Assistant [JARVIS]

from distutils import command
from unittest import main
import speech_recognition as sr
from gtts import gTTS
import webbrowser 
import datetime

def great():
    print("-------------------------------------")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")   

    else:
        print("Good Evening!")  

    print("Hello I am Jarvis.\nHow may I help you sir?")

def takeCommand():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("------------------------------------")
        print("I am listening......")
        voice = listener.listen(source)

    try:
        print("Recognising......")
        command = listener.recognize_google(voice)
        print("I listened -", command)
        
    except Exception as e:
        print("Can't recognise.......Please repeat")
        return "None"

    return command

if __name__ == "__main__":
    great()
    while True:
        query = takeCommand().lower()
        if ('hai' in query) or ('hello' in query) or ('hi' in query):
            print("hello Sir")
        elif ('who' in query) and ('you' in query):
             print("I am JARVIS, a AI based program")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")      
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'map' in query:
            webbrowser.open("maps.google.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print("Sir, the time is {strTime}")
        elif ('music' in query) or ('song' in query):
            webbrowser.open("https://music.youtube.com/watch?v=VNs_cCtdbPc&list=RDAMVMVNs_cCtdbPc")
        elif 'exit' in query:
            print("Have a nice day sir.")
            break
        else:
            print("Sorry. I can't do that")

