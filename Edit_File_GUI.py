#!/usr/bin/python
import tkinter as tk


# A popup GUI window to edit text
class EditDocument:
    
    def __init__(self, fileContent):
        self.window = tk.Tk()
        self.window.title("Edit File")
        self.window.geometry("500x500")
        self.textBox = tk.Text(self.window)
        self.textBox.insert(tk.INSERT, fileContent)
        self.textBox.pack()

        self.button = tk.Button(self.window, text="Save", width=10, bg='gray', bd=3, command=lambda: self.save())
        self.button2 = tk.Button(self.window, text="Canel", width=10, bg='gray', bd=3, command=lambda: self.cancel())
        self.button.pack()
        self.button2.pack()

        self.window.mainloop()
        
    def save(self):
        with open('test.txt', 'w') as f:
            f.write(self.textBox.get(1.0, tk.END))
            f.close()

    def cancel(self):
        exit()