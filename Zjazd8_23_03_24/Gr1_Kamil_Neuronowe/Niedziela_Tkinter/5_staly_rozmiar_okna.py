import tkinter as tk

root = tk.Tk()
root.title('zablokowanie zmiany rozmaru okna')
root.geometry('600x400+1200+50')
#root.resizable(False, True)
root.minsize(300, 300)
root.maxsize(700, 500)
root.attributes('-alpha', 0.8)   # przeźroczystość
root.attributes('-topmost', 1)   # na wierzchu

root.mainloop()