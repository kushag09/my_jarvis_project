import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Sir, please tell me how may I help you?")

def takeCommand():
    '''
    It takes microphone input form user and string as output
    '''

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold=1
        r.phrase_threshold=0.0
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-UK')
        print(f"Your Query, Sir: {query}\n")

    except Exception as e:
        # print(e)
        print("Sorry, couldn't get you Sir")
        speak("Sorry, couldn't get you Sir")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    # server.login('anshhiro.dholakia')
    # server.sendmail('anshhiro.dholakia',to,content)
    server.close()

if __name__ == '__main__':
    wishMe()

    while True:
        query=takeCommand().lower()

        # logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching Wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:

            query=query.replace("open youtube","")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(f'https://youtube.com')

        elif 'cs50' in query:

            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(f'https://courses.edx.org/courses/course-v1:DelftX+Calc001x+2T2020/courseware/748b996c006843d58b704b9f4755e60f/9715f9865812463381280a79f6c346e3/?child=first')

        y}')

        elif 'open google' in query:

            query=query.replace("open google","")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            query=query.replace(" ","+")
            webbrowser.get('chrome').open(f'https://google.com')

        elif 'are you' in query:
            speak("I am Erling Haaland, the Assistant. Authored by.......;Sir........; Ansh Dholkia")

        elif 'on stackoverflow' in query:
            query=query.replace(" on stackoverflow","")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
            query=query.replace(" ","+")
            webbrowser.get('chrome').open(f'https://stackoverflow.com/search?q={query}')

        elif 'play music' in query:
            music_dir='C:\\Users\\Ansh\\Videos\\YouTube videos\\Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath="C:\\Users\\Ansh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening VS Code;.....Sir")
            os.startfile(codepath)

        elif 'open python' in query:
            codepath="C:\\Python\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            speak("Opening PyCharm;.......Sir")
            os.startfile(codepath)

        elif 'the date' in query:
            date=datetime.date.today().strftime("day %d......; month %m.....; year 20%y")
            speak(f"Sir; today's date is {date}")

        elif 'send email to' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="anshdholakia100@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry...... Sir, I am not able to send this email.")

        elif 'quit' in query:
            speak("Thank you for your valuable time...;.....Over-and-out...........Sir")
            exit()

        else:continue
