def speak(audio):
    engine.say(audio)
    print(f" : {audio}")
    engine.runAndWait()
# convert voice to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listneing....")
        r.pause_threshold=1  # agar bolte bolte ruke to listening bnd na hoje
        audio = r.listen(source,timeout=4,phrase_time_limit=5)

    try:
        print("Recognizing...")
        text=r.recognize_google(audio, language='en-in')
        print(f"You said:{text}")
    except Exception as e:
        #speak("say that again please...")
        return "none"
    text=text.lower()
    return text



def wish():
    hour=int(datetime.datetime.now().hour)
    tt=datetime.datetime.now().strftime("%H:%M:%S")

    if hour>=0 and hour<=12:
        speak(f"good morning!,its {tt}")
    elif hour>12 and hour<18:
        speak(f"good afternoon!,its {tt}")
    else:
        speak(f"good evening!,its {tt}")
    speak("Hello Sir, I am Kelly")
    speak("Your Personal Assistant")
    speak("How may I help you ")

#import the related packages
