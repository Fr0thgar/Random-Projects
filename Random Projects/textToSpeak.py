from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.config(bg='ghost white')
root.title("Fr0thgar - Text_to_Speech")


Label(root, text='Text_to_Speech', font='airal 20 bold', bg='white smoke').pack()
Label(root, text='Fr0thgar', font='arial 15 bold',
      bg='white smoke').pack(side=BOTTOM)

Label(root, text='Enter Text', font='arial 15 bold',
      bg='white smoke').place(x=20, y=60)

Msg = StringVar()

entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)


def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save('Fr0thgar.mp3')
    playsound('Fr0thgar.mp3')


def Exit():
    root.destroy()


def Reset():
    Msg.set("")


Button(root, text="Play", font='arial 15 bold',
       command=Text_to_speech, width=4).place(x=25, y=140)
Button(root, text='Exit', font='arial 15 bold',
       command=Exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, text='Reset', font='arial 15 bold',
       command=Reset).place(x=175, y=140)

root.mainloop()
