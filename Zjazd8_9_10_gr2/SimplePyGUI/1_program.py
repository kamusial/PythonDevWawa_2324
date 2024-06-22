import PySimpleGUI as sg
import pandas as pd
from pathlib import Path

def convert_to_csv(filepath, output_folder, sheet, separator, decimal):
    df = pd.read_excel(filepath, sheet)
    filename = Path(filepath).stem
    outputfile = Path(output_folder) / f'{filename}.csv'
    df.to_csv(outputfile, sep=separator, decimal=decimal)

layout = [
    [sg.Text("Pole 1ererererere"), sg.Input(), sg.FileBrowse()],
    [sg.Text("Pole 2         "), sg.Input(), sg.FolderBrowse()],
    [sg.Button("policz srednia"), sg.Button("Wyjdz")]

]

window = sg.Window("Moj program", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, "Wyjdz"):
        break
    if event == "policz srednia":
        sg.popup_error('Funkcja niezaimplemetowana')

window.close()

