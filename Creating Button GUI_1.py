#import tkinter package
from tkinter import *
from tkinter import ttk


#call to the TK constructor
root = Tk() 

#add a button
#pass parent "root" to button
#add text to button "Click Me"
button = ttk.Button(root, text = "Click Me")

#add button by placing on root GUI
button.pack()

#check what button does
button['text']

#change text of button
button['text'] = 'Press Me'

#use config method to change text on button
button.config(text = 'Push Me')

#button.config() checks all properties to widget

#add a label to the GUI
ttk.Label(root, text = "Hello Tkinter!").pack()



