from typing import TextIO
import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('audio book/machinelearningwithtensorflow2e.pdf', 'rb'))

import pyttsx3
speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
    
speaker.stop()


speaker.save_to_file(TextIO, 'audio book/audio.mp3')
speaker.runAndWait()