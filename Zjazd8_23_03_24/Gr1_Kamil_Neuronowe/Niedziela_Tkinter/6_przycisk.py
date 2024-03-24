import tkinter as tk

root = tk.Tk()

button = tk.Button(root, text='Exit', command=root.quit)
button.pack(ipadx=30, ipady=10, expand=True)
root.mainloop()