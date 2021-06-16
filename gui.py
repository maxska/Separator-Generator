from tkinter import *
import generator
from utils import verify_string, verify_int, is_error


###############################################################################
#                               Functions
###############################################################################


def generate_separator():
    comment_input = verify_string(
        input=comment_input_text.get(),
        name="Line comment",
        max_length=3
    )
    if is_error(comment_input):
        # display message box
        print("error 1")
        return

    separator_input = verify_string(
        input=separator_input_text.get(),
        name="Separator symbol",
        max_length=1
    )
    if is_error(comment_input):
        # display message box
        print("error 2")
        return

    width_input = verify_int(
        input=width_input_text.get(),
        name="Width",
        max_size=200
    )
    if is_error(width_input):
        # display message box
        print("error 3")
        return

    rows_input = verify_int(
        input=rows_input_text.get(),
        name="Rows",
        max_size=20
    )
    if is_error(rows_input):
        # display message box
        print("error 4")
        return

    title_input = verify_string(
        input=title_input_text.get(),
        name="Title",
        max_length=500
    )
    if is_error(title_input):
        # display message box
        print("error 5")
        return

    spacing_input = verify_int(
        input=spacing_input_text.get(),
        name="Spacing",
        max_size=100
    )
    if is_error(spacing_input):
        # display message box
        print("error 6")
        return

    result = generator.generate(
        line_comment=comment_input,
        separator_symbol=separator_input,
        total_width=width_input,
        rows=rows_input,
        title=title_input,
        preferred_spacing=spacing_input
    )

    # print(result)
    # output.configure(font=("Courier", 8))
    output.insert(1.0, result)


def get_placeholder_function(input_text, placeholder, input_Event):
    """ Returns a function for handling placeholders for the StringVar named
    'input_text'. """

    def input_placeholder_handler(event):
        """ Adds or removes placeholder to the comment_input Entry. If the text
        in the input box is the placeholder, and the user clicks in it, the
        placeholder disappears. If the user leaves the input box and it's still
        empty, the placeholder is put back. """
        text = input_text.get()

        if text == placeholder:
            input_text.set("")
            input_Event.configure(fg="white")
        elif len(text) == 0:
            input_text.set(placeholder)
            input_Event.configure(fg="grey")

    return input_placeholder_handler


###############################################################################
#                           Creating GUI elements
###############################################################################
root = Tk()
root.title("Separator Generator")


# ------------------------------------------------
# ---------    Comment label & input    ----------
# ------------------------------------------------
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


# ------------------------------------------------
# ---------       Space checkbox        ----------
# ------------------------------------------------

#space_checkbox_checked = IntVar()
# space_checkbox = Checkbutton(
#	root,
#	text="Space between line comment start and separator",
#	variable=space_checkbox_checked,
#	onvalue=1,
#	offvalue=1,
# )


# ------------------------------------------------
# ---------   Separator label & input   ----------
# ------------------------------------------------
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


# ------------------------------------------------
# ---------     Width label & input     ----------
# ------------------------------------------------
width_label = Label(root, text="Total width: ", pady=30)

width_input_text = StringVar()
width_input = Entry(
    root,
    width=30,
    fg="grey",
    textvariable=width_input_text
)
width_input_placeholder = "e.g. 80 or 50"
width_input_text.set(width_input_placeholder)
width_input_placeholder_handler = get_placeholder_function(
    width_input_text,
    width_input_placeholder,
    width_input
)
width_input.bind('<FocusIn>', width_input_placeholder_handler)
width_input.bind('<FocusOut>', width_input_placeholder_handler)


# ------------------------------------------------
# ---------     Rows label & input     ----------
# ------------------------------------------------
rows_label = Label(root, text="Separator rows: ", pady=30)

rows_input_text = StringVar()
rows_input = Entry(
    root,
    width=30,
    fg="grey",
    textvariable=rows_input_text
)
rows_input_placeholder = "e.g. 3"
rows_input_text.set(rows_input_placeholder)
rows_input_placeholder_handler = get_placeholder_function(
    rows_input_text,
    rows_input_placeholder,
    rows_input
)
rows_input.bind('<FocusIn>', rows_input_placeholder_handler)
rows_input.bind('<FocusOut>', rows_input_placeholder_handler)


# ------------------------------------------------
# ---------     Title label & input     ----------
# ------------------------------------------------
title_label = Label(root, text="Comment title: ", pady=30)

title_input_text = StringVar()
title_input = Entry(
    root,
    width=30,
    fg="grey",
    textvariable=title_input_text
)
title_input_placeholder = "e.g. 'Function declarations'"
title_input_text.set(title_input_placeholder)
title_input_placeholder_handler = get_placeholder_function(
    title_input_text,
    title_input_placeholder,
    title_input
)
title_input.bind('<FocusIn>', title_input_placeholder_handler)
title_input.bind('<FocusOut>', title_input_placeholder_handler)


# ------------------------------------------------
# ------  Preferred spacing label & input  -------
# ------------------------------------------------
spacing_label = Label(root, text="Preferred spacing around title: ", pady=30)

spacing_input_text = StringVar()
spacing_input = Entry(
    root,
    width=30,
    fg="grey",
    textvariable=spacing_input_text
)
spacing_input_placeholder = "e.g. 10"
spacing_input_text.set(spacing_input_placeholder)
spacing_input_placeholder_handler = get_placeholder_function(
    spacing_input_text,
    spacing_input_placeholder,
    spacing_input
)
spacing_input.bind('<FocusIn>', spacing_input_placeholder_handler)
spacing_input.bind('<FocusOut>', spacing_input_placeholder_handler)


# ------------------------------------------------
# ---------       Generate button       ----------
# ------------------------------------------------

generate_button = Button(
    root,
    text="Generate separator",
    pady=20,
    padx=100,
    bg="#203040",
    command=generate_separator
)


# ------------------------------------------------
# ---------            Output           ----------
# ------------------------------------------------

output = Text(
    root,
    bg="#202020",
    fg="white",
    height=10,
    width=60
)
output.configure(font=("Courier", 8))


###############################################################################
#                     Placing the elements in the window
###############################################################################

comment_label.grid(row=0, column=0)
comment_input.grid(row=0, column=1)

# space_checkbox.grid(row=1, column=0, columnspan=2)

separator_label.grid(row=2, column=0)
separator_input.grid(row=2, column=1)

width_label.grid(row=3, column=0)
width_input.grid(row=3, column=1)

rows_label.grid(row=4, column=0)
rows_input.grid(row=4, column=1)

title_label.grid(row=5, column=0)
title_input.grid(row=5, column=1)

spacing_label.grid(row=6, column=0)
spacing_input.grid(row=6, column=1)

generate_button.grid(row=7, column=0, columnspan=2)

output.grid(row=8, column=0, columnspan=2)

root.mainloop()
