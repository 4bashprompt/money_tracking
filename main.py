from tkinter import *
from classes import cell
from values import CELL_HEIGHT, CELL_WIDTH

root = Tk()
root.state('zoomed')
root.title('MONEY TRACKING')


mycell = cell(20, 50)

cell.create_cell(mycell, root)
mycell.cell_object.place(x = mycell.x, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)


root.mainloop()