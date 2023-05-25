import customtkinter
from cell_class import cell
from values import *
from functools import partial


class side_frame(customtkinter.CTkFrame) :
    def __init__(self, master) :
        super().__init__(master)

        self.configure(width = 350, height = 700, border_width = 2, border_color = 'aquamarine2')

        self.save_button = customtkinter.CTkButton(self, text='Save', font=BUTTON_FONT, width=100, height=50, command = cell.save_data)
        self.save_button.grid(row = 2, column = 0, padx = (25, 100), pady = (400, 25), sticky = 'nw')

        self.sum_label = customtkinter.CTkLabel(self, text='Total money :', font=LABEL_FONT)
        self.sum_label.grid(row = 0, column = 0, padx = (25, 25), pady = (50, 25), sticky = 'nw')


        money_amount = customtkinter.StringVar(value=cell.calcualte_total_money_amount())

        self.sum = customtkinter.CTkLabel(self, textvariable=money_amount, font=LABEL_FONT)

        self.sum.bind('<Key>', lambda event : money_amount.set(cell.calcualte_total_money_amount()))
        self.sum.grid(row = 1, column = 0, padx = (25, 25), pady = (0, 25), sticky = 'sw')



class top_frame(customtkinter.CTkFrame) :
    def __init__(self, master) :
        super().__init__(master)

        self.configure(width=950, height=75, border_width=2, border_color='aquamarine2')

        self.no_label = customtkinter.CTkLabel(self, text='No', width = CELL_WIDTH, height = CELL_HEIGHT, font=LABEL_FONT)
        self.no_label.grid(row = 0, column = 0, padx = (10, 15), pady = (12, 12.5), sticky = 'n')

        self.description_label = customtkinter.CTkLabel(self, text='Description', width = CELL_WIDTH, height = CELL_HEIGHT, font=LABEL_FONT)
        self.description_label.grid(row = 0, column = 1, padx = (10, 15), pady = (12, 12.5), sticky = 'n')

        self.amount_label = customtkinter.CTkLabel(self, text='Amount', width = CELL_WIDTH, height = CELL_HEIGHT, font=LABEL_FONT)
        self.amount_label.grid(row = 0, column = 2, padx = (10, 15), pady = (12, 12.5), sticky = 'n')    

        self.date_label = customtkinter.CTkLabel(self, text='Date', width = CELL_WIDTH, height = CELL_HEIGHT, font=LABEL_FONT)
        self.date_label.grid(row = 0, column = 3, padx = (10, 15), pady = (12, 12.5), sticky = 'ne')





class scrollable_main_frame(customtkinter.CTkScrollableFrame) :
    CELL_ROW = 0
    CELL_COL = 0

    def __init__(self, master) :
        super().__init__(master)

        self.configure(width=900, height=600, border_width=2, border_color='aquamarine2')
        

        for _ in range(cell.saved_data_amount()) :
            self.mycell = cell(scrollable_main_frame.CELL_ROW, scrollable_main_frame.CELL_COL, self)

            self.mycell.display_saved_data()


            self.mycell.id_obj.grid(row = self.mycell.row, column = self.mycell.column, padx = (10, 15), pady = (25, 25))
            self.mycell.description_obj.grid(row = self.mycell.row, column = self.mycell.column + 1, padx = (10, 15), pady = (25, 25))
            self.mycell.amount_obj.grid(row = self.mycell.row, column = self.mycell.column + 2, padx = (10, 15), pady = (25, 25))
            self.mycell.time_obj.grid(row = self.mycell.row, column = self.mycell.column + 3, padx = (10, 15), pady = (25, 25))

            scrollable_main_frame.CELL_ROW += 1

        self.new_line_button = customtkinter.CTkButton(self, text='New Line', command=partial(scrollable_main_frame.new_line, self))
        self.new_line_button.grid(row = scrollable_main_frame.CELL_ROW, column = scrollable_main_frame.CELL_COL, padx = (40, 15), pady = (25, 25), sticky = 'sw')



    
    def new_line(self) :
            self.mycell = cell(scrollable_main_frame.CELL_ROW, scrollable_main_frame.CELL_COL, self)

            scrollable_main_frame.CELL_ROW += 1

            self.mycell.generate_new_line()


            self.mycell.id_obj.grid(row = self.mycell.row, column = self.mycell.column, padx = (10, 15), pady = (25, 25))
            self.mycell.description_obj.grid(row = self.mycell.row, column = self.mycell.column + 1, padx = (10, 15), pady = (25, 25))
            self.mycell.amount_obj.grid(row = self.mycell.row, column = self.mycell.column + 2, padx = (10, 15), pady = (25, 25))
            self.mycell.time_obj.grid(row = self.mycell.row, column = self.mycell.column + 3, padx = (10, 15), pady = (25, 25))

            self.new_line_button.grid(row = scrollable_main_frame.CELL_ROW, column = scrollable_main_frame.CELL_COL, padx = (40, 15), pady = (25, 25), sticky = 'sw')


        






class App(customtkinter.CTk) :
    def __init__(self) :
        super().__init__()

        self.title('MONEY TRACKING')
        self.geometry('1400x750')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        customtkinter.set_appearance_mode('dark') #make posibble to change to light mode


    def run(self) :

        self.side_frame = side_frame(self)
        self.side_frame.grid(row = 0, column = 0, rowspan = 2, padx = (100, 25), pady = (50,50), sticky = 'n'+'s'+'e'+'w')

        self.scrollable_main_frame = scrollable_main_frame(self)
        self.scrollable_main_frame.grid(row = 1, column = 1, padx = (0, 100), pady = (25, 50), sticky = 'nw')

        self.top_frame = top_frame(self)
        self.top_frame.grid(row = 0, column = 1, padx = (0, 100), pady = (50, 0), sticky = 'n'+'s'+'e'+'w')






if __name__ == '__main__' :
    app = App()

    app.run()

    app.mainloop()