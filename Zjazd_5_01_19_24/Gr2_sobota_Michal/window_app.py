from rates import get_rate
import tkinter
from tkcalendar import Calendar


class Window:
    def __init__(self):
        window = tkinter.Tk()
        window.title("COKOLWIEK")
        window.geometry("600x400")

        button = tkinter.Button(text="GET RATE")
        button.pack()
        button.bind("<Button-1>", self.get_rate_button_press)

        self.text = tkinter.Label(window, text="")

        self.calendar = Calendar(window, selectmode="day", date_pattern="yyyy-mm-dd")
        self.calendar.pack()

        window.mainloop()

    def get_rate_button_press(self, _):
        date_from_calendar = self.calendar.get_date()
        rate = get_rate("EUR", date=date_from_calendar)
        self.text.config(text=f"Current EUR rate is {rate}")
        self.text.pack()


if __name__ == '__main__':
    Window()
