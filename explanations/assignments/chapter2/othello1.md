# Othello 1

> This game fucking blows... Just learn to play FIFA *real* good, you could make
some good money.

Okay, so, again, a *lot* of what we've already covered is used again to finish
this assignment. In fact, I don't even feel like walking through this one,
and I'll just give you the finished program right away. **But try to finish it
on your own first! If you've followed along/finished the previous two 
assignments, I know you can do it! <3**

I'll make you scroll a bit so you'll be less tempted to glance at the answer
right away. If you're done, proceed to the [next assignment](electronics.md).

<div style="margin-top: 10000px"></div>

Hi

<div style="margin-top: 10000px"></div>

Okay, here:

```python
NUMBER_OF_SQUARES = 64

no_white_pieces = int(raw_input("Enter the number of white pieces on the board: "))
no_black_pieces = int(raw_input("Enter the number of black pieces on the board: "))

total_pieces = no_white_pieces + no_black_pieces

# We need to cast either the dividend or divisor to a float to prevent incorrect
# values due to 'integer division' (where the remainder is discarded)

# (We could have also just cast the raw_input values to floats right away, buuut
# they're supposed to be ints ya know... So I thought this was nicer)
pct_black_board = no_black_pieces / float(NUMBER_OF_SQUARES) * 100
pct_black_all_pieces = no_black_pieces / float(total_pieces) * 100

print "The percentage of black pieces on the board is: %0.2f%%" % pct_black_board
print "The percentage of black pieces of all the pieces on the board is: %0.2f%%" % pct_black_all_pieces
```