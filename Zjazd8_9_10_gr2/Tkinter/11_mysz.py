from tkinter import *

root = Tk()
root.geometry('800x300')

def callback(e):
    print('Wskaznik jest na pozycji %d, %d' %(e.x, e.y))

root.bind('<Motion>', callback)

root.mainloop()