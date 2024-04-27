import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()

def clicked():
    showinfo(title='Info', message='kliknieto')

icon = tk.PhotoImage(file='merito.png')
button = tk.Button(
    text='przycisk',
    image=icon,
    compound=tk.TOP,
    command=clicked)
button.pack(ipadx=5, ipady=5, expand=True)

root.mainloop()