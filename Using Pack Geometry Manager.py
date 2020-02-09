#import tkinter and ttk theme module 
from tkinter import *
from tkinter import ttk


#create root node 
root = Tk()

#create a label 
#fill option is X and Y fills geomtrically
#BOTH uses both X and Y (all of the GUI)
label = ttk.Label(root, text = 'Hello, Tkinter!', background = 'yellow')
label.pack(fill = BOTH, expand = True)
print(label)

ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue').pack(fill = BOTH)
ttk.Label(root, text = 'Hello, Tkinter!', background = 'green').pack(fill = BOTH, expand = True)

#pack to side 
#anchor to norwest portion of GUI
#ttk.Label(root, text = 'Hello, Tkinter!', background = 'green').pack(side = LEFT, anchor = 'nw')

#add external padding to a label 
#ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue').pack(side = LEFT, padx = 10, pady = 10)

#add internal padding to the widget label
#ttk.Label(root, text = 'Hello, Tkinter!', background = 'blue').pack(side = LEFT, ipadx = 10, ipady = 10)

#call a for loop to pack widgets onto Master node
#with expand and fill options stated 
for widget in root.pack_slaves():
	widget.pack_configure(fill = BOTH, expand = True)
	print(widget.pack_info())

#forget label variable 
#the widget is not removed from code, just GUI instance 	
label.forget()

#call root mainloop method to enter main loop
root.mainloop()


