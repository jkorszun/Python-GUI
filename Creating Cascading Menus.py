#import tkinter
from tkinter import *

#create top level root
root = Tk()

#restrict design of menu to look presentable
#each menu will have dashed line without command
#removes pair off menu 
root.option_add('*tearOff', False)

#create menu variable for root
menubar = Menu(root)

#configure menubar 
root.config(menu = menubar)

#add menu item
#each manu item needs to be child to menu object
file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)


#add menu items created above 
menubar.add_cascade(menu = file, label = "File")
menubar.add_cascade(menu = edit, label = "Edit")
menubar.add_cascade(menu = help_, label = "Help")

#add a command to the File Menu
file.add_command(label = 'New', command = lambda: print("New File"))

#add a separating line to the file menu
file.add_separator()

#add some more commands to file menu 
file.add_command(label = 'Open...', command = lambda: print("Opening File..."))
file.add_command(label = 'Save', command = lambda: print("Save File"))

#set entry configuration 
#does not create entry shortcut, but displays the option
file.entryconfig('New', accelerator = 'Ctrl + N')


#to delete a menu option
file.delete('Save')

#create new variable with Save 
save = Menu(file)

#add save as sub menu 
file.add_cascade(menu = save, label = 'Save')

#add command to save menu 
save.add_command(label = 'Save As', command = lambda: print('Saving As'))
save.add_command(label = 'Save All', command = lambda: print('Save All'))


#add a radio button 
choice  = IntVar()

#add in radio button 
edit.add_radiobutton(label = 'One', variable = choice, value = 1)
edit.add_radiobutton(label = 'Two', variable = choice, value = 2)
edit.add_radiobutton(label = 'Three', variable = choice, value = 3)


#draw a menu on the screen using post method 
#pixel coodinates are in relation to entire screen not GUI
file.post(400, 300)
