import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import random
import wikipedia
import pyjokes
import subprocess
from  flask import Flask

listener = sr.Recognizer()
engine = pyttsx3.init()
app = Flask(__name__)
@app.route('/')


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Hey friend listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'moon' in command:
                command = command.replace('moon', '')
                print(command)
    except:
        pass
    return command

def run_moon():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'chrome' in command:
        talk('opening chome')
        engine.runAndWait()
        program="C:\Program Files\Google\Chrome\Application\chrome.exe"
        subprocess.Popen([program])
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'hello' in command or 'hi' in command:
        talk('hello how can i help you')

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        thing = command.replace('what is', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    elif 'name' in command or 'call you' in command:
        talk('you can call me moon')
    elif 'how are you' in command:
        talk('i am fine You are very kind to ask')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'thank you' in command:
        talk('you are welcome')
    elif 'who i am' in command:
        talk('you are my only friend')
    elif 'story' in command:
        when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
        who = ['namjoon', 'Jin', 'Yoongi', 'Jhope', 'Jimin', 'Taehyung', 'Jungkook']
        residence = ['Korea','India', 'Germany', 'Japan', 'England']
        went = ['cinema', 'university','seminar', 'school', 'laundry']
        happened = ['made a lot of friends','Eats a burger', 'found a secret key', 'solved a mistery', 'wrote a book']
        talk(random.choice(when) + ', ' + random.choice(who) + ' who lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
    elif 'exit' in command:
        talk('thanks for giving me your time')
        exit()
    else:
        talk('Please say the command again.')


while True:
   run_moon()



