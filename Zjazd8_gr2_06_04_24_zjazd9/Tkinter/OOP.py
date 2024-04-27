import tkinter as tk
from tkinter import messagebox

class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Program GUI')
        self.root.geometry('600x400+1200+80')
        self.root.attributes('-alpha', 0.5)
        self.root.attributes('-topmost', 1)
        self.root.config(background='Light Blue')

        self.label = tk.Label(self.root, text='moj text')
        self.label.config(
            background='#555',
            fg='#ccc',
            font=('Arial', 20),
            padx=20,
            pady=10)
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 15))
        self.textbox.bind('<KeyPress>', self.short)
        self.textbox.pack(padx=10, pady=10)

        self.root.mainloop()

    def short(self, event):
        print(event.keysym)
        print(event.state)
        if event.keysym == 'Return' and event.state == 12:
            print('Nacisnales enter + ctrl')
MyGui()
