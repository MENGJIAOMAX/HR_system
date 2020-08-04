import json
import os
ROOT_DIR = os.path.abspath(os.curdir)


class approve_leaves:
    def __init__(self, name):
        self.name = name

    def view_pending_list(self):
        with open(
                '../Database/leave.json') as f:
            Leave = json.load(f)
        for key in Leave:
            if Leave[key][2]=="pending" or Leave[key][2]=="none":
                print(key)
                print('applied leave: ' + Leave[key][0] + ' to ' + Leave[key][1])
                print('leave status: ' + Leave[key][2])

    def change_status(self):
        with open(
                '../Database/leave.json') as f:
            Leave = json.load(f)
        for key in Leave:
            if Leave[key][2]=="pending" or Leave[key][2]=="none":
                print(key)
                print('applied leave: ' + Leave[key][0] + ' to ' + Leave[key][1])
                print('leave status: ' + Leave[key][2])
        pending_emolyee_name=str(raw_input("employee name:"))
        print("\n-----------------------------------------------------------")
        print("Please kindly choose which status by typing the number.")
        print("1. Approve")
        print("2. Reject")
        print("-----------------------------------------------------------\n")
        decision=int(raw_input("Your decision:"))
        if decision==1:
            Leave[pending_emolyee_name][2] = "Approved"
            with open(
                    '../Database/leave.json',
                    'w') as outfile:
                json.dump(Leave, outfile)
                outfile.close()
            print(pending_emolyee_name)
            print('applied leave: ' + Leave[pending_emolyee_name][0] + ' to ' + Leave[pending_emolyee_name][1])
            print('leave status: ' + Leave[pending_emolyee_name][2])

        elif decision==2:
            Leave[pending_emolyee_name][2] = "Rejected"
            with open(
                    '../Database/leave.json',
                    'w') as outfile:
                json.dump(Leave, outfile)
                outfile.close()
            print(pending_emolyee_name)
            print('applied leave: ' + Leave[pending_emolyee_name][0] + ' to ' + Leave[pending_emolyee_name][1])
            print('leave status: ' + Leave[pending_emolyee_name][2])

        else:
            print("Please type 1 or 2")





