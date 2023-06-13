import datetime
import sqlite3
import gtts
#import pygame
import pyttsx3
import speech_recognition as sr


class Notebook:
    def __init__(self, title, text, img=None, media=None, id=None):
        self.id = id
        self.title = title
        self.text = text
        self.img = img
        self.media = media
        self.date = datetime.datetime.now()

    def get_title(self):
        return self.title

    def set_date(self, date):
        self.date = date

    def update(self, title, text, img, media):
        self.title = title
        self.text = text
        self.img = img
        self.media = media
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"""
ID: {self.id}
TITLE: {self.title}
TEXT: {self.text}
DATE: {self.date}
"""


# DB
def start():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    qwery = """CREATE TABLE IF NOT EXISTS notebook(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    text TEXT,
    img TEXT,
    media TEXT,
    date NUMERIC);"""
    cursor.execute(qwery)
    conn.commit()
    conn.close()

def save(obj):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    qwery_add = """INSERT INTO notebook VALUES (?, ?, ?, ?, ?, ?); """
    cursor.execute(qwery_add, (obj.id, obj.title, obj.text, obj.img, obj.media, obj.date))
    conn.commit()
    conn.close()
    print("Add ok")

def update(obj):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    qwery = """UPDATE notebook set title= ?, text = ?, img = ?, media = ?, date = ? where id = ? """
    cursor.execute(qwery, (obj.title, obj.text, obj.img, obj.media, obj.date, obj.id))
    conn.commit()
    conn.close()
    print("Update ok")

def delete(obj):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    qwery = """DELETE FROM notebook WHERE id=?;"""
    cursor.execute(qwery, (obj.id,))
    conn.commit()
    conn.close()

def get_by_id(id_note):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    qwery = """SELECT * FROM notebook WHERE id=?;"""
    cursor.execute(qwery, (id_note,))
    res = cursor.fetchall()
    print(res)
    note = Notebook(res[0][1], res[0][2], img=res[0][3], media=res[0][4], id=res[0][0])
    conn.close()
    return note

def get_all():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    qwery = """SELECT * FROM notebook ORDER BY date DESC"""
    cursor.execute(qwery)
    res = cursor.fetchall()

    notes = []
    for item in res:
        n = Notebook(item[1], item[2], img=item[3], media=item[4], id=item[0])
        n.set_date(item[5])
        notes.append(n)

    print(res)
    conn.close()
    return notes

def inserch(title, order="за датой оновлення"):
    ## conn = sqlite3.connect("notes.db")
    # cursor = conn.cursor()
    # if order == 'за датой оновлення':
    #     order = 'date DESC'
    # elif order == 'за алфавітом':
    #     order = 'title ASC'
    # qwery = """SELECT * FROM notebook WHERE title=? ORDER BY ?"""
    # cursor.execute(qwery, (title, order))
    # res = cursor.fetchall()
    #
    # notes = []
    # for item in res:
    #     n = Notebook(item[1], item[2], img=item[3], media=item[4], id=item[0])
    #     n.set_date(item[5])
    #     notes.append(n)
    # conn.close()
    # return notes
    notes = get_all()
    search_notes = []
    for note in notes:
        if title in note.title or title in note.text:
            search_notes.append(note)

    return search_notes

def filter(order="за датой оновлення"):
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    order1 = "title ASC"
    print("filter, ", order)
    if order == 'за датой оновлення':
        order1 = 'date DESC'
    elif order == 'за алфавітом':
        order1 = 'title ASC'
    qwery = """SELECT * FROM notebook ORDER BY ?"""
    cursor.execute(qwery, (order1,))
    res = cursor.fetchall()

    notes = []
    for item in res:
        n = Notebook(item[1], item[2], img=item[3], media=item[4], id=item[0])
        n.set_date(item[5])
        notes.append(n)
    conn.close()
    return notes

def print_all(arr):
    for item in arr:
        print(item)
'''def voice(obj):
    pygame.init()
    pygame.mixer.init()
    sound_stop = pygame.USEREVENT + 1
    pygame.mixer.music.set_endevent(sound_stop)
    i = 0
    while i<1:
        ts = gtts.gTTS(obj.text, lang="en")
        sound_file = "text"+'.mp3'
        ts.save(sound_file)
        i+=1
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while True:
            event = pygame.event.wait()
            if event.type == sound_stop: break
        pygame.mixer.music.unload()

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
'''
def recognizer():
    recognizer = sr.Recognizer()
    ''' recording the sound '''
    with sr.Microphone() as source:
        #print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source)
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source)
        #print("Done recording")
        ''' Recorgnizing the Audio '''
    try:
        #print("Recognizing the text")
        text = recognizer.recognize_google(recorded_audio, language="uk-UK")
        #print("Decoded Text : {}".format(text))
        return text
    except Exception as ex:
        print(ex)
        return ""
def title_str(title):
    while len(title)<13:
        title += "."
    else:
        title = title[0:10]+'...'

    return title
if __name__=="__main__":
    #start()
    n1 = Notebook("My title", "text")
    #save(n1)
   # n2 = Notebook("title", "My second note")
    #save(n2)
    #save(n1)
    #save(n2)
   # res = get_all()
   # print_all(res)
   # print_all(inserch("title"))
   #print(recognizer())

