number = int(raw_input("Please enter the number you'd like to start with: "))
print number ,
while number != 1 :
    if number % 2 == 0 :
        number /= 2
    else :
        number = 3 * number + 1
    print number ,