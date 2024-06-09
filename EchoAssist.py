import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
        
    print(f"Hello , {greeting}!")
    speak(f"Hello , {greeting}!")
    print("I am ragnar Sir, please tell me how may I help you?")
    speak("I am ragnar Sir, please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I did not catch that. Please say that again.")
        return "None"
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return "None"
    
    return query.lower()

def search_wikipedia(query):
    query = query.replace("wikipedia", "").strip()
    speak("Searching Wikipedia...")
    try:
        results = wikipedia.summary(query, sentences=2)
        link = wikipedia.page(query).url
        print(f"\n{results}")
        speak(f"According to Wikipedia, {results}")
        print(f"For more info go to - {link}")
        speak(f"For more info go to - {link}")
    except wikipedia.exceptions.DisambiguationError as e:
        print("Disambiguation error. Be more specific.")
        speak("Disambiguation error. Be more specific.")
    except wikipedia.exceptions.PageError:
        print("Page not found.")
        speak("Page not found.")
    except Exception as e:
        print("An error occurred.")
        speak("An error occurred.")

def open_website(url, site_name):
    print(f"\nOpened {site_name}")
    speak(f"Opened {site_name}")
    webbrowser.open(url)

def open_application(path, app_name):
    try:
        os.startfile(path)
        print(f"\nOpened {app_name}")
        speak(f"Opened {app_name}")
    except FileNotFoundError:
        print(f"{app_name} not found.")
        speak(f"{app_name} not found.")
    except Exception as e:
        print("An error occurred.")
        speak("An error occurred.")

def get_date():
    final_date = datetime.datetime.now().date()
    print(f"\nSir, today's date is {final_date}")
    speak(f"Sir, today's date is {final_date}")

def get_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\nSir, the time right now is {strTime}")
    speak(f"Sir, the time right now is {strTime}")

def exit_program():
    print("\nYou can call me again at any time, Bye Sir")
    speak("You can call me again at any time, Bye Sir")
    exit()

if __name__ == "__main__":
    wishMe()
    command_functions = {
        "wikipedia": search_wikipedia,
        "open google": lambda: open_website("https://google.com", "Google"),
        "open youtube": lambda: open_website("https://youtube.com", "YouTube"),
        "open instagram": lambda: open_website("https://instagram.com", "Instagram"),
        "open twitter": lambda: open_website("https://twitter.com", "Twitter"),
        "open reddit": lambda: open_website("https://reddit.com", "Reddit"),
        "open pinterest": lambda: open_website("https://pinterest.com", "Pinterest"),
        "open github": lambda: open_website("https://github.com", "GitHub"),
        "open netlify": lambda: open_website("https://netlify.com", "Netlify"),
        "open discord": lambda: open_application("C:\\Users\\HP\\AppData\\Local\\Discord\\app-1.0.9007\\Discord.exe", "Discord"),
        "open vs code": lambda: open_application("C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", "Visual Studio Code"),
        "open pycharm": lambda: open_application("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.1\\bin\\pycharm64.exe", "PyCharm"),
        "open intellij": lambda: open_application("C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2022.2.1\\bin\\idea64.exe", "IntelliJ"),
        "date": get_date,
        "time": get_time,
        "exit": exit_program
    }
    
    while True:
        query = takeCommand()
        if query == "None":
            continue
        
        found = False
        for command, function in command_functions.items():
            if command in query:
                function(query)
                found = True
                break
        
        if not found:
            print("Command not recognized.")
            speak("Command not recognized.")
