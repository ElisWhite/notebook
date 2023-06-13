import PySimpleGUI as sg
from Notebook import Notebook, delete, inserch, update, save, get_all, print_all, get_by_id, filter, title_str
import note_gui
import gui

def serch(notes):
    layout = [
        [sg.Text("NOTEBOOK", font="Roboto 25", justification="center", size=(35, 1))],
        [sg.Push()],
            ]

    res = []
    for note in notes:
        temp = [sg.Push(), sg.Text(title_str(note.title), font="Arial", background_color="#0f0f00", enable_events=True, key=f'note{note.id}', justification="center"), sg.VerticalSeparator(), sg.Text(title_str(note.text), font="Arial", enable_events=True, key=f'notes{note.id}'), sg.Push(), sg.Image("delete.png", size=(25,25), enable_events=True, key=f'del{note.id}'), sg.Push()]
        res.append(temp)
        res.append([sg.Text('-'*60, size=(60,1), justification='center')])


    layout.extend(res)
    window = sg.Window('NoteBook',finalize=True).Layout([[sg.Column(layout,size=(630,400), scrollable=True, element_justification="center", vertical_scroll_only=True,sbar_trough_color='black')]])
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event.startswith("note") or event.startswith("notes"):
            if event.startswith('notes'):
                id = int(event[5:len(event)])
                window.close()
                note_gui.Note(id)



            elif event.startswith('note'):
                id = int(event[4:len(event)])
                window.close()
                note_gui.Note(id)

        if event.startswith("del"):
            id = int(event[3:len(event)])

            delete(get_by_id(id))
            window.close()
            gui.Main_Window()
            print("Delete ok")

    window.close()
    gui.Main_Window()
