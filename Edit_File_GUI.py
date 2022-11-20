#!/usr/bin/python
import tkinter as tk

# A popup GUI window to edit text

top = tk.Tk()
def save():
    with open('test.txt', 'w') as f:
        f.write(text.get(1.0, tk.END))

top.title("Edit File")
top.geometry("500x500")

text = tk.Text(top)
text.insert(tk.INSERT, "This is a test") # We can also read and display a file in the text box here
text.pack()

button = tk.Button(top, text="Save", width=10, bg='gray', bd=3, command=lambda: save())
button.pack()

top.mainloop()