string_of_numbers = raw_input()
list_of_numbers = string_of_numbers.split()

smallest = int(list_of_numbers[0])
second_smallest = int(list_of_numbers[1])

for number in list_of_numbers :
    number_int = int(number)
    if number_int < smallest :
        second_smallest = smallest
        smallest = number_int
    elif number_int < second_smallest :
        second_smallest = number_int

print "The second smallest integer is: %d" % second_smallest