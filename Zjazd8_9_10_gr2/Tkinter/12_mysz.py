from tkinter import *

def siema(event):
    print('Nacisnieto przycisk 1')

def wyjscie(event):
    print('nacisnieto 2 razy przycisk 2, wychodze z programu')
    import sys; sys.exit()

widget = Button(None, text='Tutaj klikamy')
widget.pack()
widget.bind('<Button-1>', siema)
widget.bind('<Double-2>', wyjscie)

widget.mainloop()