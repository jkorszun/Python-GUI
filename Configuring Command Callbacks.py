#import tkinter and ttk inter module
from tkinter import *
from tkinter import ttk

#create root node 
root = Tk()

def callback(number):
	print(number)

#create button instance
#you have to use the lambda function to pass the 
#original argument of the function in the command statement 
#else it will read it as the passing parameter, not an arugment 
ttk.Button(root, text = 'Click Me 1', command = lambda: callback(1)).pack()
ttk.Button(root, text = 'Click Me 2', command = lambda: callback(2)).pack()
ttk.Button(root, text = 'Click Me 3', command = lambda: callback(3)).pack()





root.mainloop()


