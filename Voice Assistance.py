import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import subprocess as sp
import requests

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def hi():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
        talk("Good Evening!")  
    talk("I am Olivia. Please tell me how may I help you now")

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])

def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def search_on_google(command):
    pywhatkit.search(command)

def play_on_youtube(video):
    print(pywhatkit.playonyt(video))

def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+88{number}", message)


def name(name):
    name_list = ['robin', 'nayem', 'mahinoor', 'abid', 'ashik']
    for i in range(len(name_list)):
        if name in name_list[i]:
            talk(f"Your name {name_list[i]}")

def take_command():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('listening...')
            r.pause_threshold = 1
            voice = r.listen(source)
            command = r.recognize_google(voice)
            command = command.lower()
            if 'olivia' in command:
                command = command.replace('olivia', '')
                #print(command)
    except Exception as e:
        talk('Please say the command again. i can play youtube music and many more')
        return "None"
    return command


def run_olivia():
    try:
        command = take_command()
        print(command)

        if 'play' in command:
            talk('What do you want to play on Youtube, sir?')
            video = take_command().lower()
            play_on_youtube(video)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif 'wikipedia' in command:
            person = command.replace('wikipedia', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'date' in command:
            talk('sorry, I have a headache')

        elif 'are you single' in command:
            talk('I am in a relationship with wifi')

        elif 'joke' in command:
            talk(f"Hope you like this one sir")
            talk(pyjokes.get_joke())

        elif 'creator' in command:
            talk('My creator fantastic four')
        
        elif "whatsapp " in command:
            talk(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            talk("What is the message sir?")
            message = take_command().lower()
            send_whatsapp_message(number, message)
            talk("I've sent the message sir.")
        
        elif 'open notepad' in command:
            open_notepad()

        elif 'open command' in command or 'open cmd' in command:
            open_cmd()

        elif 'open camera' in command:
            open_camera()

        elif 'open calculator' in command:
            open_calculator()

        elif 'ip address' in command:
            ip_address = find_my_ip()
            talk(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'google' in command:
            talk('What do you want to search on Google, sir?')
            query = take_command().lower()
            search_on_google(query)

        elif 'name' in command:
            talk("Please enter last 3 character in the console")
            Name_search = input("Please enter here: ")
            name(Name_search)

        elif "give" in command:
            talk(f"Here's an advice for you, sir")
            advice = get_random_advice()
            talk(advice)
            talk("For your convenience, I am printing it on the screen sir.")
            print(advice)
        
    except:
        pass

if __name__ == "__main__":
    hi()
    while True:
        run_olivia()