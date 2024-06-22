import tkinter as tk
root = tk.Tk()
root.attributes('-topmost', 1)
root.geometry('500x600')
root.title('moj program')

label = tk.Label(root, text='Siema', font=('Arial', 20))
label.pack(padx=20, pady=50)
textbox = tk.Text(root, height=3, font=('Arial', 14))
textbox.pack(padx=10, pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 15))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text='2', font=('Arial', 15))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text='3', font=('Arial', 15))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn1 = tk.Button(buttonframe, text='4', font=('Arial', 15))
btn1.grid(row=1, column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text='5', font=('Arial', 15))
btn2.grid(row=1, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text='6', font=('Arial', 15))
btn3.grid(row=1, column=2, sticky=tk.W+tk.E)

next_btn = tk.Button(root, text='TEST')
next_btn.place(x=200, y=200, height=100, width=100)

buttonframe.pack(fill='x')
root.mainloop()