#import tkinter module and ttk theme
from tkinter import *
from tkinter import ttk

#create top level root node
root = Tk()

#create buttons and pack buttons on root 
button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')
button1.pack()
button2.pack()


#create style object and store in style 
style = ttk.Style()

#search system for theme names 
style.theme_names()

#change theme use 
#check first 
style.theme_use()
#style.theme_use('classic')
#style.theme_use('vista')

#check which style theme object uses 
button1.winfo_class()

#configure button classes to blue foreground 
style.configure('TButton', foreground = 'blue')

#configure a new style 
#all style properties of Alarm will be inherited through TButton Style
style.configure('Alarm.TButton', foreground = 'orange', font = ('Arial', 24, 'bold'))

#configure the button style 
button2.configure(style = 'Alarm.TButton')

#map the style
style.map('Alarm.TButton', foreground = [('pressed', 'pink'), ('disabled', 'grey')])

#disable button2
button2.configure(state = 'disabled')
#or 
#button2.state(['disabled'])

#enable button2
button2.state(['!disabled'])

#check the elements of a style 
style.layout('TButton')

#check options available to that element 
style.element_options('Button.label')

#lookup a current style of a property 
style.lookup('TButton', 'foreground')

