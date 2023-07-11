## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound



################### Initialized window####################

# Example Text

root = Tk()
root.geometry('450x400')
root.resizable(0,0)
root.config(bg = '#2C265D')
root.title('GetProjects - TEXT_TO_SPEECH')


##heading
Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' ,fg='white', bg ='#2C265D').place(x=100,y=20)
#Label(root, text ='GetProjects' , font ='arial 15 bold', bg = '#2C265D').pack(side = BOTTOM)




#label
Label(root, text ='Enter Text', font ='arial 17 bold', fg='white', bg ='#2C265D').place(x=20,y=100)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=80 , y=140)


###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('GetProjects.mp3')
    playsound('GetProjects.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, bg = '#77DD77', width =4).place(x=100, y=200)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = '#DB92B8').place(x=185,y=200)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=270 , y =200)


#infinite loop to run program
root.mainloop()
