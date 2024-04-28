import tkinter as tk
from tkinter import messagebox

class MyGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Program GUI')
        self.root.geometry('600x400+1200+80')
        self.root.attributes('-alpha', 0.8)
        self.root.attributes('-topmost', 1)
        self.root.config(background='Light Blue')

        #menu
        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Zamknij', command=exit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Zamknij z potwierdzeniem', command=self.zamknij)

        self.filemenu2 = tk.Menu(self.menubar)
        self.filemenu2.add_command(label='Zamknij', command=exit)
        self.filemenu2.add_command(label='pokaz wiadomosc', command=self.show_message)

        self.menubar.add_cascade(menu=self.filemenu, label="pierwszy")
        self.menubar.add_cascade(menu=self.filemenu2, label="drugi")
        self.root.config(menu=self.menubar)



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

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text='show', font=('Arial', 15), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Pokaz wiadomosc', font=('Arial', 16), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.clearbtn = tk.Button(self.root, text='wyczysc', font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)

#zamnięcie okna
        self.root.protocol('WM_DELETE_WINDOW', self.zamknij)

        self.root.mainloop()

    def show_message(self):
        print('Teraz show message')
        print(self.check_state.get())
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))

    def short(self, event):
        print(event.keysym)
        print(event.state)
        if event.keysym == 'Return' and event.state == 12:
            print('Nacisnales enter + ctrl')
            self.show_message()

    def zamknij(self):
        print('ZAAAAMKNIJ')
        if messagebox.askyesno(title='Wyjscie', message='Czy chcesz wyjsc?'):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)

MyGui()
