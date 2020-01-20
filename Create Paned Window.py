#import tkinter and ttk module theme
from tkinter import *
from tkinter import ttk

#create instance of root window
root = Tk()


#create paned window 
panedwindow = ttk.Panedwindow(root, orient = HORIZONTAL)

#pack the paned window to GUI
panedwindow.pack(fill = BOTH, expand = True)

#create frame on window 
frame1 = ttk.Frame(panedwindow, width = 100, height = 300, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow, width = 400, height = 400, relief = SUNKEN)

#add frame window to paned window
#weight add the ratio of the GUI to the frame
panedwindow.add(frame1, weight = 1)
panedwindow.add(frame2, weight = 4)

#create a third frame to the GUI
frame3 = ttk.Frame(panedwindow, width = 50, height = 400, relief = SUNKEN)


#add a widget to the window 
#insert uses the index of the frames/widgets to fit to position
panedwindow.insert(1, frame3)

#remove a paned window widget 
panedwindow.forget(1)

