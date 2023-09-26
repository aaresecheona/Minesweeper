import tkinter as tk
from tkinter import messagebox



class MinesweeperGUI:

    def __init__(self):
        self.root = tk.Tk()
        
        self.root.title("Minesweeper")

        self.root.geometry("700x500")

        self.label = tk.Label(self.root, text='Minesweeper', font=("Ariel", 22))
        self.label.pack(padx=10, pady=10)

        self.buttonFrame = tk.Frame(self.root)

        self.btnDic = {}

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    
    def createButtonColumns(self, numColumns, numRows):
        t = 1
        for colNum in range(1,numColumns+1):
            self.buttonFrame.columnconfigure(colNum, weight=1)
            for rowNum in range(1, numRows+1):
                self.btnDic["btn{0}".format(str(colNum)+'.'+str(rowNum))] = tk.Button(self.buttonFrame, text = str(t), font=('Ariel', 15))
                self.btnDic["btn{0}".format(str(colNum)+'.'+str(rowNum))].grid(row=rowNum, column=colNum, sticky='news')
                t+=1
        self.buttonFrame.pack()


    def on_close(self):
        if messagebox.askyesno(title="Quit?", message='Are you sure you want to quit?'):
            self.root.destroy()

    def start(self):
        self.root.mainloop()


game = MinesweeperGUI()
game.createButtonColumns(18,14)
game.start()
