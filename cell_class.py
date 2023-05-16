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

        cell.all_lines.append(self) 


    def __create_id_label(self, id) :
        label = csTK.CTkLabel(self.location, text=id)

        self.id = id
        self.id_obj = label
    
    def __create_description_enrty(self, old_description = '') :
        entry = csTK.CTkEntry(self.location, font=('Arial',12,'bold'))

        if old_description :
            entry.insert(-1, old_description)

        self.description_obj = entry

    def __create_amount_enrty(self, old_amount = '') :
        entry = csTK.CTkEntry(self.location, font=('Arial',12,'bold'))

        if old_amount :
            entry.insert(-1, old_amount)

        self.amount_obj = entry



    def __create_time_label(self, old_time = '') :

        if not old_time:
            time = cell.today.strftime("%d/%m/%Y")
        else :
            time = old_time

        label = csTK.CTkLabel(self.location, text=time)

        self.time = time
        self.time_obj = label

    

    def generate_new_line(self, id) :
        self.__create_id_label(id)
        self.__create_description_enrty()
        self.__create_amount_enrty()
        self.__create_time_label()

    @staticmethod
    def create_label(location, text) :
        return csTK.CTkLabel(location, text=text, font=('Arial',15,'bold'))


    @staticmethod
    def read_table() :
        with open('data.csv', 'r', newline='') as file :
            reader = csv.DictReader(file)

            return list(reader)


    def display_saved_data(self, old_id) :
        reader = cell.read_table()

        row = reader[old_id - 1]

        self.__create_id_label(row['id'])
        self.__create_description_enrty(row['description'])
        self.__create_amount_enrty(row['amount'])
        self.__create_time_label(row['time'])




    @classmethod
    def __save_data(cls) :
        with open('data.csv', 'w', newline='') as file :
            field_names = ['id', 'description', 'amount', 'time']

            writer= csv.DictWriter(file, fieldnames = field_names)

            writer.writeheader()

            for line in cell.all_lines :
                line_description = line.description_obj.get()
                line_amount = line.amount_obj.get()

                writer.writerow({
                    'id' : line.id,
                    'description' : line_description,
                    'amount' : line_amount,
                    'time' : line.time
                })




    @staticmethod
    def save_button(location) :
        
        btn = csTK.CTkButton(location, text='save', command = cell.__save_data)
        return btn










