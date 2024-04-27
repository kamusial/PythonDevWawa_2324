import tkinter as tk

root = tk.Tk()
exit_button = tk.Button(text='Wyjscie', command=root.quit)
exit_button.pack(ipadx=10, ipady=50, expand=True)

# exit_button.place(x=100, y=100, height=100, width=100)

root.mainloop()