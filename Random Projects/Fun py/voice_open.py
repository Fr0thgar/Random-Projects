import pyttsx3
import os

engine = pyttsx3.init()
pyttsx3.speak("Enter Number to open Application")
while True:
    print("enter number to open applicatrion\n")
    
    print("\n1.MICROSOFT WORD \t 2.MICROSOFT POWERPOINT \n\t 3. MICROSOFT EXCEL \t 4.GOOGLE CHROME \n\t 0. FOR EXIT")
    
    p = input()
    p = p.upper()
    print(p)
    
    if("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
        pyttsx3.speak("Type Again")
        print(".")
        print(".")
        continue
    
    elif ("4" in p):
        os.system("start chrome")
        
    elif ("9" in p):
        os.system("start notepad")
        
    elif ("3" in p):
        os.system("start excel")
        
    elif ("2" in p):
        os.system("start powerpoint")
    
    elif ("1" in p):
        os.system("start winword") 
    
    elif ("0" in p):
        pyttsx3.speak("Exiting")
        break
    
    else:
        pyttsx3.speak(p)
        print("is invalid, please try again")
        pyttsx3.speak("is invalid, please try again")