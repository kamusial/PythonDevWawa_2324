from tkinter import *

win = Tk()
win.geometry("750x300+1100+50")

def callback(e):
    print(e)
    x = e.x
    y = e.y
    print("Kursor na pozycji %d, %d" % (x, y))

def button1(e):
    print('Wcisnieto przycisk')

def wyjcie(e):
    print('Podwojne klikniecie, wychodze')
    import sys; sys.exit()

win.bind('<Motion>', callback)

button = Button(win, text='Klikanie')
button.pack()

button.bind('<Button-1>', button1)
button.bind('<Double-1>', wyjcie)

win.mainloop()