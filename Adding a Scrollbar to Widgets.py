#import tkinter module and ttk theme
from tkinter import *
from tkinter import ttk

#create root top level node 
root = Tk()

#create text widget
#add wrap property to word wrap
text = Text(root, width = 40, height = 10, wrap = 'word')

#snap text to grid
text.grid(row = 0, column = 0)

#create a scrollbar 
#yview tells the text how far its been moved to change accordingly
scrollbar = ttk.Scrollbar(root, orient = VERTICAL, command = text.yview)

#add scrollbar to the grid
scrollbar.grid(row = 0, column = 1, sticky = 'ns')

#configure y scroll to meet scrollbar path
#scrollbar moves proportional to where in text we are scrolling 
text.config(yscrollcommand = scrollbar.set)