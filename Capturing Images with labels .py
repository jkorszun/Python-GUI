#import tkinter package
from tkinter import *
from tkinter import ttk

#store root variable 
root = Tk()

#create label 
label = ttk.Label(root, text = "Hello Tkinter!")

#call pack geometry manager 
label.pack()

#change the label text using config command
label.config(text = "Howdy TkInter")


#change the label to be overly long 
label.config(text = "Howdy TkInter. It is nice to be this long of a message")

#use wrap length text to display on multile lines
#use 150 characrers as the wrap amount cutoff
label.config(wraplength = 150)

#justify the text 
label.config(justify = CENTER)

#change the background color of the GUI
label.config(foreground = 'blue', background = 'yellow')

#change the font text of the GUI
label.config(font = ('Courier', 18, 'bold'))

#change the text back to short string
label.config(text = 'Howdy Tkinter')


#create python photo image
logo = PhotoImage(file = '/Users/jkorszun/Desktop/Python Scripts/Python GUI Development Tkinter/Ex_Files_Python_GUI_Dev_Tkinter/Exercise Files/Ch03/python_logo.gif')

#config image property in label
label.config(image = logo)


#change the image toi text by using compound property 
label.config(compound = 'text')
label.config(compound = 'center')
label.config(compound = 'left')

#save a reference to logo
label.img = logo

#store image within label 
label.config(image = label.img)








