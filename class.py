import time

current = time.localtime()

class action :

    def __init__(self, description, amount, time = time.strftime('%d/%m/%Y', current)) :
        self.description = description
        self.amount = amount
        self.time = time
    def __repr__(self) :
        return f'spent on {self.description} | amount {self.amount}€ | {self.time}'



