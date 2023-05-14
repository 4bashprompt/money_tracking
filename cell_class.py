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

        self.id = id
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

        self.time = time
        self.time_obj = label

    

    def generate_new_line(self, id) :
        self.__create_id_label(id)
        self.__create_description_enrty()
        self.__create_amount_enrty()
        self.__create_time_enrty()

    @staticmethod
    def create_label(location, text) :
        return csTK.CTkLabel(location, text=text, font=('Arial',15,'bold'))


    @staticmethod
    def __read_table() :
        pass


    @classmethod
    def __save_data(cls) :
        with open('data.csv', 'w', newline='') as file :
            writer= csv.writer(file)

            writer.writerow(['id', 'description', 'amount', 'time'])

            for line in cell.all_lines :
                line_description = line.description_obj.get()
                line_amount = line.amount_obj.get()
                writer.writerow([line.id, line_description, line_amount, line.time])


    @staticmethod
    def save_button(location) :
        
        btn = csTK.CTkButton(location, text='save', command = cell.__save_data)
        return btn










