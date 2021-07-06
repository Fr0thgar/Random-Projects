import os
import pyttsx3
import speech_recognition as sr

class pythonhub:
    def takeCommands(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening')
            r.pause_threshold = 0.7
            audio = r.listen(source)
            
            try:
                print("Recognizing")
                Query = r.recognize_google(audio, language='en-in')
                
                print("the query is printed='", Query,"'")
            except Exception as e:
                print(e)
                print("Say that again please")
                return "None"
        return Query
    
    def Speak(self, audio):
        engine = pyttsx3.init('sapi5')
        
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()
        
    def quitSelf(self):
        self.Speak("do you want tot switch off the computer?")
        
        take = self.takeCommands()
        choice = take
        if "yes" in choice:
            
            print("Shutting down the computer")
            self.Speak("Shutting down the computer")
            os.system("shutdown /s /t 30")
        if "no" in choice:
            print("Thank you!")
            self.Speak("Thank you!")
            
if __name__ == '__main__':
    Maam = pythonhub()
    Maam.quitSelf()