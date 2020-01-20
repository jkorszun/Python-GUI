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

#add a tag to the text widget labeled my_tag and select 1.0 to word end
text.tag_add('my_tag', '1.0', '1.0 wordend')


#congifure text tag to highlight yellow
text.tag_configure('my_tag', background = 'yellow')


#remove a tag from a text 
text.tag_remove('my_tag', '1.1', '1.4')


#get tag names within an index 
text.tag_names('1.0')


#replace text in a tag
text.replace('my_tag.first', 'my_tag.last', 'That')

#insert some text 
text.insert('insert', '_')

#insert a maker for text
text.mark_set('my_mark', 'end')


#configure gravity used for mark
#gravity configures how the text will be positioned 
#ie; left or right within the box 
text.mark_gravity('my_mark', 'right')

#remove a mark using mark unset method
text.mark_unset('my_mark')

#add an image to text 
image = PhotoImage(file = '/Users/jkorszun/Desktop/Python Scripts/Python GUI Development Tkinter/Ex_Files_Python_GUI_Dev_Tkinter/Exercise Files/Ch03/python_logo.gif')



#add image to the textbox 
text.image_create('insert', image = image)

#create a button that is a child of the text widget
button = Button(text, text = 'Click Me')

#add in the button to the text widget 
text.window_create('insert', window = button)





