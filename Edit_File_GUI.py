#!/usr/bin/python
import tkinter as tk

# A popup GUI window to edit text
def save():
    with open('test.txt', 'w') as f:
        f.write(textBox.get(1.0, tk.END))
        f.close()

def cancel():
    exit()

def getFileText():
    #Get the data from the file here
    return "This is a test"

window = tk.Tk()
window.title("Edit File")
window.geometry("500x500")

textBox = tk.Text(window)
textBox.insert(tk.INSERT, getFileText()) # We can also read and display a file in the text box here
textBox.pack()

button = tk.Button(window, text="Save", width=10, bg='gray', bd=3, command=lambda: save())
button2 = tk.Button(window, text="Canel", width=10, bg='gray', bd=3, command=lambda: cancel())
button.pack()
button2.pack()

window.mainloop()
