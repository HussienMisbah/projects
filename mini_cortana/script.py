import speech_recognition as sr
import os
import sys
import pyttsx3
import time
import subprocess

def speak(file) :
    print(f"funciton has been called with file = {file}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.setProperty('volume',1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 for male

    content = open(file,'r')
    for line in content :
        engine.say(line)
        engine.runAndWait()
    engine.stop()
    print("[+] done")
    return


r = sr.Recognizer()
action = False 

while True :
    with sr.Microphone() as source:
        print("Talk :")
        audio_text = r.listen(source)
        print("Time over, try again")

        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print("Text: "+ text.lower())
        except:
             print("Sorry, I did not get that")
             continue

        path = "C:\\"  # set the path 

        # Basic Functions

        if text.lower().strip() == 'quit' :
            print("bye")
            break

        elif text.lower() == 'reset' :
            os.system("cls")
            continue
        
 # TODO
        # elif text.lower() == 'stop' :
        #     print ("called !")
        #     print('waiting ')
        #     action = True 
        #     while action == True :
        #         print(".",end='') 
        #         test = input()
        #         if test == "start" :
        #             action = False
        #             break
        #     continue


       # main functions :

        elif text.lower() == 'camera' :
            os.system("start microsoft.windows.camera:")
            continue

        # open partitions
        elif "partition" in text :
            print(f"explorer.exe {text.split()[1]}:\\")
            os.system(f"explorer.exe {text.split()[1]}:\\")
            continue

 # TODO
        elif "open" in text :
            search  = text.split(' ',1)[1].lower().replace(' ','') #chrome
            flag = False
            print("searching ..")
            for root, dirs, files in os.walk(path):
                if flag :
                    break 
                for file in files:
                    if file.endswith(".exe"):
                        if file.split('.')[0].lower() == search : 
                            path_file = os.path.join(root,file)
                            # print(path_file)
                            path_to = path_file.rsplit('\\',1)[0]
                            print(path_to)
                            os.chdir(path_to)
                            subprocess.call(file,shell=True)
                            flag = True 
                            break
            continue




        elif "read" in text :
            flag = False
            search  = text.split(' ',1)[1].lower().replace(' ','')
            print(search)
            for root, dirs, files in os.walk(path):
                if flag == True :
                    break
                for file in files:
                    if file.endswith(".txt"):
                        if file.split('.')[0].lower() == search :
                            path_file = os.path.join(root,file)
                            path_to = path_file.rsplit('\\',1)[0]
                            print(path_to)
                            os.chdir(path_to)
                            print(f"{file}")
                            speak(file)
                            print("returned")
                            flag = True
                            break
                continue


        elif "website" in text :
            domain = text.split(' ',1)[1].lower().replace(' ','')
            url = f"https://{domain}.com"
            os.system(f"explorer {url}")
            continue

        elif "music" in text :
            os.system("start spotify.exe")
            continue
        else :
            continue
