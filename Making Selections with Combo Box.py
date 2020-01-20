#import tkinter packages and ttk module 
from tkinter import *
from tkinter import ttk 


#create root instance 
root = Tk()

#create variable that with store combo box
month = StringVar()

#create combobox and store text in month variable 
combobox = ttk.Combobox(root, textvariable = month)

#pack the combobox onto GUI
combobox.pack()

#configure combobox values 
combobox.config(values = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 
	'June', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


#get value back from combo box
month.get()

#change the value showing up in the combo box
month.set('Select A Value')

#create a string for the spin box 
year = StringVar()

#create instance of SpinBox
Spinbox(root, from_ = 1990, to = 2014, text = year).pack()






