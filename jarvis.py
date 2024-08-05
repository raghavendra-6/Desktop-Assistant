import datetime
import os
import random
import sys
import time
import webbrowser

import pyautogui

import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia
import instaloader
from requests import get
import  pause

va_name = 'friday'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 185)


def folder(f):
    os.startfile(f)
    return f



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def openfolder():
        open("/home/pi/Desktop/Images/")


def open_close(n):
    pyautogui.hotkey('ctrl', 'w')
    print("tab closed")


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=0, phrase_time_limit=8)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-UK')
        print(f"user said : {query}")
        if va_name in query:
            command = takecommand().replace(va_name + '', '')

    except Exception as e:

        return "xxxxx"
        pass
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning boss!")
    elif hour > 12 and hour < 16:
        speak(" good afternoon boss!")
    else:
        speak("good evening boss!")
    speak("I am FRIDAY,your virtual assistant")
    speak("how can i help you?")


if __name__ == "__main__":
    wish()

    while True:
        query = takecommand().lower()

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)
            speak("opening notepad")

        elif "close notepad" in query:
            speak("closing notepad")

            os.system("taskkill /f /im notepad.exe")
        elif "open command prompt" in query:
            os.system("start cmd")
            speak('starting command prompt')

        elif "play music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "stop music" in query or "close music" in query:
            speak("closing")
            path = "D:\\music"
            path = os.path.realpath(path)
            os.close(path)

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f" your ip address is{ip}")

        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
            speak("opening" + "Youtube")

        elif "close youtube" in query:
            speak("closing youtube")
            open_close("https://www.youtube.com/")

        elif "who created you" in query:
            speak("I was created by raahghava")

        elif "what is your name" in query or "what's your name" in query:
            speak("i am friday raahghava's virtual assistant")

        elif "open facebook" in query:
            webbrowser.open("https://www.facebook.com/")
            speak("opening" + "face book")

        elif "volume up" in query or "increase volume" in query:

            speak("boss,do want increase full volume")
            condition = takecommand().lower()
            if "yes" in condition:
                speak("increasing volume")
                pyautogui.press("volumeup",50)
            else:
                speak("increasing volume")
                pyautogui.press("volumeup", 10)


        elif "volume down" in query or "decrease volume" in query:
            speak("decrease volume")
            pyautogui.press("volumedown",10)

        elif "mute" in query or "un mute" in query:
            speak(query + "ing")
            pyautogui.press("volumemute")


        elif "close facebook" in query:
            speak("closing facebook")
            open_close("https://www.facebook.com/")


        elif "imitate meghana" in query:
            speak("my name is miaghana sir")

        elif "can you imitate meghana" in query:
            speak("my name is miaghana sir")

        elif "can you imitate meghna" in query:
            speak("my name is miaghana sir")

        elif "can you imitate Magna" in query:
            speak("my name is miaghana sir")


        elif "can you copy the style of Magna" in query or"can you copy the style of meghana" in query or "can you copy the style of Meghna" in query or "can you copy the style of magna" in query or "can you copy the style of meghana" in query :
            speak("my name is miaghana sir")


        elif "open stack overflow" in query:
            webbrowser.open("https://stackoverflow.com/")
            speak("opening" + "stack over flow")

        elif "close stack over flow" in query:
            speak("closing stack over flow")
            open_close("https://www.stackoverflow.com/")

        elif "close main folder" in query or "close our folder" in query:
            speak("closing")

            path = int("D:\jarvis")
            path = os.path.realpath(path)
            os.close(path)


        elif "open gmail" in query:
            webbrowser.open("www.gmail.com")
            speak("opening" + "Gmail")

        elif "close gmail" in query:
            speak("closing gmail")
            open_close("https://www.gmail.com/")

        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")
            speak("opening" + "instagram")

        elif "close instagram" in query:
            speak("closing instagram")
            open_close("https://www.instagram.com/")
        elif "open browser" in query:

            speak("what should i browse,boss?")
            cm = takecommand().lower()

            os.system(f"{cm}")

        elif "hello" in query:
            speak("hello boss!")
        elif "friday" in query:
            speak("I am here! tell me boss")
        elif "how are you" in query:
            speak("I am fine boss,what about you?")
        elif "i am fine" in query or "i am good" in query or "i am pretty good" in query:
            speak("that's nice to here,boss do you have any work?")
        elif "open google" in query or "search for" in query:
            try:
                query = query.replace('search for', '')
                query = query.replace('open google', '')
                speak("searching for" + query)
                pywhatkit.search(query)
                results = wikipedia.summary(query,2)
                speak(results)
            except:
                speak('sorry something went wrong')
                pass
        elif "close google" in query:
            speak("closing google")
            os.system("taskkill /im chrome.exe /f")

        elif "open main folder" in query or "open our folder" in query:
            speak("yes boss,opening main folder")

            folder("D:\\jarvis")












        elif "open new tab" in query or "new tab" in query:
            speak("boss,what should I search on new tab?")
            speak("opening new tab")
            cm = takecommand().lower()

            webbrowser.open(f"{cm}")

        elif "switch window" in query or "change window" in query or "slide" in query:
            speak("switching window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "pause" in query or "play" in query or "pass" in query:
            speak("yes,boss")
            pyautogui.press("space")

        elif "where am i" in query or "where we are" in query or "find my location" in query:
            speak("wait sir let me check")
            try:
                check = requests.get('https://api.ipify.org').text
                print(check)
                url = 'https://get.geojs.io/v1/ip/geo/' + check + '.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                city = geo_data['city']

                country = geo_data['country']
                speak(f"we are in {city} city of {country}")

            except Exception as e:
                speak("sorry boss, due to network issue I can't find where we are")
                pass

        elif "download profile picture on instagram" in query or "profile on instagram" in query:
            speak("please enter user name,boss ")
            name = input("enter user name:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f" boss,here is the profile of the user {name}")
            time.sleep(5)
            speak("boss, do you want to download the profile picture of this account!")
            condition = takecommand().lower()
            if "yes" in condition:
                x = instaloader.Instaloader()
                x.download_profile(name, profile_pic_only=True)
                speak("profile picture is saved in my folder")

            else:
                pass

        elif 'take screenshot' in query or "take a screeshot" in query or "screenshot" in query or 'screenshot this' in query:
            speak("boss, please tell me the name for this screenshot file")
            name = takecommand().lower()
            speak("hold the screen for few seconds, i am taking screenshot ")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak(" boss,screenshot is saved in our main folder")
        elif "you can sleep now" in query:
            speak("Thanks for using me boss.")
            speak("i will be there for you when ever you call me", )
            speak("Have a good day")
            sys.exit()
        elif "what is the time now" in query or "time" in query:
            cur_time = datetime.datetime.now().strftime("%I: %M %p")
            speak("its " + cur_time + ",boss")
            print(cur_time)
        elif 'play' in query:
            query = query.replace('play', '')
            pywhatkit.playonyt(query)
            speak('playing' + query)


        elif "bye" in query or "sleep" in query or "go to sleep" in query or "sleep now" in query:
            speak("Thanks for using me boss")
            speak("i will be there for you when ever you call me")
            speak("have a good day")

            sys.exit()
        elif 'shutdown' in query:
            os.system("shutdown /s /t 5")

        elif "who is" in query:
            try:
                query = query.replace("who is", "")
                info = wikipedia.summary(query, 2)
                speak(info)
                print(info)
            except:
                speak("sorry no matchings found")
                continue

        elif 'booring' in query or 'i am bored' in query or 'boring' in query:
            speak('boss,should I play some music')
            condition = takecommand().lower()
            if "yes" in condition:
                music_dir = "D:\\music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))
            else:
                pass


        elif 'restart' in query:
            os.system("shutdown /r /t 5")
