#import tkinter and ttk module 
from tkinter import *
from tkinter import ttk

#create root node 
root = Tk()


#create canvas object 
canvas = Canvas(root, width = 640, height = 480, background = 'white')
canvas.pack()

#create funtion for click event
#x_root displays value relative to the screen
#x displays value relative to GUI/canvas
def mouse_press(event):
	global prev
	prev = event
	print('type: {}'.format(event.type))
	print('widget: {}'.format(event.widget))
	print('num: {}'.format(event.num))
	print('x_root: {}'.format(event.x_root))
	print('y_root: {}'.format(event.y_root))


#create a bind event for whenever B1 is clicked
#B1 = left click
#B2 = scroll click
#B3 = right click

def draw(event):
	global prev
	canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
	prev = event


#create button event binded to the canvas
canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

#create main loop
root.mainloop()
