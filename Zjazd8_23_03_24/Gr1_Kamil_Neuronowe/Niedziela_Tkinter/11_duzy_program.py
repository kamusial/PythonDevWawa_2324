import tkinter as tk
from tkinter import messagebox

class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Duzy program')
        self.root.geometry('600x400+1300+50')
        self.root.attributes('-alpha', 0.8)
        self.root.attributes('-topmost', 1)
        self.root.config(background='Light Blue')

        self.label = tk.Label(self.root, text='moj text')
        self.label.config(
            background='#555',
            fg='#ccc',
            font=('Arial', 20),
            padx=20,
            pady=10)
        self.label.pack()

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 15))
        self.textbox.bind('<KeyPress>', self.short)
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text='show', font=('Arial', 15), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show Message', font=('Arial', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text='Clear', font=('Arial', 16), command=self.clear)
        self.clearbtn.pack()

        self.root.mainloop()
    def short(self, event):
        print(f'event: {event}')
        print(f' keysym: {event.keysym}')
        print(f' state: {event.state}')
        if event.keysym == 'Return' and event.state == 44:
            print('Wcisnieto ctrl + Enter')
            self.show_message()

    def show_message(self):
        print('Wywolana funkcja show message')
        messagebox.showinfo(title='Message', message='wiadomosc')

    def clear(self):
        self.textbox.delete('1.0', tk.END)
MyGui()