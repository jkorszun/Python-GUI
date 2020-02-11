#import tkinter and ttk module 
from tkinter import *
from tkinter import ttk

#create root node 
root = Tk()


#create some labels 
label1 = ttk.Label(root, text = 'Label 1')
label2 = ttk.Label(root, text = 'Label 2')
label1.pack()
label2.pack()

#bind an event to the button press for label1
label1.bind('<ButtonPress>', lambda e: print('Button Pressed with Label'))
label1.bind('<1>', lambda e: print("Button 1 was pressed"))

#create a bind method on the root
root.bind('<1>', lambda e: print('<1> Root'))

#unbind the button
label1.unbind('<1>')
label1.unbind('<ButtonPress>')

#bind all to esable key root
root.bind_all('<Escape>', lambda e: print("Escape was pressed"))

#create loop for main node 
root.mainloop()