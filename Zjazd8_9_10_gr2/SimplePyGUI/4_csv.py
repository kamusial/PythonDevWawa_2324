import PySimpleGUI as sg
import pandas as pd

def load_csv_file(file_path):
    return pd.read_csv(file_path, sep=';')

def save_csv_file(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)

layout = [
    [sg.Text("CSV File Path:"), sg.Input(key='-FILEPATH-', enable_events=True), sg.FileBrowse(file_types=(("CSV Files", "*.csv"),))],
    [sg.Table(values=[[2, 3, 4, 5],[5, 6, 7, 8], [54, 6, 76, 4]], headings=[1, 2, 3, 4], display_row_numbers=True, auto_size_columns=False, num_rows=20, key='-TABLE-')],
    [sg.Button("Load CSV"), sg.Button("Save CSV"), sg.Button("Exit")]
]

window = sg.Window("CSV Viewer and Editor", layout, resizable=True)

data = None
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == 'Load CSV':
        file_path = values['-FILEPATH-']
        if file_path:
            try:
                data = load_csv_file(file_path)
                table_data = data.values.tolist()
                headings = list(data.columns)
                window['-TABLE-'].update(values=table_data)
                sg.popup("CSV loaded successfully!")
            except Exception as e:
                sg.popup_error(f"Failed to load CSV: {e}")

    if event == 'Save CSV':
        if data is not None:
            save_path = sg.popup_get_file('Save CSV', save_as=True, file_types=(("CSV Files", "*.csv"),))
            if save_path:
                try:
                    save_csv_file(data, save_path)
                    sg.popup("CSV saved successfully!")
                except Exception as e:
                    sg.popup_error(f"Failed to save CSV: {e}")
        else:
            sg.popup_error("No data to save!")

window.close()