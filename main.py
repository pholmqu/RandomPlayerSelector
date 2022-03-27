import window
import players


def main():

    app = window.Window(players.Players())

    app.canvas.pack()

    app.btnRoll.pack()

    app.root.mainloop()


main()
