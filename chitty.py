import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")   

    else:
        print("Good Evening!")  

    print("I am Chitti. Mamory 1 terrabyte. Speed 1 gighertz.")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     print("Listening...")
    #     r.pause_threshold = 1
    #     audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = input()   #r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
	myMail = input("Enter your Gmail here: ")
	myPass = input("Enter your Password here: ")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(myMail, myPass)
	email = input("Enter recipient's Gmail address here: ")
    server.sendmail(email, to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia")
            print(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            os.system("mpv '/root/Music/Music 1.mp3'")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            os.system("code")

        elif 'email to shaurya' in query:
            try:
                print("What should I say?")
                content = input()
                sendEmail(to, content)
                print("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry my friend SparX bro. I am not able to send this email")

        elif "close" in query:
            print("Thanks for using me\nBye Bye")    
            exit()

        elif "whatsapp" in query:
            webbrowser.open("web.whatsapp.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "attack him" in query:
            pass

        else:
            print("Sorry, I didn't get you!!!\nSay that again please...")

            
