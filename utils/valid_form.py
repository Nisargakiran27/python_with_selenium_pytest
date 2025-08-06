import csv

def read_from_valid_form_data(filepath):
    with open(filepath,'r',newline='') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]