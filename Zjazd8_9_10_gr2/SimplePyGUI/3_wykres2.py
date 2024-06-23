import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Funkcja do rysowania wykresu
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


# Definicja układu okna
layout = [
    [sg.Text("Enter X values (comma separated):"), sg.InputText(key='-X-')],
    [sg.Text("Enter Y values (comma separated):"), sg.InputText(key='-Y-')],
    [sg.Text("Select chart type:")],
    [sg.Combo(['Line', 'Bar'], default_value='Line', key='-CHART TYPE-')],
    [sg.Button("Draw Chart"), sg.Button("Exit")],
    [sg.Canvas(key='-CANVAS-')]
]

# Tworzenie okna
window = sg.Window("Chart Drawer", layout, finalize=True)

# Główna pętla zdarzeń
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Draw Chart":
        try:
            x_values = list(map(int, values['-X-'].split(',')))
            y_values = list(map(int, values['-Y-'].split(',')))
            chart_type = values['-CHART TYPE-']

            # Czyszczenie poprzedniego wykresu
            plt.clf()

            if chart_type == 'Line':
                plt.plot(x_values, y_values)
            elif chart_type == 'Bar':
                plt.bar(x_values, y_values)

            plt.title('Generated Chart')
            plt.xlabel('X values')
            plt.ylabel('Y values')

            # Usunięcie poprzedniego widgetu kanwy
            for widget in window['-CANVAS-'].TKCanvas.winfo_children():
                widget.destroy()

            # Rysowanie wykresu w oknie
            fig = plt.gcf()
            draw_figure(window['-CANVAS-'].TKCanvas, fig)
        except Exception as e:
            sg.popup_error(f"Error: {e}")

window.close()