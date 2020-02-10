#import tkinter and ttk module 
from tkinter import *
from tkinter import ttk

#create root node 
root = Tk()


#create a keypress callback 
#type of character
#widget is root node = . 
#keysum is thte toal
#keycode is the keys numerical value representation
#to use Enter key <Return>: {}.format.return
def key_press(event):
	print('type: {}'.format(event.type))
	print('widget: {}'.format(event.widget))
	print('char: {}'.format(event.char))
	print('keysym: {}'.format(event.keysym))
	print('keycode: {}'.format(event.keycode))

#define shortcut function
def shortcut(action):
	print(action)

#create a bind on the root node for keypress
#root.bind('<KeyPress>', key_press)
#you need to pass the parameter to lambda in the bind method
#else it will pass argument of shortcut 
root.bind('<Control-c>', lambda e: shortcut('Copy'))
root.bind('<Control-v>', lambda e: shortcut('Paste'))



#create main loop
root.mainloop()
