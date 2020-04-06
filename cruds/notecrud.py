# this file is for note class
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.floatlayout import *
from kivy.uix.boxlayout import *
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.core.text import *
from kivy.core.text.markup import *
from kivy.properties import *
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.lang import Builder
import json
import os



class Note:
    def __init__(self):
        self.category = None
        self.createdOn = None
        self.id = None
        self.name = None
        self.related = []

    def create(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def save(self):
        pass


def createNote():
    pass


def getNote(id):
    pass


def deleteNote(id):
    pass

class NotePanel(TabbedPanel):
    # TODO: ScrollView (?)
    #       Connection to notes and categories etc.
    Builder.load_file("notepanel.kv")

    text_view = ObjectProperty()
    next_note = ObjectProperty()
    previous_note = ObjectProperty()

    def move_to_previous(self, size1, size2):
        print("pressed")
        print(size1)
        print(size2)

    def move_to_next(self, size1, size2):
        print("pressed")
        print(size1)
        print(size2)