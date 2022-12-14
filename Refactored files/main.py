import tkinter as tk
# from tkinter import *
from cell import Cell
import settings
import utils


root = tk.Tk()
# Override the settings of the window
root.configure(bg=settings.COLOR)
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = tk.Frame(
    root, bg=settings.COLOR, width=settings.WIDTH, height=utils.height_percentage(25)
)
top_frame.place(x=0, y=0)

game_title = tk.Label(
    top_frame, bg=settings.COLOR, fg='white', text='Minesweeper Game', font=('', 48)
)

game_title.place(x=utils.width_percentage(25), y=0)

left_frame = tk.Frame(
    root, bg=settings.COLOR, width=utils.width_percentage(25), height=utils.height_percentage(75)
)
left_frame.place(x=0, y=utils.height_percentage(25))

center_frame = tk.Frame(
    root, bg=settings.COLOR, width=utils.width_percentage(75), height=utils.height_percentage(75)
)
center_frame.place(
    x=utils.width_percentage(25), y=utils.height_percentage(25),
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0, y=0
)

Cell.randomize_mines()


# Run the window
root.mainloop()
