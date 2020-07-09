import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import pyjokes 

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is") 
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
    
def wishme():
    
    speak("Hello! I'm the most humanlike conversational Artificial intelligence aissistan!")
    speak("welcome back sir!")
    time()
    date()
    hour =  datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning sir!")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour<24:
        speak("Good Evening sir!")
    else:
        speak("Good night sir")

    speak("AI at your service. please tell me how can i help you ?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(query)
 
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query

def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
     wishme()
     while True:
        query = takecommand().lower()
        if 'time' in query:
             time()
        elif 'date' in query:
            date()
        
        elif 'how are you' in query:
            speak("Thank you for asking, I'M well how can i help you ? ")

        
        elif 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'search in chrome' in query:
            speak("what should i search ?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" 
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'remember that' in query:
            speak("what should i remember that ?")
            data = takecommand()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt','r')
            speak("you said me to remember that"+remember.read())

        elif 'joke'in query:
            jokes()

        elif 'goodbye' in query:
            speak("see you soon back have a nice day")

        elif 'offline' in query:
            quit()   




























