import csv
from utils.read_csv import read_login_data, filter_data_by_type


def load_login_data():
    data = read_login_data("test_data\\login_data.csv")
    return {
        "valid": filter_data_by_type(data,"success"),
        "invalid" :filter_data_by_type(data,"failure"),
        "empty_username" :filter_data_by_type(data,"empty_username"),
        "empty_password":filter_data_by_type(data,"empty_password")
    }

