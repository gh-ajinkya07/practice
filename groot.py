

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()
engine.setProperty('rate',170)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    time = datetime.datetime.now().strftime('%I:%M:%S')
    speak("The current time is:")
    speak(time)

def date():
    month = datetime.datetime.now().strftime('%B')
    day = datetime.datetime.now().day
    speak('Today\'s date is')
    speak(day)
    speak(month)

def greet():
    speak("Welcome back SIR!")
   
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 16:
        speak('Good Afternoon!')
    elif hour >= 16 and hour <= 20:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("EDITH at your service.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print('Recognizing....')
        querry = r.recognize_google(audio,language ='en-US')
        print(querry)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return querry

if __name__ == '__main__':

    greet()

    while True:
        querry = takeCommand().lower()

        if 'time' in querry:
            time()
        elif 'date' in querry:
            date()
        elif 'offline' in querry:
            quit()

        elif 'wikipedia' in querry:
            speak("Searching....")
            querry = querry.replace("wikipedia", "")
            result = wikipedia.summary(querry, sentences = 2)
            speak(result)