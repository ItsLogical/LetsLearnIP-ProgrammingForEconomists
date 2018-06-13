'''
Assignment: Collatz
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''


number = int(raw_input("Enter your a number: "))
print "%d: %d" %(number,number),

while number != 1:
    if number % 2 == 0:
        number = number / 2
    else:
        number = 3 * number + 1
    print "%d" % number,

''' Example output
11: 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
'''