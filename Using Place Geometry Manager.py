#import tkinter modele and ttk themes
from tkinter import *
from tkinter import ttk        

#create root node
root = Tk()

#specify geometry of GUI usnig geometry manager 
root.geometry('640x480+200+200')

#create some labels 
#rel properties are fractional values between 0 and 1 and 
#specify the width and height of current parent widget (root)
ttk.Label(root, text = 'Yellow', background = 'yellow').place(x = 100, y = 50, width = 100, height = 50)
ttk.Label(root, text = 'Blue', background = 'blue').place(relx = 0.5, rely = 0.5, anchor = 'center', relwidth = 0.5, relheight = 0.5)
ttk.Label(root, text = 'Green', background = 'green').place(relx = 0.5, x = 100, rely = 0.5, y = 50)
ttk.Label(root, text = 'Orange', background = 'orange').place(relx = 1.0, x = -5, y = 5, anchor = 'ne')


#call root main loop function
root.mainloop()
