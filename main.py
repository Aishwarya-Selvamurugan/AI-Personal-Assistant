import pyttsx3
import datetime
import time
import speech_recognition as sr
import wikipedia
import webbrowser
import wolframalpha
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    speak("Hi")

    if (hour < 12):

        speak("Good morning")
    elif (hour < 18):
        speak("good afternoon")
    else:
        speak("Good evening")
    time.sleep(1)
    speak("How can i help you")
wish()




def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 2000
        audio = r.listen(source, phrase_time_limit=3)

    try:
        print("Wait for few moments")

        query = r.recognize_google(audio, language='en-in')
        print(query)
        speak(query)

    except Exception as e:
        # print(e)
        speak(" say  that  again please")
        query = takecommand()

    return query

def take(question):

    app_id = "Paste your unique ID here "
    client = wolframalpha.Client('XP39GG-JVEWT52VXR')
    try:
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
        print(answer)

    except Exception as e:
        speak(" say  that  again please")
        query = takecommand()
        take(query)

if __name__ == "__main__":
    wish()
    trigger = True
    while trigger:
        querry = takecommand().lower()
        print("user said ", querry)

        if "wikipedia" in querry:
            speak("Searching in wikipedia")
            # querry = querry.replace("wikipedia", "")
            results = wikipedia.summary(querry, sentences=2)
            speak("According to wikipedia")
            webbrowser.open("https://en.wikipedia.org/wiki/" + querry)
            print(results)
            speak(results)

        elif "thank you" in querry:
            speak("You are welcome")

        elif 'search' in querry:
            querry = querry.replace("search", "")
            webbrowser.open_new_tab(querry)
            time.sleep(5)

        elif "open youtube" in querry:
            webbrowser.open("youtube.com")
            time.sleep(5)

        elif "youtube" in querry:
            webbrowser.open("https://www.youtube.com/results?search_query=" + querry)
            time.sleep(5)

        elif "open google" in querry:
            webbrowser.open("https://www.google.com/")
            time.sleep(5)

        elif "news" in querry:
            webbrowser.open("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(5)

        elif "google" in querry:
            webbrowser.open("https://www.google.com/search?q=" + querry)
            time.sleep(5)

        elif "open javatpoint" in querry:
            webbrowser.open("https://www.javatpoint.com/")
            time.sleep(5)

        elif "time" in querry:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            time.sleep(5)

        elif "stop" in querry:
            speak("Bye    see you later")
            trigger = False

        else:
            take(querry)
