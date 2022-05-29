

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os

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
    speak("Welcome back jinx!")
   
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 16:
        speak('Good Afternoon!')
    elif hour >= 16 and hour <= 20:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak(" I am GROOT!!. How can i help you?")

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

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aj.patil9292@gmail.com','AJINKYA12345')
    server.sendmail('aj.patil9292@gmail.com',to,content)
    server.close()


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
            result = wikipedia.summary(querry, sentences = 3)
            speak(result)
            
        elif "send mail" in querry:
            try:
                speak("What is the E-mail id?")
                to = takeCommand()
                speak("What should i send?")
                content = takeCommand()
                sendmail(to, content)
                speak("Mail sent Succesfully!")

            except Exception as e:
                speak(e)
                speak("Unable to send E Mail!!")

        elif "search for me" in querry:
            speak("What should i search!")
            search = takeCommand().lower()
            url = 'https://'
            wb.register('chrome',
                None,
                wb.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            wb.get('chrome').open_new_tab(url+search+".com")

        elif "logout" in querry:
            os.system("shutdown - l")

        elif "shutdown" in querry:
            os.system("shutdown /s /t 1")
        
        elif "restart" in querry:
            os.system('shutdown /r /t 1')