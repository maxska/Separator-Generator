# Separator-Generator
An app for generating separators for your code. Sometimes it's useful to divide
a file containing many lines of code into different sections, where each 
section might have a "header". This is simply for readability and being able to 
get a better overview of the file. 

Example of a separator that could be used in
a JavaScipt file:

<pre>
//###############################################
//##########      Extra functions      ##########
//###############################################
</pre>

## How to use
You need to have python3 installed.

In your terminal emulator, write
### `python3 gui.py`

If python gives the message "ModuleNotFoundError: No module named 'tkinter'",
install tkinter by (on debian linux):
### `sudo apt-get python3-tk`