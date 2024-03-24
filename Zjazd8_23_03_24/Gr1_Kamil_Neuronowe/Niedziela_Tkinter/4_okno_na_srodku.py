import tkinter as tk

root = tk.Tk()
root.title('wysrodkowane')
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height, screen_width)

# otwórz okno na środku

root.mainloop()