# Copyright (c) 2021, Xin Tan 
# All rights reserved

from tkinter import *
from Game import Game
from tkinter import messagebox
import os, sys




class Main():
    def __init__(self, main):

        self.g = Game(root)

    def on_closing(self):
        if not self.g.is_menu_frame and self.g.number_played_word != 0:
            result = messagebox.askquestion("Quit", "Save your progress?")
            if result == 'yes':
                self.g.save_progress()
        root.destroy()


if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)
elif __file__:
    application_path = os.path.dirname(__file__)

root = Tk()
root.title("Hangman")
root.geometry("1000x700")
root.resizable(0, 0)
m = Main(root)
root.protocol("WM_DELETE_WINDOW", m.on_closing)
root.mainloop()
