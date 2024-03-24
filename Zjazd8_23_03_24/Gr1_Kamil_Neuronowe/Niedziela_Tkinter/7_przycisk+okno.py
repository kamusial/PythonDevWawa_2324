import tkinter as tk
from tkinter.messagebox import showinfo
root = tk.Tk()

def button_clicked():
    print('Przycisk wcisniety')
    showinfo(title='Warning', message='kliknieto')

button_picture = tk.PhotoImage(file='merito.png')
button = tk.Button(
    root, image=button_picture,
    text='Exit', compound=tk.TOP, command=button_clicked)
button.pack(ipadx=5, ipady=5, expand=True)
root.mainloop()