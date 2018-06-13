'''
Assignment: Second Smallest
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''

numbers_string_list = raw_input("Enter a sequence of numbers: ").split()
numbers = map(int, numbers)  # list of ints

smallest = numbers[0]
second_smallest = numbers[1]

for i in range(2, len(numbers)):
    if numbers[i] < smallest:
        second_smallest = smallest
        smallest = numbers[i]
    elif numbers[i] < second_smallest:
        second_smallest = numbers[i]

print "The second smallest number is: %d" %second_smallest

''' Example input/output
10 12 2 5 15
The second smallest number is:5
'''