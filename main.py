import customtkinter as csTK
from cell_class import cell
from values import CELL_HEIGHT, CELL_WIDTH, COLUMN_COUNT, DEFAULT_ROW_COUNT, current_id

root = csTK.CTk()
root.state('zoomed')
root.title('MONEY TRACKING')

csTK.set_appearance_mode('dark') #make posibble to change to light mode

side_frame = csTK.CTkFrame(root, width=350, height=700, border_width=2, border_color='aquamarine2')
side_frame.place(x = 125, y = 50)

main_frame = csTK.CTkFrame(root, width=900, height=600, border_width=2, border_color='aquamarine2')
main_frame.place(x = 500, y = 150)

top_frame = csTK.CTkFrame(root, width=900, height=75, border_width=2, border_color='aquamarine2')
top_frame.place(x = 500, y = 50)

my_x = 50
my_y = 50

# create frmaes for extra stuff


mycell = cell(20,50, main_frame)
mycell.generate_new_line(current_id)
mycell.id_obj.place(x = mycell.x, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
mycell.description_obj.place(x = mycell.x + 200, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
mycell.amount_obj.place(x = mycell.x + 400, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
mycell.time_obj.place(x = mycell.x + 600, y = mycell.y,width = CELL_WIDTH, height = CELL_HEIGHT)


save_button = cell.save_button(side_frame)
save_button.place(x = 200, y = 50, width=100, height=50)


root.mainloop()