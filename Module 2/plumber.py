'''
Assignment: Plumber
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''


CALL_OUT_COST = 16.00  # in euro's

hourly_wages = float(raw_input("Enter the hourly wages: "))
worked_hours = float(raw_input("Enter the number of hours worked: "))

billable_hours = round(worked_hours)

total_costs = billable_hours * hourly_wages + CALL_OUT_COST

print "The total cost of this repair is: %.2f euro" % total_costs

''' Example input/output
Enter the hourly wages: 31.50
Enter the number of hours worked: 4.5
The total cost of this repair is: 173.50 euro
'''