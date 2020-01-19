#import tkinter and ttk module
from tkinter import *
from tkinter import ttk



#create intial root 
root = Tk()

#create instance of button
button = ttk.Button(root, text = 'Click Me')

#call geometry window to pack
button.pack()


#create function for button 
def callBack():
	print("Click")


#change button to react to user 
button.config(command = callBack)

#call invoke method
button.invoke()

#diable button using state method
button.state(['disabled'])

#call the instate method
#is my button in this state? boolean value 
button.instate(['disabled'])

#change button back to not being disabled 
button.state(['!disabled'])


#create new image for labelk 
logo = PhotoImage(file = '/Users/jkorszun/Desktop/Python Scripts/Python GUI Development Tkinter/Ex_Files_Python_GUI_Dev_Tkinter/Exercise Files/Ch03/python_logo.gif')
#center image to the left
button.config(image = logo, compound = LEFT)


#sub sample the image being used 5 by 5 pixels 
small_image = logo.subsample(5,5)


#reconfig button to use small image
button.config(image = small_image)














