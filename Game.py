# Copyright (c) 2021, Xin Tan 
# All rights reserved


import os
import random
import Functions
from tkinter import  *
from menu import Menu

class Game():
    def __init__(self, root):

        # Define game frame
        self.frame_game = Frame(root)
        self.frame_game.grid(row=0, column=0 ) #


        # List of words to be guessed
        self.WordDictionary = []
        # a random word from WordDictionary
        self.Random_Word = ""
        self.total_words = 2910
        self.Guessing_Word = []
        self.Guessing_Word_Copy = []

        self.failed_count = 0
        self.guessing_chance = 7
        self.win = False
        self.number_played_word = 0
        self.bingo_index = []
        self.textlables = []

        # frames
        self.img_frame = Frame(self.frame_game, width=400, height=480)
        self.words_frame_outer = Frame(self.frame_game, width=600, height=380)
        self.words_frame_inner = Frame(self.words_frame_outer)
        self.btn_frame = Frame(self.frame_game, width=800, height=480)

        self.img_frame.grid(row=0, column=0, rowspan=2)

        self.words_frame_outer.grid(row=0, column=1)
        self.words_frame_outer.grid_propagate(0)
        self.words_frame_inner.place(relx=.5, rely=.5, anchor="center")
        self.btn_frame.grid(row=1, column=1, padx=(100, 100), pady=(20, 200))

        # canvas for image
        self.canvas = Canvas(self.img_frame, width=400, height=400)
        self.canvas.grid(row=0, column=0, pady=1)

        # images
        self.hangman_imgs = []
        self.hangman_imgs.append(PhotoImage(file="imgs/hanger.png"))
        self.hangman_imgs.append(PhotoImage(file="imgs/hanger1.png"))
        self.hangman_imgs.append(PhotoImage(file="imgs/hanger2.png"))
        self.hangman_imgs.append(PhotoImage(file="imgs/hanger3.png"))
        self.hangman_imgs.append(PhotoImage(file="imgs/hanger4.png"))
        self.hangman_imgs.append(PhotoImage(file="imgs/hanger5.png"))
        self.hangman_imgs.append(PhotoImage(file="imgs/hanger6.png"))
        self.hangman_imgs.append(PhotoImage(file="imgs/hangerlose.png"))
        self.hangman_imgs.append(PhotoImage(file="imgs/hangerwin.png"))
        self.hangman_imgs.append(PhotoImage(file="imgs/hangerwinall.png"))
        self.imgIndex = 0

        # set first image on canvas
        self.img = self.hangman_imgs[self.imgIndex]
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor=NW, image=self.img)

        # store 26 letter buttons in a list
        self.letter_buttons = []

        # Define and display buttons from A to Z
        i = 0
        Row = 6
        Col = 0
        while i < 26:
            letter = chr(65 + i)
            letter_button = Button(self.btn_frame, text=letter, height=2, width=4, padx=15,
                                   command=lambda c=i: self.get_user_input(self.letter_buttons[c].cget("text")))
            self.letter_buttons.append(letter_button)
            if (i % 6) == 0 or (i == 24):
                Row += 1
                Col = 0
            Col += 1
            self.letter_buttons[i].grid(row=Row, column=Col)
            i += 1

        # Define and display 'next word' button
        self.next_word_btn = Button(self.btn_frame, text="Next Word", height=2, width=8, command=self.next_game)
        self.next_word_btn.grid(row=Row, column=Col + 1, columnspan=2)

        # Define and display letters and corresponding boxes
        self.canvas_word = Canvas(self.words_frame_inner, width=400, height=400)
        self.canvas_word.pack(fill="none", expand=True, pady=100)


        # Define and display answer and hint frame
        self.canvas_ans = Canvas(self.words_frame_inner, width=400, height=20)
        self.canvas_ans.pack(fill="none", expand=True, pady=20)

        # Define answer label
        self.ans = Label(self.canvas_ans, text="")
        self.ans.pack()

        self.main_menu = Menu(root, self)
        self.show_frame(self.main_menu.frame_menu)
        self.is_menu_frame = True

    # Change menu frame to game frame
    def show_frame(self, frame):
        frame.tkraise()

    # Get game frame
    def game_frame(self):
        return self.frame_game

    # Read vocabularies from file
    def open_file(self, fname):

        # print(fname)

        if not os.path.isfile(fname):
            print("File path {} does not exist. Exiting...".format(fname))
            sys.exit()
        with open (fname, "r") as f:
            line = f.read()
            self.WordDictionary = line.split(';')
        score = self.WordDictionary[0]
        self.number_played_word = int(score)
        self.WordDictionary.remove(score)
        # print(self.WordDictionary)



        # print("End of file reading")
        f.close()
        words_count = len(self.WordDictionary)
        # print(words_count)
        # self.total_words = words_count
        self.Random_Word = self.WordDictionary[random.randint(0, (words_count - 1))]
        # print(self.Random_Word)
        # Put the to be guessed word into a list
        self.Guessing_Word = list(self.Random_Word)
        self.Guessing_Word_Copy = Functions.add_index_to_list(self.Guessing_Word)
        # print(self.Guessing_Word_Copy)


        # show letter boxes
        for index in range(len(self.Guessing_Word)):
            label = Label(self.canvas_word, text="?", bg="lightgray")
            self.textlables.append(label)
            label.grid(row=0, column=index, padx=1)
        # Define and display scoreboard
        self.score_label = Label(self.words_frame_outer, text=("SCORE: " +
                                                        str(self.number_played_word) + "/" + str(self.total_words)))
        self.score_label.grid(row=0, column=0, pady=60, padx=400)


