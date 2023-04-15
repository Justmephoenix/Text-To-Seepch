#importing tkinter module
from tkinter import *
#Python Text To speech version3
import pyttsx3


#creating object of tkinter
win=Tk()
#setting title of window 
win.title("TEXT TO SPEECH")
#setting geometry
win.geometry("800x500")
win.configure(bg='black')


def Text_To_Speech():
    #initialize the python text to speech module
    en=pyttsx3.init()
    #setting voices
    voices=en.getProperty('voices')
    #setting a rate for the speech
    en.setProperty('rate',150)
    #setting female voice
    en.setProperty('voice',voices[1].id)
    #getting the text from the input entry
    en.say(speech.get())
    #run the text to speech
    en.runAndWait()
    #after speak delete the text upto end
    speech.delete(0,END)

#creating a entry for text
speech=Entry(win,font=('Italic',18,'bold'))
speech.pack(pady=20)
#creating a button for speak
button=Button(win,text="speak",font=('Helvatica',10,'bold'),command=Text_To_Speech,bg='#C0C0C0',fg='black')
button.pack(pady=20)


win.mainloop()
