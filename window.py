import tkinter as tk
import menu
from random import randrange

DEFAULT_CANVAS_COLOR = '#F56600'    # Clemson Orange
DEFAULT_FRAME_COLOR = '#522D80'     # Clemson Purple

ICON_PATH = '/Users/patrickholmquist/Documents/PatrickPrograms/DnD/RandomPlayerSelector/images/dnd_icon.png'


class Window:

    def roll(self):
        num = randrange(
            start=1,
            stop=len(self.players.ListOfPlayers) + 1
        )

        self.players.update_list(self)

        label = tk.Label(
            self.frame,
            text=num,
            bg=self.cur_frame
        )
        label.pack()

        pname = ''
        for p in self.players.ListOfPlayers:
            if int(p.number) == int(num):
                pname = p.name
        
        label2 = tk.Label(
            self.frame,
            font=("Comic Sans MS", 20, "bold"),
            text=pname,
            bg=self.cur_frame
        )
        label2.pack()

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
                                height=700,
                                width=700,
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
