import customtkinter
from cell_class import cell
from values import *

class side_frame(customtkinter.CTkFrame) :
    def __init__(self, master) :
        super().__init__(master)

        self.configure(width = 350, height = 700, border_width = 2, border_color = 'aquamarine2')

        self.save_button = customtkinter.CTkButton(self, text='save', font=('Arial',15), width=100, height=50, command = cell.save_data)
        self.save_button.grid(row = 0, column = 0, padx = (25, 100), pady = (600, 25), sticky = 'sw')




class top_frame(customtkinter.CTkFrame) :
    def __init__(self, master) :
        super().__init__(master)

        self.configure(width=900, height=75, border_width=2, border_color='aquamarine2')

        self.no_label = customtkinter.CTkLabel(self, text='No', width = CELL_WIDTH, height = CELL_HEIGHT, font=('Arial',15,'bold'))
        self.no_label.grid(row = 0, column = 0, padx = (10, 15), pady = (12, 12.5))

        self.description_label = customtkinter.CTkLabel(self, text='Description', width = CELL_WIDTH, height = CELL_HEIGHT, font=('Arial',15,'bold'))
        self.description_label.grid(row = 0, column = 1, padx = (10, 15), pady = (12, 12.5))

        self.amount_label = customtkinter.CTkLabel(self, text='Amount', width = CELL_WIDTH, height = CELL_HEIGHT, font=('Arial',15,'bold'))
        self.amount_label.grid(row = 0, column = 2, padx = (10, 15), pady = (12, 12.5))    

        self.date_label = customtkinter.CTkLabel(self, text='Date', width = CELL_WIDTH, height = CELL_HEIGHT, font=('Arial',15,'bold'))
        self.date_label.grid(row = 0, column = 3, padx = (10, 15), pady = (12, 12.5))





class scrollable_main_frame(customtkinter.CTkScrollableFrame) :
    def __init__(self, master, column, row) :
        super().__init__(master)

        self.configure(width=900, height=600, border_width=2, border_color='aquamarine2')
        
        #self.my_button = customtkinter.CTkButton(self, text='hi')
        #self.my_button.place(x = 50, y = 50)

        for _ in range(cell.saved_data_amount()) :
            self.mycell = cell(column, row, self)

            self.mycell.display_saved_data()


            self.mycell.id_obj.grid(row = self.mycell.row, column = self.mycell.column, padx = (10, 15), pady = (25, 25))
            self.mycell.description_obj.grid(row = self.mycell.row, column = self.mycell.column + 1, padx = (10, 15), pady = (25, 25))
            self.mycell.amount_obj.grid(row = self.mycell.row, column = self.mycell.column + 2, padx = (10, 15), pady = (25, 25))
            self.mycell.time_obj.grid(row = self.mycell.row, column = self.mycell.column + 3, padx = (10, 15), pady = (25, 25))

            row += 1

        for _ in range(10) :
            self.mycell = cell(column, row, self)

            self.mycell.generate_new_line()


            self.mycell.id_obj.grid(row = self.mycell.row, column = self.mycell.column, padx = (10, 15), pady = (25, 25))
            self.mycell.description_obj.grid(row = self.mycell.row, column = self.mycell.column + 1, padx = (10, 15), pady = (25, 25))
            self.mycell.amount_obj.grid(row = self.mycell.row, column = self.mycell.column + 2, padx = (10, 15), pady = (25, 25))
            self.mycell.time_obj.grid(row = self.mycell.row, column = self.mycell.column + 3, padx = (10, 15), pady = (25, 25))

            row += 1
        






class App(customtkinter.CTk) :
    def __init__(self) :
        super().__init__()

        self.title('MONEY TRACKING')
        self.geometry('1300x750')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        customtkinter.set_appearance_mode('dark') #make posibble to change to light mode


        self.side_frame = side_frame(self)
        self.side_frame.grid(row = 0, column = 0, rowspan = 2, padx = (100, 25), pady = (50,50), sticky = 'n'+'s'+'e'+'w')

        self.scrollable_main_frame = scrollable_main_frame(self, CELL_COL, CELL_ROW)
        self.scrollable_main_frame.grid(row = 1, column = 1, padx = (0, 100), pady = (25, 50), sticky = 'nw')

        self.top_frame = top_frame(self)
        self.top_frame.grid(row = 0, column = 1, padx = (0, 100), pady = (50, 0), sticky = 'nw')









app = App()

app.mainloop()