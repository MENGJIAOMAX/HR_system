import json
#import holidays
import time
import datetime
#from datetime import datetime
from datetime import date, timedelta
import os
ROOT_DIR = os.path.abspath(os.curdir)


class system_approve_rules:

    def __init__(self,name,):
        self.name = name

    def eligibility_check(self,name):
        #print("eligibility check")
        #holiday_2020=[]
        #business_day_leave={}
        #pip install holidays (CAN NOT PIP INSTALL EXTERNAL LIBRARIES)
        #Holiday in 2020
        #for date in holidays.Singapore(years=2020).items():
            #holiday_2020.append(str(date[0]))
        #print(holiday_2020)
        #exclude holiday
        with open(
                '../Database/holiday_2020.json',
                'r') as file:
            holiday_mj = json.load(file)
            holiday_2020 = holiday_mj['holiday']
            #print(holiday_2020)
        #exclude weekends
        def epoch_to_date(epoch):
            return datetime.datetime.fromtimestamp(epoch).strftime('%Y-%m-%d')


        with open(
                '../Database/leave.json') as f:
            Leave = json.load(f)
        business_day_leave={}
        for everyone in Leave:

            leave_ctime = epoch_to_date(float(Leave[everyone][0]))  # epoch time to date
            leave_etime = epoch_to_date(float(Leave[everyone][1]))  # epoch time to date
            #datestring_c = leave_ctime
            #datestring_e = leave_etime
            dt_c = datetime.datetime.strptime(leave_ctime, '%Y-%m-%d')
            dt_e = datetime.datetime.strptime(leave_etime, '%Y-%m-%d')
            ctime = datetime.date(dt_c.year, dt_c.month, dt_c.day)
            etime = datetime.date(dt_e.year, dt_e.month, dt_e.day)
            delta = etime - ctime  # as timedelta
            business_day_leave[everyone]=[]# exclude weekends and holidays
            for i in range(delta.days + 1):
                day = ctime + timedelta(days=i)
                if day.weekday() != 5 and day.weekday() != 6 and str(day) not in holiday_2020:
                    business_day_leave[everyone].append((str(day)))

        #print(business_day_leave)


        length = len(business_day_leave[name])

        if length <= 20:
            # for day in business_day:
            # scan each day
            for day in business_day_leave[name]:
                count = 0
                for others in business_day_leave:

                    if day in business_day_leave[others]:
                        count += 1  # not everybody in the team on leave
                if count < len(business_day_leave):
                    print(day,count,"people on leaves","You can take leave on this date") # (days off date, how many people on leave on that day, ok to take leave)

                else:
                    print(day, "Deny,not everybody in the team on leave")
                    Leave[name][2] = "Rejected"
                    with open(
                            '../Database/leave.json',
                            'w') as outfile:
                        json.dump(Leave, outfile)
                        outfile.close()
                        break
            Leave[name][2] = "Pending"
            print("You applied for ", length, "days")
            print("Pending manager to approve")
            with open(
                     '../Database/leave.json',
                     'w') as outfile:
                 json.dump(Leave, outfile)
                 outfile.close()

        else:
            Leave[name][2]="Rejected"
            print("You applied for ", length, "days")
            print("You can not take leaves longer than 20 business days")
            with open(
                    '../Database/leave.json',
                    'w') as outfile:
                json.dump(Leave, outfile)
                outfile.close()
