from tkinter import *


def generate():
	pass


def comment_input_placeholder(event):
	""" Adds or removes placeholder to the comment_input Entry. """
	text = comment_input_text.get()

	
	if text == placeholder:
		print("B")
		comment_input_text.set("")
	if len(text) == 0:
		comment_input_text.set(placeholder)

	return


root = Tk()
root.title("Separator Generator")

language_label = Label(root, text="Line comment syntax: ")
language_label.pack()


comment_input_text = StringVar()
comment_input = Entry(
	root, 
	width=50,
	fg="grey",
	textvariable=comment_input_text
)
comment_input.pack()

placeholder = "e.g. '//' in C++ or '#' in Python"
comment_input_text.set(placeholder)
comment_input.bind('<FocusIn>', comment_input_placeholder)
comment_input.bind('<FocusOut>', comment_input_placeholder)




temp_entry = Entry(root)
temp_entry.pack()





generate_button = Button(
	root, 
	text="Generate separator",
	pady=50, 
	bg="#002060",
	command=generate
)
						 
generate_button.pack()


root.mainloop()