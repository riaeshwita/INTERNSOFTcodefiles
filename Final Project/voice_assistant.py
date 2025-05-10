import os
import time
import subprocess
import requests
import webbrowser
import wikipedia
import datetime
import pyttsx3
import speech_recognition as sr
import wolframalpha

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning Roux")
    elif hour >= 12 and hour <= 18:
        speak("Hello, Good Afternoon Roux")
    else:
        speak("Hello, Good Evening Roux")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"User said: {statement}\n")
        except Exception:
            speak("Pardon me, please say that again.")
            return "None"
        return statement

# Refactored assistant logic to run in the background
def start_assistant_logic(log_function):
    wishMe()
    log_function("Assistant started...\n")

    while True:
        statement = takeCommand().lower()
        if statement == "none":
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("Your personal assistant Jarvis is shutting down. Goodbye!")
            log_function("Assistant shutting down...\n")
            break

        if 'wikipedia' in statement:
            speak("Searching Wikipedia...")
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            log_function(f"Wikipedia search result: {results}\n")

        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open")
            log_function("YouTube opened\n")

        elif "open google" in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open")

        elif "open gmail" in statement:
            webbrowser.open_new_tab("https://mail.google.com")
            speak("Gmail is open")

        elif "close chrome" in statement or "close browser" in statement:
            speak("Closing Chrome browser")
            os.system("taskkill /f /im msedge.exe")

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What's your city name?")
            city_name = takeCommand()
            complete_url = f"{base_url}appid={api_key}&q={city_name}"
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(f"Temperature: {current_temperature} K, Humidity: {current_humidity}%, Weather: {weather_description}")
            else:
                speak("City not found")

        elif "time" in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "who are you" in statement or "what can you do" in statement:
            speak("I am Jarvis, your personal assistant. I can open websites, tell the time and weather, search Wikipedia, and answer questions.")

        elif "who made you" in statement or "who created you" in statement:
            speak("I was built by Roux at AiRobosoft")

        elif "open stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com")
            speak("Stack Overflow is open")

        elif "news" in statement:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are the latest headlines")

        elif "search" in statement:
            query = statement.replace("search", "")
            webbrowser.open_new_tab(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}")

        elif "ask" in statement:
            speak("Ask me any computational or geographical question")
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)

        elif "log off" in statement or "sign out" in statement or "shut down" in statement:
            speak("Okay, your PC will shut down in 10 seconds")
            os.system("shutdown /s /t 10")

    time.sleep(2)
