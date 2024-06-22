import PySimpleGUI as sg
import pandas as pd
from pathlib import Path

def convert_to_csv(filepath, output_folder, sheet, separator, decimal):
    df = pd.read_excel(filepath, sheet)
    filename = Path(filepath).stem
    outputfile = Path(output_folder) / f'{filename}.csv'
    df.to_csv(outputfile, sep=separator, decimal=decimal, index=False)

layout = [
    [sg.Text("Plik wejsciowy"), sg.Input(key='wejscie'), sg.FileBrowse(file_types=(('Pliki excel', '*.xls*'),))],
    [sg.Text("Folder wYjsciowy"), sg.Input(key='wyjscie'), sg.FolderBrowse()],
    [sg.Button("konwertuj"), sg.Button("Wyjdz"), sg.Exit(button_text='EXXXXIT', button_color='blue')]

]

window = sg.Window("Moj program konversja do csv", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Wyjdz", "EXXXXIT"):
        break
    if event == "konwertuj":
        convert_to_csv(
            filepath=values['wejscie'],
            output_folder=values['wyjscie'],
            sheet='Call Center Data',
            separator='|',
            decimal='.'
        )

window.close()

