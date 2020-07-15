import speech_recognition as sr

r = sr.Recognizer();

bye="bye"

while(True):
    with sr.Microphone() as source:
        print("Speak anything to test")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        try:
            if text == bye:
                print("aborting..")
                break
            print("You said : {}".format(text))
        except:
            print("Sorry. We could not hear what you said")
