# main window of the notepad
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.floatlayout import *
from kivy.uix.boxlayout import *
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.core.text import *
from kivy.core.text.markup import *
from kivy.properties import *
from kivy.uix.popup import Popup
import os


class Notepad(App):
    def __init__(self, **kwargs):
        App._init_(self)

    def build(self):
        return MainWindow()


class MainWindow(BoxLayout):
    # buttonit tähän ja viewit ym
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__()
        self.clipboard_text = ""
        self.filepath = ""


if __name__ == '__main__':
    Notepad().run()
