'''
Assignment: Expressions 1
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''

#Question 1
result = 2 + 3

#Question 2
result = 1.2 * 2 + 3

#Question 3
result = "ab" + "cd"

#Question 4
result = ord('c') - ord('a') + ord('A')
result = chr(result)

#Question 5
result = True or False

#Question 6
result = 17 / 4

#Question 7
result = 17 % 4

#Question 8
if True:
    print "not not true"

#Question 9
if False:
    print "really not true"

#Question 10
if 2 < 3:
    print "2 is not larger or equal to 3"

#Question 11
if (3 < 2 and 4 < 2 and (5 == 6 or 6 != 5)) or True:
    print "too much work"

#Question 12
number = '7'
print "%c" % number

#Question 13
if False and (3 > 2 or 7 < 14 or (5 != 6)):
    print "finished quickly"