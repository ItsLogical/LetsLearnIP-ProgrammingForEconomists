CALL_OUT_COST = 16.00

hourly_wages = float(raw_input("Enter the hourly wages: "))
hours_worked = float(raw_input("Enter the number of hours worked: "))
hours_worked_rounded = round(hours_worked)
total_cost = hourly_wages * hours_worked_rounded + CALL_OUT_COST
print "The total cost of this repair is: %0.2f euro" % total_cost