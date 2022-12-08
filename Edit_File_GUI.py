import tkinter as tk
from FileIO import FileIO
from tkinter import messagebox
# A GUI window to edit text

class EditDocument:
    
    def __init__(self, fileContent):
        self.fileContents=fileContent
        self.window = tk.Tk()
        self.window.title("Edit File")
        self.window.geometry("500x500")
        self.textBox = tk.Text(self.window)
        self.textBox.insert(tk.INSERT, fileContent)
        self.textBox.pack()

        self.button = tk.Button(self.window, text="Save", width=10, bg='gray', bd=3, command=lambda: self.save())
        self.button2 = tk.Button(self.window, text="Exit", width=10, bg='gray', bd=3, command=lambda: self.exit())
        self.button.pack()
        self.button2.pack()
        self.window.attributes('-topmost', True)

        self.window.mainloop()
        
        
        
    def save(self):
        FileHandler=FileIO()
        lenOfPrevContent = len(self.fileContents)
        curText=self.textBox.get(1.0, tk.END)
        
        if(curText[0:lenOfPrevContent]==self.fileContents) and len(curText[lenOfPrevContent:])>0:
            FileHandler.appendToFile('data/message.txt', curText[lenOfPrevContent:])
        else:
            FileHandler.writeFile('data/message.txt', curText)
            

    def exit(self):
        self.window.destroy()