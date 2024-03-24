import tkinter as tk

root = tk.Tk()
root.title('wysrodkowane')
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print(screen_height, screen_width)

# otwórz okno na środku
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.mainloop()


root.mainloop()