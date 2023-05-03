from tkinter import *
from classes import cell
from values import CELL_HEIGHT, CELL_WIDTH, COLUMN_COUNT, DEFAULT_ROW_COUNT

root = Tk()
root.state('zoomed')
root.title('MONEY TRACKING')

my_x = 20
my_y = 50


for _ in range(DEFAULT_ROW_COUNT) : # add new line button to add extra rows
    for _ in range(COLUMN_COUNT) :
        mycell = cell(my_x, my_y)

        cell.create_cell(mycell, root)
        mycell.cell_object.place(x = mycell.x, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
        my_x += CELL_WIDTH
    my_y += CELL_HEIGHT
    my_x = 20



save_button = cell.save_button(root)
save_button.place(x = 400, y = 600, width=50, height=25)

root.mainloop()