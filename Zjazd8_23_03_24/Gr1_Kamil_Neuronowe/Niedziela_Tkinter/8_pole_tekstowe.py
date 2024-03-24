import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()
entry_text = tk.StringVar()

def button_clicked():
    msg = f'Wpisales: {entry_text.get()}'
    showinfo(title='Info', message=msg)

frame = tk.Frame(root)
frame.pack(padx=20, pady=20, expand=True, fill='x')

label = tk.Label(frame, text='Wpisz sentencje')
label.pack(expand=True, fill='x')
entry = tk.Entry(frame, textvariable=entry_text)
entry.pack(expand=True, fill='x')
button = tk.Button(frame, text='Kliknij', command=button_clicked)
button.pack(padx=50)




root.mainloop()