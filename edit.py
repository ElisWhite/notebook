import PySimpleGUI as sg
from Notebook import Notebook, delete, inserch, update, save, get_all, print_all, get_by_id
import os, sys
import note_gui
def Edit(id_Note):
    note = get_by_id(id_Note)

    layout = [
        [sg.InputText(note.title, font="Roboto 25", justification="center", size=(35, 1), key="title_input")],
        [sg.InputText(note.text, justification="center", font="Roboto 15", size=(55, 1), key="text_input")], # add Scroll
        [sg.Image(note.img, background_color="red", size=(105,100)), sg.Push(), sg.Image(note.media, background_color="green", size=(105,100)), sg.Push(),  sg.Push(),sg.Button("Edit", size=(12, 1),  visible=False)],
        #[ ], #надо вернутся!!!
        [sg.Input(key="edit_image", use_readonly_for_disable=True, visible=False, default_text=note.img),sg.FileBrowse("Edit image", size=(12, 1), file_types=(("GIF Files", "*.gif"), ("PNG Files", "*.png"), ("All Files" "*.*")), enable_events=True, key= "edit_img"), sg.Push(), sg.Input(key="media", use_readonly_for_disable=True, visible=False, default_text=note.media), sg.FileBrowse("Edit media", size=(12, 1), enable_events=True, file_types=(("GIF Files", "*.gif"), ("PNG Files", "*.png"), ("All Files" "*.*")),key= "edit_media"), sg.Push(), sg.Button("Edit", size=(12, 1), enable_events=True, key= "edit", button_color="#0f0f0f")]

    ]
    window=sg.Window(note.get_title(), layout, size=(600, 550))

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED or event == "close":
            break
        if event == "edit":
            title = values["title_input"]
            text = values["text_input"]
            img = values["edit_image"]
            media = values["media"]
            note.update(title, text, img, media)
            update(note)
            print(note)
            window.close()
            note_gui.Note(id_Note)


    window.close()
    note_gui.Note(id_Note)


#Edit(7)
