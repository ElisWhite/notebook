import PySimpleGUI as sg
from Notebook import Notebook, delete, inserch, update, save, get_all, print_all, get_by_id, filter, title_str
import one_note
import note_gui
import serch
import threading

def Main_Window():
    layout = [
        [sg.Text("NOTEBOOK", font="Roboto 25", justification="center", size=(35, 1))],
        [sg.Push()],
        [sg.Input(justification="center", border_width="5", font="Roboto 15", key="input_text"), sg.Image("search.png", enable_events=True, key="search")],
        [sg.Push()],
        [sg.InputCombo(values=["за алфавітом","за датой оновлення"], key="filter", default_value="за датой оновлення", enable_events=True)],
    ]
    notes = []
    notebooks = get_all()
    for note in notebooks:
        temp = [sg.Push(), sg.Text(title_str(note.title), font="Arial", background_color="#0f0f00", enable_events=True, key=f'note{note.id}', justification="center"), sg.VerticalSeparator(), sg.Text(title_str(note.text), font="Arial", enable_events=True, key=f'notes{note.id}'), sg.Push(), sg.Image("delete.png", size=(25,25), enable_events=True, key=f'del{note.id}'), sg.Push()]
        notes.append(temp)
        notes.append([sg.Text('-'*60, size=(60,1), justification='center')])


    layout.extend(notes)
    layout.append([sg.Push(), sg.Push(), sg.Push(),sg.Image("add-svg.png", enable_events=True, key="add_new"), sg.Push()])
    window = sg.Window('NoteBook',finalize=True, icon="C:\\Users\\Admin\\Desktop\\ІТ Харьков\\питон\\Notebook\\notebbok.png").Layout([[sg.Column(layout,size=(630,400), scrollable=True, element_justification="center", vertical_scroll_only=True,sbar_trough_color='black')]])
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == "search":
            if len(values['input_text']) > 0:
                notes = inserch(values["input_text"], values["filter"])
                if len(notes)>0:
                    window.close()
                    serch.serch(notes)
            print("Click")


        if event == "filter":
            print("filter")
            print(values['filter'])
            notes = filter(order=values['filter'])
            print_all(notes)




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
            Main_Window()
            print("Delete ok")


        if event == "add_new":
            print("ADD")
            window.close()
            one_note.Add_Note()


    window.close()

    '''
    
    import PySimpleGUI as sg
    from Notebook import Notebook, delete, inserch, update, save, get_all
    
    title = [sg.Text("Notebook", size=(100, 1), text_color="#f0f0ff", font="Roboto 25")]
    
    search = [sg.InputText(key="input_search", size=(50, 5), justification="center"), sg.Image("Notebook/search.png", size=(25,25), enable_events=True, key="Image")]
    
    filter = [sg.InputCombo(values=["за алфавітом","за датой оновлення"], key="filter", default_value="за датой оновлення")]
    
    notes = []
    notebooks = get_all()
    for note in notebooks:
        temp = [sg.Text(note.title, font="Arial", background_color="#0f0f00", enable_events=True, key=f'note{note.id}', justification="center"), sg.VerticalSeparator(), sg.Text(note.text[0:5]+"...", font="Arial")]
        notes.append(temp)
        notes.append([sg.Text('-'*60, size=(60,1), justification='center')])
    
    layout = [
        title,
        [sg.HorizontalSeparator()],
        search,
        [sg.HorizontalSeparator()],
        filter,
    ]
    layout.extend(notes)
    layout.append([sg.Image("Notebook/add-svg.png", enable_events=True, key="add_new"), sg.Push(), sg.Push()])
    
    window = sg.Window("Notebook" ).Layout([[sg.Column(layout, scrollable=True, size=(450, 450), vertical_scroll_only=True)]])
    event, values = window.read()
    while event not in (None, "Cancel"):
        event, value = window.read()
        if event == "Image":
            print("Click")
        if event.startswith("note"):
            print(event)
        if event == "add_new":
            print("ADD")
    '''
if __name__ == "__main__":
    Main_Window()
