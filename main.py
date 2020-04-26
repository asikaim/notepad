# main window of the notepad
from popups import (
    NoteDeletionPopup,
    NoteSavedPopup,
    ColorChangePopup,
    NameChangePopup,
    NotImplementedPopup,
    NoFilepathPopup,
    FirstNotePopup,
    ExitPopup,
)
from helpers import (
    get_note_id,
    create_note,
    create_placeholder_notes,
    save_note,
    get_color,
    reverse,
)
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.settings import SettingsWithSpinner
from kivy.uix.settings import SettingsPanel
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.lang import Builder
from settingsjson import application_settings_json, category_settings_json
import os
import glob

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
        root = MainWindow()
        return root

    def build_config(self, config):
        config.setdefaults(
            "application", {"window": "360x640", "filepath": ".\\notes", "language": "English",}
        )
        for i in range(1, 9):
            config.setdefaults(
                "category{}".format(i),
                {
                    "categoryID": "{}".format(i),
                    "categoryName": "#{} Notes".format(i),
                    "categoryColor": "white",
                },
            )

    def build_settings(self, settings):
        settings.add_json_panel(
            "Application Settings", self.config, data=application_settings_json
        )
        settings.add_json_panel(
            "Category Settings", self.config, data=category_settings_json
        )

    def on_config_change(self, config, section, key, value):
        # NOTE: No functionality yet for application setting changes
        #       since window resize / language aren't supported yet
        if config is self.config:
            if section in [
                "category1",
                "category2",
                "category3",
                "category4",
                "category5",
                "category6",
                "category7",
                "category8",
            ]:
                category_id = section[-1]
                if key == "categoryColor":
                    color = get_color(value)
                    self.root.panel.change_color(category_id, color)
                elif key == "categoryName":
                    self.root.panel.change_name(category_id, value)

    def get_note(self):
        text = self.root.panel.current_tab.content.children[0].children[1].text
        note = self.root.panel.current_tab.current_note
        return text, note


class EditMenu(FloatLayout):
    Builder.load_file("./view/editmenu.kv")

    delete = ObjectProperty()
    image = ObjectProperty()
    link = ObjectProperty()
    save = ObjectProperty()

    def __init__(self, text, note):
        self.text = text
        self.note = note
        super().__init__()

    def delete_note(self):
        self.text, self.note = App.get_running_app().get_note()
        try:
            print("Deleting: " + self.note)
            os.remove(self.note)
            App.get_running_app().root.panel.change_note("previous", delete=True)
            deletion_popup = NoteDeletionPopup()
            deletion_popup.open()
        except NameError as ne:
            print("Error while deleting file ")
            print(ne)
        except FileNotFoundError as fnfe:
            print("Error while deleting file ")
            print(fnfe)

    def add_image(self):
        not_implemented_popup = NotImplementedPopup()
        not_implemented_popup.open()

    def link_note(self):
        not_implemented_popup = NotImplementedPopup()
        not_implemented_popup.open()

    def on_save(self, *args):
        self.text, self.note = App.get_running_app().get_note()
        self.filepath = App.get_running_app().config.get("application", "filepath")
        if self.filepath == "":
            no_filepath_popup = NoFilepathPopup()
            no_filepath_popup.open()
        else:
            save_note(self.text, self.note)
            note_saved_popup = NoteSavedPopup()
            note_saved_popup.open()


class NotePanel(TabbedPanel):
    Builder.load_file("./view/notepanel.kv")

    text_view = ObjectProperty()
    next_note = ObjectProperty()
    previous_note = ObjectProperty()

    def __init__(self):
        self.path = App.get_running_app().config.get("application", "filepath")
        super().__init__()

    def show_note(self, note):
        if self.current_tab.content is not None:
            try:
                f = open(note, "r")
                s = f.read()
                self.current_tab.content.children[0].children[1].text = s
                f.close()
                self.tab_content_shown = True
            except FileNotFoundError as e:
                print(e)

    def get_latest_note(self, category):
        list_of_notes = glob.glob("{}\\{}-*".format(self.path, category))
        if list_of_notes:
            latest_note = max(list_of_notes, key=os.path.getctime)
        else:
            create_placeholder_notes(self.path)
            latest_note = "{}\\{}-1.txt".format(self.path, category)
        self.show_note(latest_note)
        return latest_note

    def change_note(self, action, delete=False):
        category = self.current_tab.text
        if self.current_tab.current_note:
            note_id = get_note_id(self.current_tab.current_note)
            if note_id > 1 and action == "previous":
                note_id = note_id - 1
            elif action == "next":
                note_id = note_id + 1
            else:
                first_note_popup = FirstNotePopup()
                first_note_popup.open()
                return
            note_text = self.current_tab.content.children[0].children[1].text

            if delete is False:
                save_note(note_text, self.current_tab.current_note)

            note = self.path + "\\" + category + "-" + str(note_id) + ".txt"
            latest_note_id = get_note_id(self.get_latest_note(category))

            if note_id > latest_note_id:
                create_note(note)

            self.current_tab.current_note = note
            self.show_note(note)
        return

    def change_color(self, category, color):
        tab = int(category) - 1
        self.reverse_list = reverse(self.tab_list)
        self.reverse_list[tab].content.background_color = color
        color_popup = ColorChangePopup()
        color_popup.open()

    def change_name(self, category, name):
        tab = int(category) - 1
        self.reverse_list = reverse(self.tab_list)
        self.reverse_list[tab].content.children[1].text = "[b] {}. {} [/b]".format(
            category, name
        )
        name_popup = NameChangePopup()
        name_popup.open()

    def get_category_color(self, category):
        color = App.get_running_app().config.get(
            "category{}".format(category), "categoryColor"
        )
        val = get_color(color)
        return val

    def get_category_name(self, category):
        name = App.get_running_app().config.get(
            "category{}".format(category), "categoryName"
        )
        val = "[b] {}. {} [/b]".format(category, name)
        return val


class MainWindow(FloatLayout):
    Builder.load_file("./view/notepad.kv")

    close = ObjectProperty()
    settings = ObjectProperty()
    edit = ObjectProperty()

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__()
        self.clipboard_text = ""
        self.panel = NotePanel()
        self.add_widget(self.panel)

    def close_app(self):
        self.text, self.note = App.get_running_app().get_note()
        save_note(self.text, self.note)
        exit_popup = ExitPopup()
        exit_popup.open()

    def open_settings(self):
        self.settings = SettingsPanel()
        self.add_widget(self.settings)

    def toggle_edit(self, state):
        if state == "down":
            self.text, self.note = App.get_running_app().get_note()
            self.menu = EditMenu(self.text, self.note)
            self.add_widget(self.menu)
        else:
            self.remove_widget(self.menu)


if __name__ == "__main__":
    Notepad().run()
