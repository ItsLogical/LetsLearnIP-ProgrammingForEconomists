'''
Assignment: MileInKilometers 2
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''

PASS_MINIMUM = 5.5

grade = float(raw_input("Enter a grade: "))

if grade >= PASS_MINIMUM:
    print "The grade, %0.2f, is a pass." % grade
else:
    print "The grade, %0.2f, is not a pass." % grade