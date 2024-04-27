import tkinter as tk

root = tk.Tk()
root.title('Max i min okna')
root.geometry('600x400+1200+80')
root.minsize(200, 200)
root.maxsize(800, 500)
root.attributes('-alpha', 0.8) #nieprzezroczystosc
root.attributes('-topmost', 1)  # okno zawsze na wierzchu
root.iconbitmap('./pobrane.ico')
root.mainloop()