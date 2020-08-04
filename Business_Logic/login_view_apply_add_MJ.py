
import json
import datetime
from Manual_approve_leaves_MJ import approve_leaves
from approve_rules_MJ import system_approve_rules
import os
ROOT_DIR = os.path.abspath(os.curdir)




with open('../Database/employee.json') as people:
    all = json.load(people)


#print(json.dumps(all, indent = 4, sort_keys=True))

with open('../Database/leave.json') as f:
    Leave = json.load(f)

#Leave=[leave start time, leave end time, leave application status]
#print(json.dumps(Leave, indent = 4, sort_keys=True))



class list_options:
    def __init__(self, role, name):
        self.role = role
        self.name = name

    def Employee_list(self):
        print("\n-----------------------------------------------------------")
        print("Please kindly choose which option by typing the number.")
        print("1. View self")
        print("2. Apply leaves")
        print("-----------------------------------------------------------\n")


    def Manager_list(self):
        print("\n-----------------------------------------------------------")
        print("Please kindly choose which option by typing the number.")
        print("1. View self")
        print("2. Apply leaves")
        print("3. View employee pending list")
        print("4. Approve leaves")
        print("-----------------------------------------------------------\n")

    def Admin_list(self):
        print("\n-----------------------------------------------------------")
        print("Please kindly choose which option by typing the number.")
        print("1. View self")
        print("2. Add Employee")
        print("3. View all")
        print("-----------------------------------------------------------\n")


class view_self:

    def __init__(self, role,name,leave_ctime,leave_etime,leave_status):
        self.role = role
        self.name = name
        self.leave_ctime=leave_ctime
        self.leave_etime=leave_etime
        self.leave_status=leave_status



    def emplyee_manager_self(self,role,name,leave_ctime,leave_etime,leave_status):
        if role==1:
            print("Role: Employ")
        else:
            print("role: Manager")

        print(name)
        print ('applied leave: '+ leave_ctime +' to '+leave_etime)
        print('leave status: '+ leave_status)


    def admin_self(self,name):
        print("Role: Admin")
        print(name)

class apply_leaves:
    def __init__(self,name):
        self.name = name

    def apply_date(self,name):
    #apply_ctime
        year = int(raw_input("Start time(yyyy):"))
        month = int(raw_input("Start time(mm):"))
        day = int(raw_input("Start time(dd):"))
        apply_ctime_timestamp = datetime.datetime(year,month,day,0,0).strftime('%s')
        Leave[name][0]=apply_ctime_timestamp
        with open(
                '../Database/leave.json',
                'w') as outfile:
            json.dump(Leave, outfile)
            outfile.close()
        #print(Leave[name])
    #apply_etime
        year = int(raw_input("End time(yyyy):"))
        month = int(raw_input("End time(mm):"))
        day = int(raw_input("End time(dd):"))
        apply_etime_timestamp = datetime.datetime(year, month, day, 0, 0).strftime('%s')
        Leave[name][1] = apply_etime_timestamp
        with open(
                '../Database/leave.json',
                'w') as outfile:
            json.dump(Leave, outfile)
            outfile.close()
        #print(Leave[name])


    #def auto_check(self):
        #eligibility_check=system_approve_rules()




class add_employee:

    def add_new_role(self):
        try:
            new_role = int(input("New employee's role(staff:1, manager:2, admin:3):"))
            if new_role == 1:
                new_name = raw_input("New employee's name:")
                all['staff'].append(new_name)
                Leave[new_name]=["0","0","none"]
                with open('../Database/employee.json', 'w') as outfile:
                    json.dump(all, outfile)
                    outfile.close()
                with open('../Database/leave.json', 'w') as file:
                    json.dump(Leave, file)
                    file.close()
                print("staff list:", all['staff'])

            elif new_role == 2:
                new_name = raw_input("New employee's name:")
                all['manager'].append(new_name)
                Leave[new_name] = ["0", "0", "none"]
                with open('../Database/employee.json', 'w') as outfile:
                    json.dump(all, outfile)
                    outfile.close()
                with open('../Database/leave.json', 'w') as file:
                    json.dump(Leave, file)
                    file.close()
                print("manager list:", all['manager'])

            elif new_role == 3:
                new_name = raw_input("New employee's name:")
                all['admin'].append(new_name)
                Leave[new_name] = ["0", "0", "none"]
                with open('../Database/employee.json', 'w') as outfile:
                    json.dump(all, outfile)
                    outfile.close()
                with open('../Database/leave.json', 'w') as file:
                    json.dump(Leave, file)
                    file.close()
                print("admin list:", all['admin'])

            else:
                print('please input 1 or 2 or 3')
        except ValueError:
            print('please input 1 or 2 or 3')



def epoch_to_date(epoch):
    return datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d')

invalid_input=True
def start() :
    try:
        role = int(raw_input("Select your role(staff:1, manager:2, admin:3):"))
        name = str(raw_input("name:"))
        leave_ctime =epoch_to_date(float(Leave[name][0])) #epoch time to date
        leave_etime =epoch_to_date(float(Leave[name][1])) #epoch time to date
        leave_status = Leave[name][2]
        if role==1:
            if name in all['staff']:
                #print(role,name,Leave[name][0])
                employee=list_options(role,name)
                employee.Employee_list()
                action=int(raw_input("Option number:"))
                if action==1:
                    employee_view_self=view_self(role,name,leave_ctime,leave_etime,leave_status)
                    employee_view_self.emplyee_manager_self(role,name,leave_ctime,leave_etime,leave_status)
                elif action==2:
                    employee_apply=apply_leaves(name)
                    employee_apply.apply_date(name)
                    system_check=system_approve_rules(name)
                    system_check.eligibility_check(name)
            else:
                print("user doesn't exist")

        elif role==2:
            if name in all['manager']:
                manager = list_options(role, name)
                manager.Manager_list()
                action = int(raw_input("Option number:"))
                if action==1:
                    manager_view_self=view_self(role,name,leave_ctime,leave_etime,leave_status)
                    manager_view_self.emplyee_manager_self(role,name,leave_ctime,leave_etime,leave_status)

                elif action==2:
                    manager_apply = apply_leaves(name)
                    manager_apply.apply_date(name)
                    system_check = system_approve_rules(name)
                    system_check.eligibility_check(name)

                elif action==3:
                    manual_approve = approve_leaves(name)
                    manual_approve.view_pending_list()
                elif action == 4:
                    manual_approve = approve_leaves(name)
                    manual_approve.change_status()

            else:
                print("user doesn't exist")

        elif role==3:
            if name in all['admin']:
                print(role, name)
                admin = list_options(role, name)
                admin.Admin_list()
                action = int(raw_input("Option number:"))
                if action==1:
                    admin_view_self=view_self(role,name,leave_ctime,leave_etime,leave_status)
                    admin_view_self.admin_self(name)
                elif action==2:
                    add=add_employee()
                    add.add_new_role()
                elif action == 3:
                    for key in Leave:
                        print(key)
                        print('applied leave: ' + Leave[key][0] + ' to ' + Leave[key][1])
                        print('leave status: ' + Leave[key][2])

            else:
                print("user doesn't exist")

        else:
            print('please input 1 or 2 or 3')
    except ValueError:
        print('please input 1 or 2 or 3')

while invalid_input :
    start()
