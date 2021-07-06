import os
import pyttsx3
import speech_recognition as sr

# Creating a class
class speech:
    #   method to take choice cammands as input
    def takeCommands(self):
        #using recognizer and microphone method for input voice
        # commands
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening')
            #number of seconds of non-speaking audio
            # a phrase is considered complete
            r.pause_trheshold = 0.7
            audio = r.listen(source)
            #voice input is identified
            try:
                # listening for voice commands 
                print("Recongnizing")
                Query = r.recognize_google(audio, language='en')
                #Displaying the voice command                
                print("the query is printed ='", Query, "'")
            except Exception as e:
                # displaying the exception
                print(e)
                # handling the exception
                print("Say that again please")
                return "None"
        return Query
    # method for voice output
    def Speak(self,audio):
        # constructor ccall for pyttsx3.init()
        engine = pyttsx3.init('sapi5')
        # setting voice type and ID
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()
        
    #method to self shut down system
    def quitSelf(self):
        self.Speak("do you want to turn off the Computer?")
        #input voice command
        take = self.takeCommands()
        choice = take
        if "yes" in choice:
            # Shutting Down
            print("Shutting down")
            self.Speak("Shutting down")
            os.system("shutdown /s /t 30")
        if "no" in choice:
            #Idle
            print("Thank you")
            self.Speak("Thank you")

#driver code           
if __name__ == '__main__':
    Main = speech()
    Main.quitSelf()