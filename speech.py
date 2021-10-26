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


#import the related packages
