from hr.position import load_positions
from hr.title import load_titles
from hr.status import load_status
from hr.leave_status import load_leave
from hr.product_line import load_product_lines
from hr.feature import load_features
from hr.input_validation import get_option_input
from hr.employee_manager import employee_manager as em
from hr.input_validation import get_modify_input, get_delete_input, \
    get_record_input, get_record_score
from hr_functions.find_qa_feature import find_qa_feature
from hr_functions.search_qa import search_emp
from hr_functions.list_qa_support import list_feature_team
from hr_functions.display_qa import display_info
from hr_functions.show_qa import show_emp
import config_variables as cv


def main():
    #TODO: write the function to run the different options. Handle the case for various user_roles.
    login_menu()
    option = get_option_input()
    while True:
        if option == 1:
            pass
        elif option == 2:
            print("The program will quit now.")
            return False

def login_menu():
    print("\n-----------------------------------------------------------")
    print("Please Login. Enter username and password. \nPress 0 to exit.")
    print("-----------------------------------------------------------\n")


def menu():
    #TODO: Add more options here
    print("\n-----------------------------------------------------------")
    print("Please kindly choose which option by typing the number.")
    print("1. Show all team members")
    print("2. Exit")
    print("-----------------------------------------------------------\n")


if __name__ == "__main__":
    main()
