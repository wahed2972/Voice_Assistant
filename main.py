import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!")
    
    else:
        speak("Good Evening!")
        print("Good Evening!")
        
    speak("I am your Assistant Sir.Please tell me how may I help you")
    print("I am your Assistant Sir.Please tell me how may I help you")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Say that again please")
        return "None"
    return query

def sendEmail(to,content):
    with open("D:\Internship\Python- Codeclause\Voice Assistant\password.txt",'r') as file:
        pword = file.read()

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('faisalwahed21@gmail.com',pword)
    server.sendmail('faisalwahed21@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open cricbuzz' in query:
            webbrowser.open("cricbuzz.com")
            
        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime} ")
            print(f"Sir, the time is {strTime} ")
            
        elif 'the date' in query:
            dateT = datetime.date.today().strftime("%D-%M-%Y")
            speak(f"Sir, todays date is {dateT}")
            print(f"Sir, todays date is {dateT}")
            
            
        elif 'open code' in query:
            codePath = "C:\\Users\\0727tx\\Documents\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'email to wahed' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "faisalwahed21@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
                print("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Sorry ! I am not able to send this email")
                
        elif 'how are you' in query:
            speak("I am good!")
            print("I am good!")
                
        elif 'ok bye' in query:
            speak("Good Bye! Have a good day.")
            print("Good Bye! Have a good day.")
            break
            
                              