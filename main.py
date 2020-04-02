# main window of the notepad
from kivy.core.window import Window
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

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'borderless', False)
Config.write()


class Notepad(App):
    def __init__(self, **kwargs):
        # TODO: get window size from json file
        App.__init__(self)

    def build(self):
        return MainWindow()


class EditMenu(FloatLayout):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__()


class MainWindow(FloatLayout):
    # buttonit tähän ja viewit ym

    close = ObjectProperty()
    options = ObjectProperty()
    edit = ObjectProperty()
    #text_edit = ObjectProperty()

    tab1 = ObjectProperty()
    tab2 = ObjectProperty()
    tab3 = ObjectProperty()
    tab4 = ObjectProperty()
    tab5 = ObjectProperty()
    tab6 = ObjectProperty()
    tab7 = ObjectProperty()
    tab8 = ObjectProperty()


    def __init__(self, **kwargs):
        super(MainWindow, self).__init__()
        self.clipboard_text = ""
        self.filepath = ""

    def close_app(self, size, parent_size):
        print(size)
        print(parent_size)

    def toggle_options(self, size, parent_size):
        print(size)
        print(parent_size)

    def toggle_edit(self, size, parent_size):
        print(size)
        print(parent_size)

    def change_tab(self, size, parent_size):
        print(size)
        print(parent_size)



if __name__ == '__main__':
    Notepad().run()
