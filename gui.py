from tkinter import *


###############################################################################
#								Functions
###############################################################################

def generate():
    pass


def comment_input_placeholder(event):
    """ Adds or removes placeholder to the comment_input Entry. """
    text = comment_text.get()

    if text == placeholder:
        comment_text.set("")
    elif len(text) == 0:
        comment_text.set(placeholder)

    return


###############################################################################
#							Creating GUI elements
###############################################################################

root = Tk()
root.title("Separator Generator")

language_label = Label(root, text="Line comment syntax:")


comment_text = StringVar()
comment_input = Entry(
    root,
    width=30,
    fg="grey",
	# the text in comment_input can now be accessed through comment_text:
    textvariable=comment_text  
)
placeholder = "e.g. '//' in C++ or '#' in Python"
comment_text.set(placeholder)
# Binds comment_input_placeholder function to when the user clicks on or 
# outside of comment_input:
comment_input.bind('<FocusIn>', comment_input_placeholder)
comment_input.bind('<FocusOut>', comment_input_placeholder)

temp_input = Entry(root)

generate_button = Button(
    root,
    text="Generate separator",
    pady=50,
    bg="#002060",
    command=generate
)


###############################################################################
#						Placing the elements in the window
###############################################################################

language_label.pack()
comment_input.pack()
temp_input.pack()
generate_button.pack()


root.mainloop()
