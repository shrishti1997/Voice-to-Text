import speech_recognition as sr
import os

r = sr.Recognizer();
file_name = ""
bye="bye"

#get file name from user
while(True):
    #get file name from user
    print("Enter file name ")
    file_name = input()
    file_path = "./"+file_name+".txt"
    #check if the file name already exists
    #if doesn't create file
    if os.path.isfile(file_path) == False:
        file_name = file_path[2:]
        break
    else:
        #if does then ask user again for name
        print("file already exists..")
        print("Try giving some other name ",end = '  ') 
    
while(True):
    with sr.Microphone() as source:
        # Open function to open the file "MyFile1.txt"  
        # (same directory) in append mode and 
        file1 = open(file_name,"a") 
        print("Speak anything to test")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language='en')
            if text == bye:
                print("aborting..")
                break
            print("You said : {}".format(text))
            file1.write(text+'\n')
            
        except:
            print("Sorry. We could not hear what you said")

