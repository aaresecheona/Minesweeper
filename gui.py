import tkinter as tk
from tkinter import messagebox



class Minesweeper:

    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("700x500")

        self.label = tk.Label(self.root, text='Your Message')
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5)
        self.textbox.bind('<KeyPress>', self.shortcut)
        self.textbox.pack(padx=10, pady=10)


        self.check_state = tk.IntVar()


        self.check = tk.Checkbutton(self.root, text='Show messagebox', variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='show message', command=self.show_message)
        self.button.pack(padx=10, pady=10)


        self.root.protocol("WM_DELETE_WINDOW", self.on_close)



        self.root.mainloop()
    

    def show_message(self):
        print('Hellow World')
        print(self.check_state.get())

        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))


    def shortcut(self, event):
        if event.state == 12 and event.keysym == "Return":
            self.show_message()



    def on_close(self):
        if messagebox.askyesno(title="Quit?", message='Are you sure you want to quit?'):
            self.root.destroy()


Minesweeper()