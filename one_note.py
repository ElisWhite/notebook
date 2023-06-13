from turtle import title
from venv import create
import PySimpleGUI as sg
import gui
from Notebook import Notebook, delete, inserch, update, save, get_all, print_all,recognizer
import os, sys
def copy_file(file_url):
    pass

def Add_Note():

    layout=[
        [sg.Text("Title", font="Roboto 15", justification="center", size=(15, 1)), sg.Input(key="title_input",size=(50, 1))],
        [sg.Text("Text", font="Roboto 15", justification="center", size=(15, 1)), sg.Input(key="text_input",size=(50, 1)), sg.Button("Rec",  size=(2, 1), enable_events=True, key= "rec")],
        [sg.Input(key="IMG", use_readonly_for_disable=True, visible=False), sg.FileBrowse("ADD IMAGE", key='-IMG-', file_types=(("JPG Files", "*.jpg"), ("PNG Files", "*.png"), ("All Files" "*.*"))), sg.Image(source = '', size = (None,None)), sg.FileBrowse("ADD MEDIA", size=(15, 1), key="media")],
        [sg.Button("Create", size=(15, 1), enable_events=True, key= "create")]
        ]


    window = sg.Window("Add new").Layout(layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == "create":
            title = values["title_input"]
            text = values["text_input"]
            img = values["IMG"]
            media = values["media"]
            add = Notebook(title, text, img=img, media=media)
            save(add)
            break

        elif event == "rec":
            sg.PopupOK("Натисніть Ок для запису")

            text = recognizer()

            window["text_input"].update(text)


    window.close()
    gui.Main_Window()
            #print("create", title, text, img, media)

#Add_Note()
