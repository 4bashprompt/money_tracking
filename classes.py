import time, csv, tkinter

current = time.localtime()

class action : #no need for action class. create a new file for methods of current action class, merge action and cell classes inder cell

    def __init__(self, id, description, amount, time = time.strftime('%d/%m/%Y', current)) :
        self.description = description
        self.amount = amount
        self.time = time
        self.id = id

    

    def __repr__(self) :
        return f'id = {self.id} spent on {self.description} | amount {self.amount}€ | {self.time}'



    def extract_data_from_table(self) :
        pass # use this to make data readible by csv and send it to save_data as paramater to be saved to file


    @staticmethod
    def save_data(data) : # function does not work properly--> overwriting existing data in csv
        with open('data.csv', 'w', newline='') as file :
            writer= csv.writer(file)
            writer.writerow([self.id, self.description, self.amount, self.time]) # use pandas learn it







class cell :
    def __init__(self, x, y) :
        self.x = x
        self.y = y



    def create_cell(self, location) :
        entry = tkinter.Entry(location, font=('Arial',15,'bold'))

        self.cell_object = entry


    @staticmethod
    def save_button(location) :
        #data_to_save = action.extract_data_from_table(self) 

        btn = tkinter.Button(location, text='save', command = action.save_data(data_to_save))
        return btn