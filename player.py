from tkinter import simpledialog, filedialog
class Player:
    def __str__(self):
        return self.name + "\t" + str(self.number)

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def set_number(self, number):
        self.number = number

