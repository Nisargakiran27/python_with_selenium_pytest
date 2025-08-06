import csv

def datepicker(filepath):
    with open (filepath, mode= 'r') as file:
        reader = csv.DictReader(file)
        return[( row["month"], row["day"],row["year"]) for row in reader]