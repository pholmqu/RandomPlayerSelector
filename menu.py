from cProfile import label
from tkinter import Menu, messagebox


class MyMenu:

    def __init__(self, app):

        # Create Menu
        self.menubar = Menu(app.root)
        app.root.config(menu=self.menubar)

        # Create File Menu
        self.file_menu = Menu(self.menubar)

        # Add Save Button
        self.file_menu.add_command(
            label='Save',
            command=lambda: app.players.save_players()
        )

        # Add Open Button
        self.file_menu.add_command(
            label='Open',
            command=lambda: app.players.load_players(app)
        )

        # Add Exit Button to File Menu
        self.file_menu.add_command(
            label='Exit',
            command=lambda: close_application(app.root)
        )

        # Add File Menu to menubar
        self.menubar.add_cascade(
            label='File',
            menu=self.file_menu,
            underline=0
        )

        # Create Player Menu
        self.player_menu = Menu(self.menubar)

        # Add 'Add Player' Button to Player Menu
        self.player_menu.add_command(
            label='Add Player',
            command=lambda: app.players.add_player(app)
        )

        # Add 'Assign Numbers' Button to Player Menu
        self.player_menu.add_command(
            label='Assign Numbers',
            command=lambda: app.players.assign_numbers(app)
        )

        # Add 'Remove Last Player' Button to Player Menu
        self.player_menu.add_command(
            label='Remove Last Player',
            command=lambda: app.players.pop(app)
        )

        # Add 'Clear Players' Button to Player Menu
        self.player_menu.add_command(
            label='Clear Players',
            command=lambda: app.players.clear_players(app)
        )

        # Add Player Menu to menubar
        self.menubar.add_cascade(
            label='Player',
            menu=self.player_menu,
            underline=0
        )

        # Create Edit Menu
        self.edit_menu = Menu(self.menubar)

        # Add 'Canvas Color' to Edit Menu
        self.edit_menu.add_command(
            label='Canvas Color',
            command=lambda: app.set_color('Canvas')
        )

        # Add 'Frame Color' to Edit Menu
        self.edit_menu.add_command(
            label='Frame Color',
            command=lambda: app.set_color('Frame')
        )

        # Add 'Reset to Default Colors' to Edit Menu
        self.edit_menu.add_command(
            label='Reset to Default Colors',
            command=lambda: app.set_default_color()
        )

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
