#import tkinter package and ttk module 
from tkinter import *
from tkinter import ttk

#create root instance 
root = Tk()

#create a notebook
notebook = 	ttk.Notebook(root)

#add notebook to GUI
notebook.pack()


#create a frame for the notebook
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

#add frame to notebook
notebook.add(frame1, text = 'One')
notebook.add(frame2, text = 'Two')

#add button to frame1 
ttk.Button(frame1, text = 'Click Me').pack()

#create a third frame 
frame3 = ttk.Frame(notebook)

#insert frame3 into notebook
notebook.insert(1, frame3, text = 'Three')

#remove the third frame from notebook
notebook.forget(1)

#add back in frame 3
notebook.add(frame3, text = 'Three')

#check the ID of the widget 
notebook.select()

#use the notebook index method to check position selected on GUI
notebook.index(notebook.select)

#change the position selected 
notebook.select(2)

#change tab 1 to hidden
notebook.tab(1, state= 'hidden')

#check the text at index positon 1 
notebook.tab(1, 'text')






