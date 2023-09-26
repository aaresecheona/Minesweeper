import tkinter as tk
from tkinter import messagebox



class MinesweeperGUI:

    def __init__(self):
        self.root = tk.Tk()
        
        self.root.title("Minesweeper")

        self.root.geometry("700x500")

        self.label = tk.Label(self.root, text='Minesweeper', font=("Ariel", 22))
        self.label.pack(padx=10, pady=10)



        
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.root.mainloop()
    


    def on_close(self):
        if messagebox.askyesno(title="Quit?", message='Are you sure you want to quit?'):
            self.root.destroy()


MinesweeperGUI()