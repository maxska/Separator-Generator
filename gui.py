from tkinter import *


###############################################################################
#								Functions
###############################################################################


def generate():
    pass


def get_placeholder_function(input_text, placeholder, input_Event):
	""" Returns a function for handling placeholders for the StringVar named
	'input_text'. """

	def input_placeholder_handler(event):
		""" Adds or removes placeholder to the comment_input Entry. """
		text = input_text.get()

		if text == placeholder:
			input_text.set("")
			input_Event.configure(fg="white")
		elif len(text) == 0:
			input_text.set(placeholder)
			input_Event.configure(fg="grey")

	return input_placeholder_handler
	


###############################################################################
#							Creating GUI elements
###############################################################################

root = Tk()
root.title("Separator Generator")


#------------------------------------------------
#---------    Comment label & input    ----------
#------------------------------------------------
comment_label = Label(root, text="Line comment syntax: ", pady=30)

comment_input_text = StringVar()
comment_input = Entry(
    root,
    width=30,
    fg="grey",
	# the text in comment_input can now be accessed through comment_input_text:
    textvariable=comment_input_text  
)
comment_input_placeholder = "e.g. '//' in C++ or '#' in Python"
comment_input_text.set(comment_input_placeholder)
# Binds comment_input_placeholder_handler function to when the user clicks on or
# outside of comment_input:
comment_input_placeholder_handler = get_placeholder_function(
	comment_input_text, 
	comment_input_placeholder,
	comment_input
)
comment_input.bind('<FocusIn>', comment_input_placeholder_handler)
comment_input.bind('<FocusOut>', comment_input_placeholder_handler)


#------------------------------------------------
#---------   Separator label & input   ----------
#------------------------------------------------
separator_label = Label(root, text="Separator symbol: ", pady=30)

separator_input_text = StringVar()
separator_input = Entry(
    root,
    width=30,
    fg="grey",
    textvariable=separator_input_text  
)
separator_input_placeholder = "e.g. '-' or '+'"
separator_input_text.set(separator_input_placeholder)
separator_input_placeholder_handler = get_placeholder_function(
	separator_input_text, 
	separator_input_placeholder,
	separator_input
)
separator_input.bind('<FocusIn>', separator_input_placeholder_handler)
separator_input.bind('<FocusOut>', separator_input_placeholder_handler)

#------------------------------------------------
#---------       Generate button       ----------
#------------------------------------------------
generate_button = Button(
    root,
    text="Generate separator",
    pady=50,
	padx=100,
    bg="#002060",
    command=generate
)


###############################################################################
#						Placing the elements in the window
###############################################################################

comment_label.grid(row=0, column=0)
comment_input.grid(row=0, column=1)

separator_label.grid(row=1, column=0)
separator_input.grid(row=1, column=1)

generate_button.grid(row=2, column=0, columnspan=2)


root.mainloop()
