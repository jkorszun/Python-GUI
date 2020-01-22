#import tkinter package and ttk module
from tkinter import *
from tkinter import ttk

#create root node with constructor 
root = Tk()



treeview = ttk.Treeview()


treeview.pack()

#insert parent node to the treeview 
treeview.insert('', '0', 'item1', text = 'First Item')

#insert second and third nodes to tree
#empty string, position, name, label (optional)
treeview.insert('', '1', 'item2', text = 'Second Item')
treeview.insert('', '2', 'item3', text = 'Third Item')

#insert logo using PhotoImage
#use subset to shrink image
logo = PhotoImage(file = '/Users/jkorszun/Desktop/Python Scripts/Python GUI Development Tkinter/Ex_Files_Python_GUI_Dev_Tkinter/Exercise Files/Ch03/python_logo.gif').subsample(10, 10)

#insert logo to the treeview after item2 as subnode
treeview.insert('item2', 'end', 'python', text = 'python',image = logo)

#change treeview by item total display
#ie 5 is to display 5 items in treeview of GUI
treeview.config(height = 5)

#move an item in the treeview 
treeview.move('item2', 'item1', 'end')

#configure an item to be open in the treeview 
treeview.item('item1', open = True)

#check the status of an item 
#returns T or F
tree.item('item1', 'open')

#remove an item from a treeview 
treeview.detach('item3')

#add back in item 3 under item 2
treeview.move('item3', 'item2', '0')

#completely remove an item from a treeview 
treeview.delete('item3')

