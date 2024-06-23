import PySimpleGUI as sg

# Lista kontaktów
contacts = []

layout = [
    [sg.Text('Contact Management')],
    [sg.Text('Name'), sg.InputText(key='-NAME-', size=(30, 1))],
    [sg.Text('Phone'), sg.InputText(key='-PHONE-', size=(30, 1))],
    [sg.Text('Email'), sg.InputText(key='-EMAIL-', size=(30, 1))],
    [sg.Button('Add Contact'), sg.Button('Edit Contact'), sg.Button('Remove Contact')],
    [sg.Listbox(values=[], key='-CONTACT LIST-', size=(40, 10), select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)],
    [sg.Button('Exit')]
]

window = sg.Window('Contact Management App', layout)

event, values = window.read()