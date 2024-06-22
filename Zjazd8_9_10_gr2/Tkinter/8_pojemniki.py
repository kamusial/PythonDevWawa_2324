import tkinter as tk
root = tk.Tk()
root.title('Pojemniki')
root.geometry('400x200')

box1 = tk.Label(root, text='Pojemnik 1', bg='green', fg='white')
box1.pack(ipady=10, fill=tk.X)
box2 = tk.Label(root, text="Pojemnik 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True)

root.attributes('-topmost', 1)
root.mainloop()