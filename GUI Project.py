#import tkinter and ttk module
from tkinter import *
from tkinter import ttk
#import tkinter messagebox module 
from tkinter import messagebox


#create feedback class for form 
class Feedback:

	def __init__(self, master):
		
		#add title and restrict resizing
		master.title("Explore California Feedback")
		master.resizable(False, False)
		#change the background 
		master.configure(background = '#e1d8b9')

		#create styles object 
		self.style = ttk.Style()

		#configure style for Frames 
		self.style.configure('TFrame', background = '#e1d8b9')

		#configure style background for button
		self.style.configure('TButton', background = '#e1d8b9')
		self.style.configure('TLabel', background = '#e1d8b9', font = ('Arial', 11))
		self.style.configure('Header.TLabel', background = '#e1d8b9', font = ('Arial', 18, 'bold'))


		#create first frame insance for logo and header
		self.frame_header = ttk.Frame(master)
		self.frame_header.pack()

		#create logo object 
		self.logo = PhotoImage(file = '/Users/jkorszun/Desktop/Python Scripts/Python GUI Development Tkinter/Ex_Files_Python_GUI_Dev_Tkinter/Exercise Files/Ch08/tour_logo.gif')

		#create label objects to store logo and texts
		ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
		ttk.Label(self.frame_header, text = 'Thanks for Exploring!', style = 'Header.TLabel').grid(row = 0, column = 1)
		ttk.Label(self.frame_header, wraplength = 300, 
		 text = ("We're glad you chose Explore California." 
			"Please tell us what you thought about the Desert Sea Tour.")).grid(row = 1, column = 1)


		#create second frame 
		self.frame_content = ttk.Frame(master)
		self.frame_content.pack()

		#create Label objects for inputs
		ttk.Label(self.frame_content, text = 'Name:').grid(row = 0, column = 0, padx = 5, sticky = 'sw')
		ttk.Label(self.frame_content, text = 'Email:').grid(row = 0, column = 1, padx = 5, sticky = 'sw')
		ttk.Label(self.frame_content, text = 'Comments:').grid(row = 2, column = 0, padx = 5, sticky = 'sw')

		#create entry objects for user input
		self.entry_name = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))
		self.entry_email = ttk.Entry(self.frame_content, width = 24, font = ('Arial', 10))

		#create text comments
		self.text_comments = Text(self.frame_content, width = 50, height = 10, font = ('Arial', 10))

		#create entry objects for name, email, and text field for commentsß
		self.entry_name.grid(row = 1, column = 0, padx = 5)
		self.entry_email.grid(row = 1, column = 1, padx = 5)
		self.text_comments.grid(row = 3, column = 0, columnspan = 2, padx = 5)

		#create buttons for user feedback submission and form clearing
		ttk.Button(self.frame_content, text = 'Submit', command = self.submit).grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
		ttk.Button(self.frame_content, text = 'Clear', command = self.clear).grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'w')

	#define function for submit button
	#read in user input and write to console window
	def submit(self):
		print('Name: {}'.format(self.entry_name.get()))
		print('Email: {}'.format(self.entry_email.get()))
		print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
		self.clear()
		messagebox.showinfo(title = 'Explore California Feedback', message = 'Comments Submitted!')

	#define clear button for user form clear
	def clear(self):
		self.entry_name.delete(0, 'end')
		self.entry_email.delete(0, 'end')
		self.text_comments.delete(1.0, 'end')


#define main function for feedback class submission
def main():

	root = Tk()
	feedback = Feedback(root)
	root.mainloop()
 

#conditional statement that will only
#call python file if this is main script
if __name__ == "__main__": main()