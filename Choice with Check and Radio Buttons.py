#import tkinter package and ttk module 
from tkinter import *
from tkinter import ttk

#create root 
root = Tk()

#create check button 
checkButton = ttk.Checkbutton(root, text = 'SPAM?')
checkButton.pack()


#use stringvar to create string instance 
spam = StringVar()

##set spam variable to SPAM!
spam.set("SPAM!")

#check the value of the spam variable 
spam.get()

#assign the check button the variable spam
checkButton.config(variable = spam, onvalue = "SPAM!", offvalue = "Boo Spam!")

#check value if checked/unchecked
spam.get()

#make radio button called breakfast
breakfast = StringVar()

#create radio button and store breakfast string instance 
ttk.Radiobutton(root, variable= breakfast, text = "SPAM", value = 'SPAM').pack()

#create several more buttons
ttk.Radiobutton(root, variable= breakfast, text = "Eggs", value = 'Eggs').pack()

ttk.Radiobutton(root, variable= breakfast, text = "Sausage", value = 'Sausage').pack()

ttk.Radiobutton(root, variable= breakfast, text = "SPAM", value = 'SPAM').pack()

#check the value of the button
breakfast.get()

#change the check variable to value fo breakfast
#value will change based on text selected from radio button
checkButton.config(textvariable = breakfast)









