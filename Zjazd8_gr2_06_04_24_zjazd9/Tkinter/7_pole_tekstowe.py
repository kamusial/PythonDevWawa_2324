import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
entry_text = tk.StringVar()

def clicked():
    msg = f'Wpisales: {entry_text.get()}'
    showinfo(title='Info', message=msg)

frame = tk.Frame()
frame.pack(padx=10, pady=10, fill='x', expand=True)
label = tk.Label(frame, text='Wpisz cos')
label.pack(fill='x')
entry = tk.Entry(frame, textvariable=entry_text)
entry.pack(fill='x')
button = tk.Button(frame, text='kliknij', command=clicked)
button.pack(fill='x', ipadx=5, ipady=30)

root.mainloop()