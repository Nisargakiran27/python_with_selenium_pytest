import csv 

def read_form_login_data(filepath):
    with open (filepath,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]
