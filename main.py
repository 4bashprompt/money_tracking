import customtkinter as csTK
from cell_class import cell
from values import CELL_HEIGHT, CELL_WIDTH, COLUMN_COUNT, DEFAULT_ROW_COUNT, current_id, displayed_old_line_id

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
my_y = 20

cell.create_label(top_frame, 'No').place(x = my_x, y = my_y, width = CELL_WIDTH, height = CELL_HEIGHT)
cell.create_label(top_frame, 'Description').place(x = my_x + 200, y = my_y, width = CELL_WIDTH, height = CELL_HEIGHT)
cell.create_label(top_frame, 'Amount').place(x = my_x + 400, y = my_y, width = CELL_WIDTH, height = CELL_HEIGHT)
cell.create_label(top_frame, 'Date').place(x = my_x + 600, y = my_y, width = CELL_WIDTH, height = CELL_HEIGHT)


for _ in range(3) :
    mycell = cell(my_x,my_y, main_frame)
    mycell.display_saved_data(displayed_old_line_id)
    mycell.id_obj.place(x = mycell.x, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
    mycell.description_obj.place(x = mycell.x + 200, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
    mycell.amount_obj.place(x = mycell.x + 400, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
    mycell.time_obj.place(x = mycell.x + 600, y = mycell.y,width = CELL_WIDTH, height = CELL_HEIGHT)
    my_y += 75
    current_id += 1
    displayed_old_line_id += 1 # make this part more dynamical

for _ in range(3) :
    mycell = cell(my_x,my_y, main_frame)
    mycell.generate_new_line(current_id)
    mycell.id_obj.place(x = mycell.x, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
    mycell.description_obj.place(x = mycell.x + 200, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
    mycell.amount_obj.place(x = mycell.x + 400, y = mycell.y, width = CELL_WIDTH, height = CELL_HEIGHT)
    mycell.time_obj.place(x = mycell.x + 600, y = mycell.y,width = CELL_WIDTH, height = CELL_HEIGHT)
    my_y += 75
    current_id += 1


save_button = cell.save_button(side_frame)
save_button.place(x = 200, y = 50, width=100, height=50)


root.mainloop()