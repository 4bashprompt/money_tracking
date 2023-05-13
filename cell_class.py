import csv
import customtkinter as csTK
from datetime import date




class cell :
    today = date.today()
    all_lines = []

    def __init__(self, x, y, location) :
        self.x = x
        self.y = y
        self.location = location

        cell.all_lines.append(self) # maybe


    def __create_id_label(self, id) :
        label = csTK.CTkLabel(self.location, text=id)

        self.id_obj = label
    
    def __create_description_enrty(self) :
        entry = csTK.CTkEntry(self.location, font=('Arial',12,'bold'))

        self.description_obj = entry

    def __create_amount_enrty(self) :
        entry = csTK.CTkEntry(self.location, font=('Arial',12,'bold'))

        self.amount_obj = entry

    def __create_time_enrty(self) :
        time = cell.today.strftime("%d/%m/%Y")

        label = csTK.CTkLabel(self.location, text=time)

        self.time_obj = label

    

    def generate_new_line(self, id) :
        self.__create_id_label(id)
        self.__create_description_enrty()
        self.__create_amount_enrty()
        self.__create_time_enrty()




    @staticmethod
    def __extract_data_from_table() :
        pass # use this to make data readible by csv and send it to save_data as paramater to be saved to file


    @staticmethod
    def __save_data(data) : # function does not work properly--> overwriting existing data in csv
        with open('data.csv', 'w', newline='') as file :
            writer= csv.writer(file)
            writer.writerow([self.id, self.description, self.amount, self.time]) # use pandas learn it

    @staticmethod
    def save_button(location) :
        #data_to_save = cell.__extract_data_from_table() 

        btn = csTK.CTkButton(location, text='save') # command = cell.__save_data(data_to_save)
        return btn










