'''
Assignment: Manny
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''

MIN_DONATE_AMOUNT = 50

donation = 0
while donation < MIN_DONATE_AMOUNT:
    donation = float(raw_input("Enter the amount you want to donate: "))

print "Thank you very much for your contribution of %.2f euro." %donation

''' Example input/output
Enter the amount you want to donate:
0
Enter the amount you want to donate:
10
Enter the amount you want to donate:
52
Thank you very much for your contribution of 52.00 euro.
'''