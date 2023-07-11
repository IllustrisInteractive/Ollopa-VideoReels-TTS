## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound



################### Initialized window####################

# Example Text

root = Tk()
root.geometry('450x400')
#image background
bg = PhotoImage(file="C:\\Users\\Cheska Gil\\Downloads\\tts.png")
root.resizable(0,0)
root.config(bg = '#2C265D')
root.title('GetProjects - TEXT_TO_SPEECH')


##heading
Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' ,fg='white', bg ='#8A4FBF').place(x=100,y=20)
#Label(root, text ='GetProjects' , font ='arial 20 bold', bg = '#2C265D').pack(side = BOTTOM)




#label edit color
Label(root, text ='Enter Text', font ='arial 17 bold', fg='white', bg ='#4F1964').place(x=20,y=100)


##text variable
Msg = StringVar()


#Entry
#edit
entry_field = Entry(root,textvariable =Msg, width ='50', fg='white', bg ='#8A4FBF')
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
#Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, bg = '#77DD77', width =4).place(x=100, y=200)
#Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = '#DB92B8').place(x=185,y=200)
#Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=270 , y =200)


#Test
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, fg='white', bg = '#8A4FBF', width =4).place(x=185, y=200)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, fg='white', bg = '#8A4FBF').place(x=185,y=300)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset, fg='white', bg='#8A4FBF').place(x=185 , y =350)

#infinite loop to run program
root.mainloop()
