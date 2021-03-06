from genericpath import exists
from random import randrange, shuffle
from tkinter.font import NORMAL
from turtle import title
import player
from tkinter import DISABLED, simpledialog, filedialog, Label

class Players:

    def __init__(self):
        self.ListOfPlayers = []
        self.count = len(self.ListOfPlayers)

    def add_player(self, app):
        name = simpledialog.askstring(
            title='Player Name',
            prompt='What is the name of the player that you want to add?'
        )

        while name == '':
            name = simpledialog.askstring(
                title='Player Name',
                prompt='What is the name of the player that you want to add?'
            )
        
        self.ListOfPlayers.append(player.Player(name))

        self.update_list(app)

    def save_players(self):
        filename = filedialog.asksaveasfilename(
            initialdir='./saves',
            title='Save As',
            filetypes=[
                ("Text Files", "*.txt")
            ]
        )

        if exists(filename):
            with open(filename, 'w') as f:
                for player in self.ListOfPlayers:
                    f.write(str(player) + '\n')

    def load_players(self, app):

        filename = filedialog.askopenfilename(
            initialdir='./saves',
            title='Select File',
            filetypes=[
                ("Text Files", "*.txt")
            ]
        )

        if exists(filename):
            self.ListOfPlayers.clear()
            with open(filename, 'r') as f:
                read_file = f.read()
                lines = read_file.split('\n')
                for line in lines:
                    if line != '':
                        player_attrs = line.split('\t')
                        self.ListOfPlayers.append(
                            player.Player(
                                player_attrs[0]
                            )
                        )

            self.update_list(app)

    def __str__(self):
        output = ""
        
        for p in self.ListOfPlayers:
            output += str(p) + '\n'

        return output

    def pop(self, app):
        self.ListOfPlayers.pop()
        self.update_list(app)

    def shuffle_players(self, app):
        shuffle(self.ListOfPlayers)
        self.update_list(app)

    def clear_players(self, app):
        self.ListOfPlayers.clear()
        self.update_list(app)

    def update_list(self, app):
        for widget in app.frame.winfo_children():
            widget.destroy()

        if len(self.ListOfPlayers) == 0:
            h = 50
        else:
            h = len(self.ListOfPlayers) * 25

        app.canvas.config(
            height=h
        )

        for p in self.ListOfPlayers:
            label = Label(
                app.frame,
                text=str(p),
                bg=app.cur_frame
            )
            label.pack()

        if len(self.ListOfPlayers) > 0:
            app.btnRoll.config(
                state=NORMAL
            )
        else:
            app.btnRoll.config(
                state=DISABLED
            )
