import datetime as dt
import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import urllib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(dt.datetime.now().hour)
    user.split()
    if hour>=0 and hour<12:
        speak(f"good morning {user[-1]}")
    if hour>=12 and hour<18:
        speak(f"good afternoon{user[-1]}")
    else:
        speak(f"good evening {user[-1]}")
    speak("how may i help you")

def userCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising...!")
        command=r.recognize_google(audio,language='en-Us')
        print(f"you said: { command}")
    except sr.UnknownValueError as e:
        print(e)
        print("sorry I could not get it")
        return "None"
    return command

if __name__ == "__main__":
    speak("Hii what's your name")
    user=userCommand()
    wishme()
    while True:
        command=userCommand().lower()
        if "google" in command:
            webbrowser.open('google.com')
       
        elif "time" in command:
            time=dt.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(time)
        elif "youtube" in command:
            webbrowser.open('youtube.com')
        elif "name" in command:
            print("My name is Chota Aman")
            speak("My Name is Chota Aman")
        elif "open chrome" in command:
            path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        elif "wikipedia" or "search" in command:
            speak("searcing Wikipedia")
            command=command.replace("wikipedia","")
            try:
                result=wikipedia.summary(command,sentences=2)
                print(result)
                speak(result)
            except Exception as e:
                print(e[0:10])
                speak("sorry please say again")

        #elif "search" | "who is" in command:
            #command=command.replace("search","")
            #command=urllib.quote(command)

        elif "wifi on" or "on wifi" in command:
            speak("turing wifi on")
            os.system("netsh interface set interface Wi-Fi enabled")

        elif "wifi off" or "off wifi" in command:
            speak("turing wifi off")
        os.system("netsh interface set interface Wi-Fi disabled")
        
        
        elif "exit"or "quit" in command:
            speak("bye bye see you next time soon")
            exit()
            
        