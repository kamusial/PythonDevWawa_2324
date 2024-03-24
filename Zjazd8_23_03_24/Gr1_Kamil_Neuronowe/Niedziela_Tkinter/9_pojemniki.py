import tkinter as tk
root = tk.Tk()
root.title('Pojemniki')
root.geometry('600x400+1200+50')

box1 = tk.Label(root, text='Pojemnik 1', bg='green')
box1.pack(ipady=10, ipadx=30, padx=10, pady=20)
box2 = tk.Label(root, text='Pojemnik 2', bg='red', fg='white')
box2.pack(ipady=20, fill=tk.BOTH, expand=True)

root.mainloop()