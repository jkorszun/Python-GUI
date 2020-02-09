#import tk inter package and ttk themed module
from tkinter import *
from tkinter import ttk        

#create master node
root = Tk()

#Create a series of root windows 
#sticky is used to tell which side fo the GUI to stick to 
#NSEW north, south, east, west (All sides for all)
ttk.Label(root, text = 'Yellow', background = 'yellow').grid(row = 0, column = 2,
 rowspan = 2, sticky = 'nsew')
ttk.Label(root, text = 'Blue', background = 'Blue').grid(row = 1, column = 0, 
	columnspan = 2, sticky = 'nsew')
ttk.Label(root, text = 'Green', background = 'Green').grid(row = 0, column = 0, 
	sticky = 'nsew', padx = 10, pady = 10)
ttk.Label(root, text = 'Orange', background = 'Orange').grid(row = 0, column = 1,
 sticky = 'nsew', ipadx = 25, ipady = 25)

#tell the row weights to reconfigure when GUI is resized 
#weight is used to scale resizing 
#weight 3 resizes 3 times the rate of row 0
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 3)
root.columnconfigure(2, weight = 1)

root.mainloop()