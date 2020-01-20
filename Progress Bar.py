#import tkinter packages and ttk module 
from tkinter import *
from tkinter import ttk


#create root instance 
root = Tk()


#create instance of progress bar 
progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 200)

#add to window
progressbar.pack()


#configure progress bar for indeterminate mode 
#progressbar.config(mode = 'indeterminate')

#start progress bar 
#progressbar.start()

#end the progress bar
#progressbar.end()

#use derterminate mode 
progressbar.config(mode = 'determinate', maximum = 11.0, value = 4.3)


#increase the value of the progress bar by 1 
#if you exceed the specified max, your progress bar will restart 100 at 0 and add remainder 
progressbar.step(1)


#create a variable called value
value = DoubleVar()

#store the value of value in progressbar
progressbar.config(variable = value)

#add a scale to the progressbar
scale = ttk.Scale(root, orient = HORIZONTAL, length = 400, variable = value, from_ = 0.0, to = 11.0)

#append the scalebar to the GUI
scale.pack()


#set initial value for scalebar
scale.set(3.1)

