import csv
import customtkinter as csTK
from datetime import date
from values import *
from CTkMessagebox import CTkMessagebox


class cell :
    today = date.today()
    all_lines = []

    def __init__(self, row, column, location) :
        self.row = row
        self.column = column
        self.location = location

        id = cell.get_current_id()

        self.id = id

        cell.all_lines.append(self)

    @staticmethod
    def get_current_id() :
        if cell.all_lines == [] :
            return 1
        else :
            return cell.all_lines[-1].id + 1


    def __create_id_label(self) :
        label = csTK.CTkLabel(self.location, text=self.id, width = CELL_WIDTH, height = CELL_HEIGHT, font = CELL_FONT)

        self.id_obj = label
    
    def __create_description_enrty(self, old_description = '') :
        entry = csTK.CTkEntry(self.location, width = CELL_WIDTH, height = CELL_HEIGHT, font=CELL_FONT)

        if old_description :
            entry.insert(-1, old_description)

        self.description_obj = entry

    def __create_amount_enrty(self, old_amount = '') :
        entry = csTK.CTkEntry(self.location, width = CELL_WIDTH, height = CELL_HEIGHT, font=CELL_FONT)

        if old_amount :
            entry.insert(-1, old_amount)

        self.amount_obj = entry



    def __create_time_label(self, old_time = '') :

        if not old_time:
            time = cell.today.strftime("%d/%m/%Y")
        else :
            time = old_time

        label = csTK.CTkLabel(self.location, text=time, width = CELL_WIDTH, height = CELL_HEIGHT, font = CELL_FONT)

        self.time = time 
        self.time_obj = label

    

    def generate_new_line(self) :
        self.__create_id_label()
        self.__create_description_enrty()
        self.__create_amount_enrty()
        self.__create_time_label()


    @staticmethod
    def read_table() :
        with open('data.csv', 'r', newline='') as file :
            reader = csv.DictReader(file)

            return list(reader)



    @staticmethod
    def saved_data_amount() :
        return len(cell.read_table())


    def display_saved_data(self) :
        reader = cell.read_table()

        if reader :
            row = reader[self.id - 1]

            self.__create_id_label()
            self.__create_description_enrty(row['description'])
            self.__create_amount_enrty(row['amount'])
            self.__create_time_label(row['time'])




    @classmethod
    def save_data(cls) :

        if cell.value_check() :

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
    def calcualte_total_money_amount() :

        reader = cell.read_table()
        sum = 0

        for row in reader :
            if row['amount'].strip() != '' :
                sum += float(row['amount'])

        return str(sum)


    @staticmethod
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False


    @classmethod
    def value_check(cls) :
        global check_control

        for line in cell.all_lines :

            amount = line.amount_obj.get()

            if amount != '' and not cell.is_float(amount) :
                CTkMessagebox(title="Error", message="Money amount must be digits", icon="cancel")
                return False

        else :
            return True

