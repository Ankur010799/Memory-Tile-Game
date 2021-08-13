from tkinter import *
from tkinter import messagebox
from random import shuffle
from game import MemoryGame
from tile import Tile


def get_tiles(current_game, frame, contents):
    tile_contents = contents * 2
    shuffle(tile_contents)

    _tiles = []
    index = 0

    for row in range(4):
        current_row = []
        for column in range(4):
            color = tile_contents[index]
            index = index + 1
            current_tile = Tile(frame, color, lambda x=row, y=column: current_game.select(x, y), row, column)
            current_row.append(current_tile)
        _tiles.append(current_row)

    return _tiles


root = Tk()
root.configure(bg="#9ba4b4")
root.title("The Memory Game")

def help():
    st = """Welcome to Memory Tiles Game
    • Instructions
    > Two one after other same color tiles remain same and will be disabled.
    >Two one after other different color tiles remain same as previous and
    will be enabled to click."""
    messagebox.showinfo("help",st)

Help = Button(root,text = "help",bg = "#ffffff",command = help)
Help.grid(sticky = NE)


tiles_frame = Frame(root)  # set frame for buttons
tiles_frame.grid(padx=20, pady=20)
close = Button(root, text="close", height=1, width=3, padx=10, pady=10, command=root.destroy)
close.grid()


color_list = ["#cd5d7d", "#654062", "#fa9579", "#ff8585",
              "#98acf8", "#59886b", "#5dcd7e", "#626540"]

game = MemoryGame(4, lambda: messagebox.showinfo(title='Success!', message='You won!'))
tiles = get_tiles(game, tiles_frame, color_list)
game.add_tiles(tiles)
# closing the root window
root.mainloop()
