
def extract_data_from_table(self) :
    pass # use this to make data readible by csv and send it to save_data as paramater to be saved to file



def save_data(data) : # function does not work properly--> overwriting existing data in csv
    with open('data.csv', 'w', newline='') as file :
        writer= csv.writer(file)
        writer.writerow([self.id, self.description, self.amount, self.time]) # use pandas learn it