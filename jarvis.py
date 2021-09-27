import pyttsx3
import datetime
import speech_recognition as sr
import sys
import os
import wikipedia
import webbrowser
import random
import smtplib



engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices') #getting details of current voice
print(voices[1].id)

engine.setProperty('voice', voices[1].id)

def speak(audio):

    engine.say(audio) 

    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Sir, I am roya . Please tell me how may I help you")   

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold =  11575
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')  #Using google for voice recognition.
        print(f"User said: {query}\n")                        #User query will be printed.

    except:
        print("Say that again please...")                     #Say that again will be printed in case of improper voice
        return "None" #None string will be returned
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rkmb9648@gmail.com', 'Ritesh9670..')
    server.sendmail('rkmb9648@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open canva' in query:
            webbrowser.open("canva.com")

        elif 'open ecs' in query:
            webbrowser.open("electrocus.com")
        
        elif 'play music' in query:
            c = random.randint(1, 4)
            music_dir = 'F:\\music\\mp3'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[c]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\LUCKY SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif 'send a email' in query:
        #     try:
        #         speak("Which mail i will send message ?")
        #         print("Which mail i will send message ?")
        #         to1 = takeCommand()
        #         to2 = '@gmail.com'
        #         to3 = to1 + to2
        #         to = to3.replace(" ", "")
        #         speak('What is subject') 
        #         content = takeCommand()  
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend harry bhai. I am not able to send this email")    

        elif 'email to lucky' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "riteshbharti262903@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend lucky bhai. I am not able to send this email")   

        elif 'sleep' in query:
            speak('Ok sir i am going to sleep now')
            exit()

        elif 'who are you' in query:
            speak('Sir I am roya')
             