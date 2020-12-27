import speech_recognition as sr
import pyttsx3

import pywhatkit
import datetime
import wikipedia
import pyjokes
import time


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    
    global command
    command = ''
    try:
        with sr.Microphone() as source:
            
            global voice
            voice = listener.listen(source)
            talk("bol bhai kese help karu tera")
           
           

            command = listener.recognize_google(voice)
            command = command.lower()
            if 'dexter' in command:

                command = command.replace('dexter', '')  
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        command=''
        pywhatkit.playonyt(song)
        
        #time.sleep(50)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'shutdown' in command:
        exit()

    else:
        talk('Please say the command again.')
    
    command=''



while True:
    run_alexa()
   # time.sleep(50)


