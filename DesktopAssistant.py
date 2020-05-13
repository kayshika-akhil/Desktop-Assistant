from tkinter import *
from time import gmtime, strftime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os
import urllib.request
import urllib.parse



engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = Tk()
window.configure(bg="black")
window.geometry("400x640")
window.maxsize(400, 640)
window.iconbitmap("C:\\Users\\Hp\\PycharmProjects\\justchilliing\\robot-2192617_1280.ico")

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        var.set("Good Morning sir")
        window.update()
        speak("Good Morning sir!")
    elif 12 <= hour <= 18:
        var.set("Good Afternoon sir")
        window.update()
        speak("Good Afternoon sir")
    else:
        var.set("Good Evening sir")
        window.update()
        speak("Good Evening sir")
    speak("Myself Alice! How may I help you sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        var.set("Sir can you say that again")
        window.update()
        speak("sir can you say that again")
        return "None"
    var1.set(query)
    window.update()
    return query


def play():
    btn1.configure(bg='black')
    wishme()
    while True:
        btn1.configure(bg='grey')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")
            break
        elif 'open course error' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.open("coursera.com")
            break

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")
            break
        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")
            break
        elif 'who are you' in query:
            speak("hello sir,I am alice the creation of akhil sir and  personal assistant")
            break
        elif 'what is the time' in query:
            stime = strftime("%a,%d%b%Y", gmtime())
            speak(stime)
            break
        elif 'create a folder' in query:
            var.set('creating folder')
            window.update()
            speak('creating folder')
            os.chdir("D:")
            speak("sir can you tell me the folder name")
            folder = takeCommand()
            os.mkdir(folder)
            break
        elif 'who made you' in query:
            speak("I have been created by KAPA")
            break
        elif 'search video' in query:
            speak('what type of video would you like to search')
            sv = takeCommand()
            query_string = urllib.parse.urlencode({"search_query": input(sv)})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])
            break





def update(ind):
    frame = frames[ind % 1]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)


label2 = Label(window, textvariable=var1, bg='black')
label2.config(font=("Courier", 20), fg='white')
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable=var, bg='black')
label1.config(font=("Courier", 20), fg='white')
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='C:\\Users\\Hp\\Pictures\\imagses.gif')]
window.title('ALICE')

label = Label(window, width=500, height=500)
label.pack()
window.after(0, update, 0)

btn1 = Button(text='SPEAK', width=20, command=play, bg='black', fg='white')
btn1.config(font=("Courier", 12))
btn1.pack()

btn2 = Button(text='EXIT', width=20, command=window.destroy, bg='black', fg="white")
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()
