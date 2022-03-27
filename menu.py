from cProfile import label
from tkinter import Menu, messagebox


class MyMenu:

    def __init__(self, root):

        # Create Menu
        self.menubar = Menu(root)
        root.config(menu=self.menubar)

        # Create File Menu
        self.file_menu = Menu(self.menubar)

        # Add Exit Button to File Menu
        self.file_menu.add_command(
            label='Exit',
            command=lambda: close_application(root)
        )

        # Add File Menu to menubar
        self.menubar.add_cascade(
            label='File',
            menu=self.file_menu,
            underline=0
        )

        # Create Player Menu
        self.player_menu = Menu(self.menubar)

        # Add Player Menu to menubar
        self.menubar.add_cascade(
            label='Player',
            menu=self.player_menu,
            underline=0
        )

        # Create Edit Menu
        self.edit_menu = Menu(self.menubar)

        # Add Edit Menu to menubar
        self.menubar.add_cascade(
            label='Edit',
            menu=self.edit_menu,
            underline=0
        )


def close_application(root):
    if messagebox.askyesno(title='Close Application?',
                           message='Do you want to close application?'):
        root.destroy()
