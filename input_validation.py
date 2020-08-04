import re

#TODO: Add more validations in this file

def get_user_name():
    while True:
        name = input("\nName: ")
        regex = '^[a-zA-Z](?!.*\s{2}).*[a-zA-Z]$'
        if name and name.strip():
            if re.search(regex, name):
                return name
            else:
                print("That is not a valid name. Please do not start/ end"
                      " with white-spaces or have more than 1 consecutive "
                      "white-spaces in between.")
        else:
            print("Please do not leave blank.")

