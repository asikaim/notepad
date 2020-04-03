# this is for configuration view
import json
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



class Options:
    def __init__(self):
        pass

    def setCategoryToEdit(self, **kwargs):
        pass

    def setCategoryColor(self, **kwargs):
        pass

    def setCategoryName(self, **kwargs):
        pass

    def setResolution(self):
        pass

    def setFilePath(self):
        pass

    def setLanguage(self):
        pass

    def setKeybinds(self):
        pass

    def save(self):
        pass

    def cancel(self):
        pass

class OptionsDialog(FloatLayout):
    close = ObjectProperty()
    category_select = ObjectProperty()
    category_name = ObjectProperty()
    category_color = ObjectProperty()
    window_size = ObjectProperty()
    file_location = ObjectProperty()
    language_select = ObjectProperty()
    keybind_open = ObjectProperty()
    help_open = ObjectProperty()
    delete_data = ObjectProperty()
    confirm = ObjectProperty()
    cancel = ObjectProperty()