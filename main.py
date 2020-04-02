# main window of the notepad
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
import json
import os

Config.set("graphics", "resizable", False)
Config.set("graphics", "width", "360")
Config.set("graphics", "height", "640")
Config.set("graphics", "borderless", False)
Config.write()


class Notepad(App):
    def __init__(self, **kwargs):
        # TODO: get window size from json file
        App.__init__(self)

    def build(self):
        return MainWindow()


class EditMenu(FloatLayout):

    delete = ObjectProperty()
    image = ObjectProperty()
    link = ObjectProperty()
    save = ObjectProperty()


class NotePanel(TabbedPanel):
    # TODO: ScrollView
    #       Connection to notes and categories etc.
    text_view = ObjectProperty()
    pass


class MainWindow(FloatLayout):
    # buttonit tähän ja viewit ym

    close = ObjectProperty()
    options = ObjectProperty()
    edit = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__()
        self.menu_open = False
        self.clipboard_text = ""
        self.filepath = ""
        self.panel = NotePanel()
        self.add_widget(self.panel)

    def close_app(self, size, parent_size):
        print(size)
        print(parent_size)

    def toggle_options(self, size, parent_size):
        print(size)
        print(parent_size)

    def toggle_edit(self, state):
        if state == "down" and self.menu_open is False:
            em = EditMenu()
            self.menu_open = True
        else:
            if self.menu_open is True:
                EditMenu.__del__()
                self.menu_open = False

    def change_tab(self, size, parent_size):
        print(size)
        print(parent_size)


if __name__ == "__main__":
    Notepad().run()
