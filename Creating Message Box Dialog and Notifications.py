#import tkinter messagebox package
from tkinter import messagebox 

#create a messagebox to show dialog 
messagebox.showinfo(title = 'A Friendly Message', message = 'Hello Tkinter!')

#add a yes or no messagebox
#requires user input before progressing 
#yes or no response captured as boolean in IDLE
messagebox.askyesno(title = 'Hungry?', message = 'Do you want SPAM?')

#import filedialog package 
from tkinter import filedialog

#use file dialog object 
filename = filedialog.askopenfile()

#get filename user selected 
filename.name

#import color chooser module 
from tkinter import colorchooser 

#create a color chooser 
#when user selects a color, the item chosen is displayed and hex representation
colorchooser.askcolor(initialcolor = '#FFFFF')
