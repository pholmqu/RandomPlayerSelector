from tkinter import simpledialog, filedialog


class Player:
    def __str__(self):
        return self.name + "\t" + str(self.number)

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def set_number(self, number):
        self.number = number


def add_player():
    name = simpledialog.askstring(
        title='Player Name',
        prompt='What is the name of the player that you want to add?')

    while name == '':
        name = simpledialog.askstring(
            title='Player Name',
            prompt='What is the name of the player that you want to add?')

    return name


def save_players(players):
    filename = filedialog.asksaveasfilename(initialdir='.', title='Save As',
    filetypes=[("Text Files", "*.txt")])
    with open(filename, 'w') as f:
        for player in players:
            f.write(str(player) + '\n')


def load_players():
    tmp = []

    filename = filedialog.askopenfilename(initialdir='.', title='Select File',
    filetypes=[("Text Files", "*.txt")])

    with open(filename, 'r') as f:
        read_file = f.read()
        lines = read_file.split('\n')
        for line in lines:
            if line != '':
                p_attrs = line.split('\t')
                tmp.append(Player(p_attrs[0], p_attrs[1]))

    return tmp
