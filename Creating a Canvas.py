#import tkinter module
from tkinter import *


#create top level tk window 
root = Tk()

#create canvas 
canvas = Canvas(root)

#pack canvas on GUI root node
canvas.pack()

#set pixel h and w
canvas.config(width = 640, height = 480)

#create a line on the canvas
line = canvas.create_line(160, 360, 480, 120, fill = 'blue', width = 5)

#change the color of line using line object
canvas.itemconfigure(line, fill = 'green')

#get coordinates of the line 
canvas.coords(line)


#change the line coordinates 
canvas.coords(line, 0, 0, 320, 240, 640, 0)

#smooth the line out 
canvas.itemconfigure(line, smooth = True)

#smooth out the line using splinestep
canvas.itemconfigure(line, splinestep = 100)

#delete the line 
canvas.delete(line)


#draw a rectangle on the canvas 
rect = canvas.create_rectangle(160, 120, 480, 360)

#create a rectangle on the canvas
canvas.itemconfigure(rect, fill = 'yellow')

#create an oval 
oval = canvas.create_oval(160, 120, 480, 360)

#create an arc 
arc = canvas.create_arc(160, 1, 480, 240)

#define start and finish for arc item 
canvas.itemconfigure(arc, start = 0, extent = 180, fill = 'green')

#create a polygon on the canvas 
poly = canvas.create_polygon(160, 360, 320, 480, 480, 360, fill = 'blue')


#add some text to the canvas
text = canvas.create_text(320, 240, text = 'Python', font = ('Courier', 32, 'bold'))

#Lift/lower method used to re-ordering objects on canvas
canvas.lower(text, oval)
canvas.lift(text)

#add a button 
button = Button(canvas, text = 'Click Me')

#add a button to the canvas 
canvas.create_window(320, 60, window = button)

#add in tags to canvas items for easier reconfiguring of "Shape"
canvas.itemconfigure(rect, tag = ('shape'))
canvas.itemconfigure(oval, tag = ('oval', 'round'))

#change all shape tags to grey
canvas.itemconfigure('shape', fill = 'grey')

#obtain the tag for an item 
canvas.gettags(oval)






