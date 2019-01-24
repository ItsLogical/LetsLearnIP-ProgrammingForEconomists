NUMBER_OF_SQUARES = 64

no_white_pieces = int(raw_input("Enter the number of white pieces on the board: "))
no_black_pieces = int(raw_input("Enter the number of black pieces on the board: "))

total_pieces = no_white_pieces + no_black_pieces

# We need to cast either the dividend or divisor to a float to prevent incorrect
# values due to integer division
# (We could have also just cast the raw_input values to floats right away, buuut
# they're supposed to be ints ya know... So I thought this was nicer)
pct_black_board = no_black_pieces / float(NUMBER_OF_SQUARES) * 100
pct_black_all_pieces = no_black_pieces / float(total_pieces) * 100

print "The percentage of black pieces on the board is: %0.2f%%" % pct_black_board
print "The percentage of black pieces of all the pieces on the board is: %0.2f%%" % pct_black_all_pieces