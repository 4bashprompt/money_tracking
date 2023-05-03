import time, csv, tkinter

current = time.localtime()

class action :

    def __init__(self, id, description, amount, time = time.strftime('%d/%m/%Y', current)) :
        self.description = description
        self.amount = amount
        self.time = time
        self.id = id

    

    def __repr__(self) :
        return f'id = {self.id} spent on {self.description} | amount {self.amount}€ | {self.time}'


    def save_data(self) : # function does not work properly--> overwriting existing data in csv
        with open('data.csv', 'w', newline='') as file :
            writer= csv.writer(file)
            writer.writerow([self.id, self.description, self.amount, self.time]) # use pandas learn it




x = action(1, 'netto', 25.63)

action.save_data(x)



class cell :
    def __init__(self, x, y) :
        self.x = x
        self.y = y



    def create_cell(self, location) :
        entry = tkinter.Entry(location)

        self.cell_object = entry