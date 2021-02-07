from tkinter import *


def generate():
	pass

root = Tk()
root.title("Separator Generator")

language_label = Label(root, text="Programming language: ")
language_label.pack()

language_input = Entry(root)




generate_button = Button(root, text="Generate separator", command=generate)
generate_button.pack()


root.mainloop()