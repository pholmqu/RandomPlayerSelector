from genericpath import exists
from os import stat
from random import randrange
import tkinter as tk
from tkinter import *
from tkinter import colorchooser
from turtle import st
import player

DEFAULT_CANVAS_COLOR = '#F56600'
DEFAULT_FRAME_COLOR = '#522D80'


def close_rps():
    if tk.messagebox.askyesno(title="Close Application?",
                              message="Do you want to close application?"):
        root.destroy()


def update_list(cur_frame):
    for widget in frame.winfo_children():
        widget.destroy()

    for p in players:
        label = tk.Label(frame, text=str(p), bg=cur_frame)
        label.pack()

    check_assigned(players)


def update_players(cur_frame):
    players.append(player.Player(player.add_player(), 0))
    update_list(cur_frame)


def assign_number(cur_frame):
    nums = []
    while len(nums) != len(players):
        num = randrange(start=1,
                        stop=len(players) + 1)

        while num in nums:
            num = randrange(start=1,
                            stop=len(players) + 1)
        nums.append(num)

    for player in players:
        player.set_number(nums[players.index(player)])
    update_list(cur_frame)


def roll(cur_frame):
    num = randrange(start=1,
                    stop=len(players) + 1)

    update_list(cur_frame)

    label = tk.Label(frame, text=num, bg=cur_frame)
    label.pack()

    pname = ""

    for player in players:
        if int(player.number) == int(num):
            pname = player.name

    label2 = tk.Label(frame,
                      font=("Comic Sans MS", 20, "bold"),
                      text=pname,
                      bg=cur_frame)
    label2.pack()


def menu_load_players(cur_frame):
    tmp = player.load_players()
    players.clear()
    for p in tmp:
        players.append(p)
    update_list(cur_frame)


def clear_players(cur_frame):
    players.clear()
    update_list(cur_frame)


def remove_last_player(cur_frame):
    players.pop()
    update_list(cur_frame)
    if players[0].number != 0:
        assign_number(cur_frame)


def set_color(location, cur_frame, cur_canvas):
    if location == "Canvas":
        cur_canvas = colorchooser.askcolor(title="Choose Canvas Color")[1]
        canvas.config(bg=cur_canvas)
    elif location == "Frame":
        cur_frame = colorchooser.askcolor(title="Choose Frame Color")[1]
        frame.config(bg=cur_frame)
        update_list(cur_frame)


def set_default_color():
    cur_frame = DEFAULT_FRAME_COLOR
    cur_canvas = DEFAULT_CANVAS_COLOR
    canvas.config(bg=cur_canvas)
    frame.config(bg=cur_frame)
    update_list(cur_frame)


def check_assigned(players):
    if len(players) == 0:
        btnRoll.config(state=DISABLED)
        return
    else:
        for player in players:
            if player.number == 0:
                btnRoll.config(state=DISABLED)
                return

    btnRoll.config(state=NORMAL)


def main():

    global root, frame, canvas, players, btnRoll

    cur_canvas = DEFAULT_CANVAS_COLOR
    cur_frame = DEFAULT_FRAME_COLOR

    # Create Root
    root = tk.Tk()
    root.title("Random Player Selector")
    root.iconphoto(
        False, tk.PhotoImage(
            file='/Users/patrickholmquist/Documents/PatrickPrograms/DnD/RandomPlayerSelector/images/dnd_icon.png'))

    # Create main window
    canvas = tk.Canvas(root,
                       height=700,
                       width=700,
                       bg=cur_canvas)  # Clemson Orange
    canvas.pack()

    # Create smaller window to create 'Frame look'
    frame = tk.Frame(root,
                     bg=cur_frame)  # Clemson Purple

    frame.place(relwidth=0.8,
                relheight=0.8,
                relx=0.1,
                rely=0.1)

    # Create Menu
    menubar = Menu(root)
    root.config(menu=menubar)

    # Create Color Menu
    # Canvas Color
    color_menu = Menu(menubar)
    color_menu.add_command(
        label='Canvas Color',
        command=lambda: set_color('Canvas', cur_frame, cur_canvas)
    )

    # Frame Color
    color_menu.add_command(
        label='Frame Color',
        command=lambda: set_color('Frame', cur_frame, cur_canvas)
    )

    # Return to Default Colors
    color_menu.add_command(
        label='Default Color',
        command=lambda: set_default_color()
    )

    # Create File Menu
    file_menu = Menu(menubar)

    # Create Player Menu
    player_menu = Menu(menubar)

    # Create Add Player Button
    player_menu.add_command(
        label='Add Player',
        command=lambda: update_players(cur_frame)
    )

    # Pop Last Player
    player_menu.add_command(
        label='Remove Last Player',
        command=lambda: remove_last_player(cur_frame)
    )

    # Assign Numbers
    player_menu.add_command(
        label='Assign Numbers',
        command=lambda: assign_number(cur_frame)
    )

    # Save Players
    file_menu.add_command(
        label='Save As',
        command=lambda: player.save_players(players)
    )

    # Load Players
    file_menu.add_command(
        label='Open',
        command=lambda: menu_load_players(cur_frame)
    )

    # Clear Players
    player_menu.add_command(
        label='Clear Players',
        command=lambda: clear_players(cur_frame)
    )

    # Create Exit Button
    file_menu.add_command(
        label='Exit',
        command=lambda: close_rps()
    )

    # Create Edit Menu
    edit_menu = Menu(menubar)
    edit_menu.add_cascade(
        label='Color',
        menu=color_menu,
        underline=0
    )

    # Add to Menu
    menubar.add_cascade(
        label='File',
        menu=file_menu,
        underline=0
    )

    menubar.add_cascade(
        label='Player',
        menu=player_menu,
        underline=0
    )

    menubar.add_cascade(
        label='Edit',
        menu=edit_menu,
        underline=0
    )

    # Add Roll Button
    btnRoll = tk.Button(root,
                        text="Roll",
                        state=DISABLED,
                        command=lambda: roll(cur_frame))
    btnRoll.pack()

    players = []

    root.mainloop()


main()
