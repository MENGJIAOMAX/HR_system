# Python Assignment

This is my Python assignment to build a mini HR system. 

**Requirements**

TODO: 
Only have one team, staff type: emplyee, manager,admin

In Login_view_apply_add MJ.py (including easy basic class and main code)

Employee can :
1: View self info
    include: role number, name, apply leave start time, pply leave end time, and leave status

2: Apply leaves.
Input start time and end time
Initial status is "none"
After apply leaves, will directly do system apply leaves eligibility check
if the application period is less than 20 (excule holiday and weekends)
& each date not everybody in the team on leave
Then change the status to "Pending"
Waiting Manager to approve

Manager can:
1.View self info
include: role number, name, apply leave start time, pply leave end time, and leave status

2: Apply leaves.
Input start time and end time
Initial status is "none"
After apply leaves, will directly do system apply leaves eligibility check
if the application period is less than 20 (excule holiday and weekends)
& each date not everybody in the team on leave
(system check will be class in approve_rule_MJ.py)
Then change the status to "Pending"
Waiting Manager to approve

3: View list of staff whoes leave status is "pending" or "none"
(will call the class in Manual_approve_leaves_MJ.py)

4: Approve leaves
Input employee name 
Change his/her leave status to "Approved" or "Rejected"

Admin can:
1.view self
include role and name

2.Add new employee
will add new item in employ.json
and add new key in leave.json

3.view all
can will all employee,manager,admin list 
with applied leave periond and leave status



approve_rules_MY.py--> system apply leaves eligibility check
1. Print all day-dates between two dates of leaves period
2. Exculde weekends and holiday
3. Calculate how many days off in total
4. Check  whether the lenght is less than 20 days
5. Check each day not everybody is on leave


Manual_approve_leaves_MJ.py-->
manager view pending/none employee list
then make a decision to approve or reject
then write the new status in leave.json


in leave.json file, Leave=[leave start time, leave end time, leave application status]
**Others**

Run the program from the  login_view_apply_add_MJ.py
