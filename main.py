import customtkinter as csTK
from cell_class import cell
from values import CELL_HEIGHT, CELL_WIDTH, COLUMN_COUNT, DEFAULT_ROW_COUNT, current_id

root = csTK.CTk()
root.state('zoomed')
root.title('MONEY TRACKING')

csTK.set_appearance_mode('dark') #make posibble to change to light mode

my_x = 20
my_y = 50

# create frmaes for extra stuff


mycell = cell(20,50, root)
mycell.generate_line(current_id)
mycell.id_obj.place(x = mycell.x + 200, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
mycell.description_obj.place(x = mycell.x + 400, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
mycell.amount_obj.place(x = mycell.x + 600, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
mycell.time_obj.place(x = mycell.x + 800, y = mycell.y,width = CELL_WIDTH, height = CELL_HEIGHT)


save_button = cell.save_button(root)
save_button.place(x = 400, y = 600, width=50, height=25)

root.mainloop()