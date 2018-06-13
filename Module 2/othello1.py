'''
Assignment: Othello 1
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''

OTHELLO_BORD_SIZE = 64


number_of_white_pieces = float(raw_input("Enter the number of white pieces on the board: "))
number_of_black_pieces = float(raw_input("Enter the number of black pieces on the board: "))

total_pieces = number_of_white_pieces + number_of_black_pieces
percentage_black_pieces_coverage = number_of_black_pieces / OTHELLO_BORD_SIZE * 100
percentage_black_pieces = number_of_black_pieces / total_pieces * 100

print "The percentage of black pieces on the board is: %.2f%%" %percentage_black_pieces_coverage
print "The percentage of black pieces of all the pieces on the board is: %.2f%%" %percentage_black_pieces


''' Example input/output
Enter the number of white pieces on the board: 34
Enter the number of black pieces on the board: 23
The percentage of black pieces on the board is: 35.94%
The percentage of black pieces of all the pieces on the board is: 40.35%
'''