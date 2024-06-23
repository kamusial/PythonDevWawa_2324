import PySimpleGUI as sg
import pandas as pd

def load_csv_file(file_path):
    return pd.read_csv(file_path)

def save_csv_file(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)

layout = [
    [sg.Text("CSV File Path:"), sg.Input(key='-FILEPATH-'), sg.FileBrowse(file_types=(("CSV Files", "*.csv"),))],
[sg.Button("Load CSV"), sg.Button("Save CSV"), sg.Button("Exit")]