# Copyright (c) 2021, Xin Tan 
# All rights reserved



from tkinter import *
from tkinter.ttk import *
import os

class Menu():
    def __init__(self, root, game):
        self.game = game
        self.frame_menu = Frame(root)
        self.frame_menu.grid(row=0, column=0, sticky="nsew")

        sto = Style()
        sto.configure('TButton',
                      foreground='Green')

        # Buttons for user to start a new game or to resume the previous game

        self.Resume_game_btn = Button(self.frame_menu, text='Resume',
                                  command=lambda: self.resume_game())
        self.Resume_game_btn.pack(pady=(350, 2))
        self.New_game_btn = Button(self.frame_menu, text='New Game',
                                   cursor="gumby", style='TButton', command=lambda: self.start_new_game())
        self.New_game_btn.pack()

        # txt file records information for previous game
        self.resume_file = "RESUME.txt"

        self.has_resume = self.check_previous_file()



    # get menu frame
    def menu_frame(self):
        return self.frame_menu

    # start the new game when clicked New game button
    def start_new_game(self):
        self.to_game_frame()
        self.game.open_file("GRE2910.txt")

    # resume the previous game when clicked Resume button
    def resume_game(self):
        self.to_game_frame()
        if self.has_resume:
            self.game.open_file(self.resume_file)



    # Check if there is a saved file for previous game
    def check_previous_file(self):
        self.to_game_frame()
        if not os.path.isfile(self.resume_file):
            self.Resume_game_btn['state'] = 'disable'
            return False
        else:
            return True

    # change to game frame
    def to_game_frame(self):
        self.game.show_frame(self.game.game_frame())
        self.game.is_menu_frame = False









