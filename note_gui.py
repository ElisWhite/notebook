import PySimpleGUI as sg
from Notebook import Notebook, delete, inserch, update, save, get_all, print_all, get_by_id #voice
import os, sys
import gui
import edit

def Note(id_Note):
    note = get_by_id(id_Note)

    layout = [
        [sg.Push(), sg.Button("Edit", size=(15, 1), enable_events=True, key= "edit")],
        [sg.Text(note.title, font="Roboto 25", justification="center", size=(35, 1))],
        [sg.Text(note.text, justification="center", font="Roboto 15", auto_size_text=True)],
        [sg.Image(note.img, background_color="red", size=(100,100)), sg.Image(note.media, background_color="green", size=(100,100)), sg.Push(), sg.Button("Play", size=(15, 1), enable_events=True, key= "play")],
        #[ ], #надо вернутся!!!

    ]
    window=sg.Window(note.get_title(), layout, size=(600, 550))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "close":
            break
        elif event == "edit":
            window.close()
            edit.Edit(id_Note)
        elif event == "play":
            #voice(note)
            print("Stop voice")


    window.close()
    gui.Main_Window()

