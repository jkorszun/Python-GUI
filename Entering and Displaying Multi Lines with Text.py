from tkinter import *

#create top level window
root = Tk()

#create textbox
text = Text(root, width= 40, height = 40)

#add to top level window 
text.pack()

#configure text wrapping options to wrap whole words
text.config(wrap = 'word')

#get all words from start and end indices of textbox
text.get('1.0', 'end')

#get first line of words
text.get('1.0', '1.end')

#insert text at logical line position
text.insert('1.0 + 2 lines', 'Inserted Message')

#insert more lines 
text.insert('1.0 + 2 lines lineend', 'and \nmore and and and and \nmore End Inserted Message2')

#delete text to the text widget 
#will not delete end line; leaves spaces
text.delete('1.0', '1.0 lineend')

#delete everything in a line 
text.delete('1.0', '3.0 lineend + 1 chars')

#replace words in a line using indicies 
text.replace('1.0','1.0 lineend', 'This is the new first line')


#disable text entry into the text field 
text.config(state = 'disabled')

#reset state back to normal
text.config(state = 'normal')



