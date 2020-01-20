#import tkinter packages and ttk module
from tkinter import *
from tkinter import ttk

#create root node instance 
root = Tk()


#create entry widget
entry = ttk.Entry(root, width = 30).pack()

#retrieve currrent contents from entry field 
entry.get()

#call delete method 
#delete 0 to 1 
#in pyhon n - 1 is the specified index 
entry.delete(0, 1)

#deletes all contents
entry.delete(0, END)


#use insert mthod
entry.insert(0, "Enter your password")

#hide the characters in text field replacing with *
entry.config(show = "*")

#disable entry from text field 
entry.state(['disabled'])

#make the textbox read only 
entry.state(['readonly'])