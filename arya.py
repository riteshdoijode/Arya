import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install speechRecgnition 
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys


engine = pyttsx3.init('sapi5') #what is sapi5? It is used to take voices from computer.
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):    
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")    

    else:
        speak("Good Evening!")
        
    speak("Arya here. How may I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.dynamic_energy_adjustment_damping = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)    
        print("Say that again please...")
        return "None"
      
    return query 


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('evillord9513289354@gmail.com', 'ritdoijode724262')
    server.sendmail('riteshdoijde7@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
       query = takeCommand().lower()

       #Logics for executing tasks based on query

       if 'wikipedia' in query:
         speak('Searching Wikipedia...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=3)
         speak("According to Wikipedia")
         print(results)
         speak(results)

       elif 'hello' in query:
           speak('Hey there nice to meet you.')
       
       elif 'love you' in query:
           speak('I love you too.')

       elif 'launch youtube' in query:
          webbrowser.open_new_tab("https://youtube.com")

       elif 'launch 80' in query:  
          webbrowser.open_new_tab("https://the.hiveos.farm/farms/2372048/workers/5268527/")

       elif 'open google' in query:
          webbrowser.open_new_tab("https://google.com")  

       elif 'open stack overflow' in query:
          webbrowser.open_new_tab("https://stackoverflow.com")

       elif 'play songs' in query:
          music_dir = 'E:\\Ritesh\\Error E\\Songs\\English\\Songs#2021\\Songs#8'
          songs = os.listdir(music_dir)
          #print(songs)
          os.startfile(os.path.join(music_dir, songs[0]))

       elif 'time' in query:
          strTime = datetime.datetime.now().strftime("%H:%M") 
          speak(f"Sir, the time is {strTime}")

       elif 'open code' in query:
          codePath = "C:\\Python\\Microsoft VS Code\\Code.exe" 
          os.startfile(codePath) 

       elif 'open task manager' in query:
          codePath = "C:\\Windows\\System32\\Taskmgr.exe"
          os.startfile(codePath)

       elif 'open brave browser' in query:
          codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
          os.startfile(codePath)

       elif 'friends' in query:
            speak("Wassup bitches. How you doing?")

       elif 'email to ritesh' in query:
          try:
            speak("What should i say?")
            content = takeCommand()
            to = "riteshdoijode7@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent.")
          except Exception as e:
            print(e)
            speak("Sorry the email is not sent to the given request!")

       elif 'thank you' in query:
           speak("Thankyou sir, have a great day ahead")

       elif 'device' in query:
            speak("All systems running normally. Next reporting in T minus 1 hour")

       elif 'exit' in query:
            speak("Thankyou sir, have a great day ahead.")
            sys.exit(0)

       
        
       #else:
           #speak("Sorry for the inconvenience, this command cannot be processed. Please wait for ferther updates. ")
           #sys.exit(0)