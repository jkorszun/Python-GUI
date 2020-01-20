#import tkinter package and ttk module 
from tkinter import *
from tkinter import ttk


#create instance of root 
root = Tk()

#create a frame and pack to GUI
#instance of pack has to be separate onto Root
#due to not being a child of the root 
frame = ttk.Frame(root)
frame.pack()

#set the height of the frame 
frame.config(height = 100, width = 200)

#configure relief around frame 
frame.config(relief = RIDGE)


#add a button using Grid Geometry Manager 
button = ttk.Button(frame, text = 'Click Me').grid()

#change the padding on the frame
frame.config(padding = (30,15))


#create a label frame 
ttk.LabelFrame(root, height= 100, width = 200, text	= 'My Frame').pack()