#import tkinter and ttk module 
from tkinter import *
from tkinter import ttk


#create root node
root = Tk()


#create entrybox event
entry = ttk.Entry(root)
entry.pack()

#virtual events have doubl <
entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

#add a new event binding and bind to event 
#print odd number to console when odd number
entry.event_add('<<OddNumber>>', '1', '3', '5', '7', '9')
entry.bind('<<OddNumber>>', lambda e: print("Odd Number!"))

#prints out virtual event and what keys trigger the event to console
print(entry.event_info('<<OddNumber>>'))

#programmatically trigger an event
entry.event_generate('<<OddNumber>>')
entry.event_generate('<<Paste>>')

#create main loop
root.mainloop()