from multiprocessing.dummy import current_process
from os import curdir
import tkinter as tk
from tkinter import colorchooser, Label
from turtle import title
import menu
from random import randrange

DEFAULT_CANVAS_COLOR = '#F56600'    # Clemson Orange
DEFAULT_FRAME_COLOR = '#522D80'     # Clemson Purple

ICON_PATH = '/Users/patrickholmquist/Documents/PatrickPrograms/DnD/RandomPlayerSelector/images/dnd_icon.png'


class Window:

    def roll(self):
        num = randrange(
            start=0,
            stop=len(self.players.ListOfPlayers)
        )

        # self.players.update_list(self)

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.canvas.config(
            height=(len(self.players.ListOfPlayers) * 30)
        )

        for p in self.players.ListOfPlayers:
            if num == self.players.ListOfPlayers.index(p):
                label2 = tk.Label(
                    self.frame,
                    font=("Comic Sans MS", 20, "bold"),
                    text=self.players.ListOfPlayers[num].name,
                    bg=self.cur_frame
                )
                label2.pack()
            else:
                label = Label(
                    self.frame,
                    text=str(p),
                    bg=self.cur_frame
                )
                label.pack()

    def set_color(self, location):
        if location == 'Canvas':
            self.cur_canvas = colorchooser.askcolor(
                title='Choose ' + location + ' Color'
            )[1]
            self.canvas.config(bg=self.cur_canvas)
        elif location == 'Frame':
            self.cur_frame = colorchooser.askcolor(
                title='Choose ' + location + ' Color'
            )[1]
            self.frame.config(bg=self.cur_frame)
            self.players.update_list(self)

    def set_default_color(self):
        self.cur_canvas = DEFAULT_CANVAS_COLOR
        self.cur_frame = DEFAULT_FRAME_COLOR
        self.canvas.config(bg=self.cur_canvas)
        self.frame.config(bg=self.cur_frame)
        self.players.update_list(self)

    def __str__(self):
        print("Additional Feature for Later")

    def __init__(self, players):

        self.cur_canvas = DEFAULT_CANVAS_COLOR
        self.cur_frame = DEFAULT_FRAME_COLOR
        self.players = players

        # Creating Root
        self.root = tk.Tk()
        self.root.title("Random Player Selector")
        self.root.iconphoto(
            False, tk.PhotoImage(
                file=ICON_PATH))

        # Creating Canvas
        self.canvas = tk.Canvas(self.root,
                                bg=self.cur_canvas)

        # Creating Frame
        self.frame = tk.Frame(self.root,
                              bg=self.cur_frame)

        self.frame.place(relwidth=0.8,
                         relheight=0.8,
                         relx=0.1,
                         rely=0.1)

        # Create Menu
        self.menubar = menu.MyMenu(self)

        # Create Roll Button
        self.btnRoll = tk.Button(
            self.root,
            text='Roll',
            state=tk.DISABLED,
            command=lambda: self.roll()
        )
