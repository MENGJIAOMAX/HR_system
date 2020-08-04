import json
import os

dir_name = os.path.dirname(__file__)
file_name = os.path.join(dir_name, '../Database/employee.json')

def load_employee_data():
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except ValueError:
        print("There is no data in the json file.")
    except IOError:
        print("The file do not exist or has a syntax error.")

