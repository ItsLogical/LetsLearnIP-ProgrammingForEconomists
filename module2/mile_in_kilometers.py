'''
Assignment: MileInKilometers
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''

MILE_IN_KILOMETERS = 1.609344

number_of_miles = int(raw_input("Enter the number of miles: "))
number_of_kilometers = number_of_miles * MILE_IN_KILOMETERS

print "%f miles equals %f kilometer" % (number_of_miles, number_of_kilometers)