from popups import NoteCreationPopup
from kivy.utils import get_color_from_hex


def get_note_id(note):
    note = note.split("-", 1)[1]
    note_id = int(note.split(".", 1)[0])
    return note_id


def create_note(note, first_run=False):
    f = open(note, "w+")
    f.write("New note\n" + note)
    f.close()
    if first_run is False:
        creation_popup = NoteCreationPopup()
        creation_popup.open()


def create_placeholder_notes(filepath):
    for i in range(1, 8):
        create_note("{}\\{}-1.txt".format(filepath, i), True)


def save_note(text, note):
    f = open(note, "w")
    f.write(str(text))
    f.close()


def get_color(color):
    colors = {
        "white": "#FFFFFF",
        "red": "#FF1B1B",
        "blue": "#0011FF",
        "teal": "#00E6FF",
        "green": "#00F541",
        "purple": "#5B0090",
        "orange": "#C36800",
        "brown": "#724903",
        "yellow": "#E4EB28",
        "gray": "#E0E0E0",
        "black": "#000000",
    }
    val = get_color_from_hex(colors.get(color))
    return val


def reverse(lst):
    return [ele for ele in reversed(lst)]
