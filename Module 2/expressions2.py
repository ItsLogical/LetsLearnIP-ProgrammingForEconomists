'''
Assignment: Expressions 2
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''

#Question 1
def function():
    number = 2
    return number / 3
    result = function() * 3


#Question 2
def world_upside_down():
    numbers_upside_down = 2 > 3
    booleans_upside_down = True == False
    return numbers_upside_down and booleans_upside_down

if world_upside_down():
    print "The world is upside down!"
else :
    print "The world is not upside down."


#Question 3
def awkward_number():
    character = 'y'
    return 'z' - character

print "The result is awkward " + "result: \%s" % awkward_number()


#Question 4
if 'a' < 'b':
    print "smaller"


#Question 5
if 'a' > 'B':
    print "hmmm"


#Question 6
number = '7'
print "%d" % number - 1
