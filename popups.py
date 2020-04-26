# this file is for popups
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_file("./view/popups.kv")


class NoteCreationPopup(Popup):
    pass


class NoteSavedPopup(Popup):
    pass


class NoteDeletionPopup(Popup):
    pass


class ColorChangePopup(Popup):
    pass


class NameChangePopup(Popup):
    pass


class NotImplementedPopup(Popup):
    pass


class NoFilepathPopup(Popup):
    pass


class FirstNotePopup(Popup):
    pass


class ExitPopup(Popup):
    text = StringProperty("Are you sure you want to exit?\nChanges have been saved")

    ok_text = StringProperty("OK")
    cancel_text = StringProperty("Cancel")

    __events__ = ("on_ok", "on_cancel")

    def ok(self):
        self.dispatch("on_ok")
        self.dismiss()

    def cancel(self):
        self.dispatch("on_cancel")
        self.dismiss()

    def on_ok(self):
        App.get_running_app().stop()

    def on_cancel(self):
        pass
