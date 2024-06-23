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

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Add Contact':
        name = values['-NAME-']
        phone = values['-PHONE-']
        email = values['-EMAIL-']
        if name and phone and email:
            contact = f'{name} | {phone} | {email}'
            contacts.append(contact)
            window['-CONTACT LIST-'].update(contacts)
            window['-NAME-'].update('')
            window['-PHONE-'].update('')
            window['-EMAIL-'].update('')

    if event == 'Edit Contact':
        selected_contact = values['-CONTACT LIST-']
        if selected_contact:
            index = contacts.index(selected_contact[0])
            contacts[index] = f"{values['-NAME-']} | {values['-PHONE-']} | {values['-EMAIL-']}"
            window['-CONTACT LIST-'].update(contacts)
            window['-NAME-'].update('')
            window['-PHONE-'].update('')
            window['-EMAIL-'].update('')

    if event == 'Remove Contact':
        selected_contact = values['-CONTACT LIST-']
        if selected_contact:
            contacts.remove(selected_contact[0])
            window['-CONTACT LIST-'].update(contacts)


window.close()