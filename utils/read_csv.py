import csv

def read_login_data(filepath):
    with open(filepath, newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def filter_data_by_type(data, expected_value):
    return [
        (row["username"], row["password"], row["expected"])
        for row in data if row["expected"] == expected_value
    ]

# def get_test_ids(data, outcome):
#     return [f"{outcome}_{row['username'] or 'emptyuser'}_{row['password'] or 'emptypass'}" 
#             for row in data if row["expected"] == outcome]