# change state of button from disable to normal
    def button_normal(self):
        for btn in self.letter_buttons:
            btn['state'] = 'normal'

    # disable all the letter buttons
    def button_disable(self):
        for btn in self.letter_buttons:
            btn['state'] = 'disable'

    # disable next word button
    def disable_next_word(self):
        self.next_word_btn['state'] = 'disable'

    # next word button update
    def next_game(self):
        self.canvas.itemconfig(self.image_on_canvas, image=self.hangman_imgs[0])
        self.game_prep()


    # change images if wrong guess
    def change_image(self):
        if not self.win:
            self.imgIndex= self.failed_count
        if self.win:
            self.imgIndex = 8
        self.image_changing_by_index(self.imgIndex)

    # change image by index
    def image_changing_by_index(self, index):
        self.canvas.itemconfig(self.image_on_canvas, image=self.hangman_imgs[index])

    # letter update
    def letter_update(self, character, bingo_indexes):
        for index in bingo_indexes:
            label = self.textlables[index]
            label.config(text=character)

    # restore labels for new game
    def new_labels(self):
        for destroy_label in self.textlables:
            destroy_label.destroy()
        self.textlables.clear()
        for index in range(len(self.Guessing_Word)):
            label = Label(self.canvas_word, text="?", bg="lightgray")
            self.textlables.append(label)
            label.grid(row=0, column=index, padx=1)

    # update score label
    def update_score(self):
        self.score_label.config(text=("SCORE: " +
                                                str(self.number_played_word)+"/"+str(self.total_words)))
    # show answer
    def show_answer(self):
        self.ans.config(text=self.Random_Word)

    # remove previous answer in new game
    def no_show_answer(self):
        self.ans.config(text="")

    # button updates
    def get_user_input(self, character):
        button = self.letter_buttons[ord(character) - 65]
        button['state'] = 'disable'
        if self.failed_count < self.guessing_chance and not self.win:
            user_input = character
            self.bingo_index = Functions.get_index(user_input, self.Guessing_Word_Copy)
            if len(self.bingo_index) != 0:
                self.letter_update(character, self.bingo_index)
            if len(self.bingo_index) == 0:
                self.failed_count += 1
                self.change_image()

            if len(self.Guessing_Word_Copy) == 0 and self.failed_count < self.guessing_chance:
                self.win = True

            if self.win:
                self.change_image()
                # print("You win! The word is: " + self.Random_Word)
                self.WordDictionary.remove(self.Random_Word)
                # print(self.WordDictionary)
                self.number_played_word += 1
                self.update_score()

                if self.number_played_word == self.total_words:
                    # Game cleared, no more words, exit the program
                    # print("Congratulation! You Guessed all the words! ")
                    self.image_changing_by_index(9)
                    self.disable_next_word()
                    # exit(0)
                self.button_disable()
                # print(self.number_played_word)
        if self.failed_count >= self.guessing_chance:
            # print("You lose!... The word is: " + self.Random_Word)
            self.show_answer()
            self.button_disable()

        # print(self.failed_count)
        # print(self.Guessing_Word_Copy)


    # initial the game
    def game_prep(self):

        self.Random_Word = self.WordDictionary[random.randint(0, (len(self.WordDictionary) - 1))]
        self.Guessing_Word = list(self.Random_Word)
        self.Guessing_Word_Copy = Functions.add_index_to_list(self.Guessing_Word)

        self.new_labels()
        self.failed_count = 0
        self.guessing_chance = 7
        self.win = False
        self.change_image()
        self.button_normal()
        self.no_show_answer()
        # print(self.Random_Word)
        # print(self.Guessing_Word_Copy)

    # Save progress by writing current WordDictionary into a txt file called Resume.txt
    def save_progress(self):
        with open("Resume.txt", "w") as outfile:
            outfile.write(str(self.number_played_word) + ";")
            for count, word in enumerate(self.WordDictionary, start=1):
                if len(self.WordDictionary) != count:
                    word = word + ";"
                outfile.write(word)
        outfile.close()

