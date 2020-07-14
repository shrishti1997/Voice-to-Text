import speech_recognition as sr
r = sr.Recognizer();
with sr.Microphone() as source:
    print("Speak anything to test")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    try:
        print("You said : {}".format(text))
    except:
        print("Sorry. We could not hear what you said")

