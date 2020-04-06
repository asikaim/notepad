# main window of the notepad
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import *
from kivy.uix.boxlayout import *
from kivy.uix.settings import SettingsWithSpinner
from kivy.core.text import *
from kivy.core.text.markup import *
from kivy.properties import *
from kivy.config import Config
from settingsjson import settings_json
import os

Config.set("graphics", "resizable", False)
Config.set("graphics", "width", "360")
Config.set("graphics", "height", "640")
Config.set("graphics", "borderless", False)
Config.write()


class Notepad(App):
    def __init__(self, **kwargs):
        App.__init__(self)

    def build(self):
        self.settings_cls = SettingsWithSpinner
        self.use_kivy_settings = False
        return MainWindow()

    def build_config(self, config):
        config.setdefaults("category", {
            "categoryID": "1",
            "categoryName": "Notes",
            "categoryColor": "white",
        })
        config.setdefaults("application", {
            "window": "360x640",
            "filePath": "/notes/",
            "language": "English",
        })

    def build_settings(self, settings):
        settings.add_json_panel("Settings", self.config, data=settings_json)

    def on_config_change(self, config, section, key, value):
        pass


class EditMenu(FloatLayout):
    Builder.load_file("./view/editmenu.kv")

    delete = ObjectProperty()
    image = ObjectProperty()
    link = ObjectProperty()
    save = ObjectProperty()

    def delete_note(self):
        pass

    def add_image(self):
        pass

    def link_note(self):
        pass

    def save_note(self):
        pass


class NotePanel(TabbedPanel):
    # TODO: ScrollView (?)
    #       Connection to notes and categories etc.
    Builder.load_file("./view/notepanel.kv")

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


class MainWindow(FloatLayout):
    # buttonit tähän ja viewit ym
    Builder.load_file("./view/notepad.kv")

    close = ObjectProperty()
    settings = ObjectProperty()
    edit = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__()
        self.clipboard_text = ""
        self.filepath = ""
        self.panel = NotePanel()
        self.add_widget(self.panel)

    def close_app(self):
        exit()

    def open_settings(self):
        if state == "down":
            self.settings = SettingsPanel()
            self.add_widget(self.settings)
        else:
            self.remove_widget(self.settings)

    def toggle_edit(self, state):
        if state == "down":
            self.menu = EditMenu()
            self.add_widget(self.menu)
        else:
            self.remove_widget(self.menu)

    def change_tab(self, size, parent_size):
        print(size)
        print(parent_size)


if __name__ == "__main__":
    Notepad().run()
