# main window of the notepad
import os
from tkinter import *


class Notepad:
    __root = Tk()
    __thisWidth = 360
    __thisHeight = 640

    def __init__(self, **kwargs):
        pass

    def __quitApplication(self):
        self.__root.destroy()
        # exit()

    def run(self):
        # Run main application
        self.__root.mainloop()


if __name__ == '__main__':
    notepad = Notepad(width=360, height=640)
    notepad.run()
