import time, csv
import customtkinter as csTK

current = time.localtime()


class cell :
    cell_ids = 0 # create a func to find last id at datatable and use instead of this to find new id

    def __init__(self, x, y, id = cell_ids + 1, description = '', amount = 0, time = time.strftime('%d/%m/%Y', current)) :
        self.x = x
        self.y = y
        self.description = description
        self.amount = amount
        self.time = time
        self.id = id

        cell.cell_ids += 1



    def create_cell(self, location) :
        entry = csTK.CTkEntry(location, font=('Arial',15,'bold'))

        self.cell_object = entry


    @staticmethod
    def save_button(location) :
        #data_to_save = action.extract_data_from_table(self) 

        btn = csTK.CTkButton(location, text='save') # command = action.save_data(data_to_save)
        return btn