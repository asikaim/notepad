# this file is for note related cruds
"""
        # TODO: at the beginning of main,
        # read filepath from .ini
    if self.filepath == "":
        self.on_save_as()
    else:
        f = open(self.filepath,'w')
        f.write(self.text_view.text)
        f.close()
    def on_save_as(self, *args):

        content = SaveDialog(save_file = self.save_as_file,
                             cancel = self.cancel_dialog)
        self._popup = Popup(title="Save As File",content=content,
                            size_hint=(0.9,0.9))
        self._popup.open()
"""


def createNote():
    # Check if note exists
    # If it does, update existing one
    # else create new one with category and id
    pass


def updateNote():
    # Check if note exists
    # If it does, update existing one
    # else create error
    pass


def getNote(id):
    # get note with category and id
    pass


def deleteNote(id):
    # call
    pass
