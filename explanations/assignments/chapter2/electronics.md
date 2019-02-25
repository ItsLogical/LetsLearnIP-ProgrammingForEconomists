# Electronics

Okay, so the first part of the program we should be building looks very familiar
again. Asking the user for input, storing it in a variable: easy peasy.

We start with:

```python
price1 = float(raw_input("Enter the price of the first article: "))
price2 = float(raw_input("Enter the price of the second article: "))
price3 = float(raw_input("Enter the price of the third article: "))
```

> We cast the inputs we get from `raw_input` to floats, of course, since we are
dealing with a number representing money

Then comes the part of the assignment where it differs from the previous few; 
this assignment will require the use of `if`-statements. 

> What are `if`-statements? Well, an example is given on page 20 of the manual,
so be sure to check that out. A short recap: an `if`-statement is used to 
conditionally execute lines. It looks like:
>
> ```python
> if something :
>    # execute these lines
>    print "something was True"
> else :
>    # execute these lines
>    print "something was False"
>```
>
> Note the indentation - this is Python's way of knowing which code belongs 
where. An example:
> ```python
> x = 5
> if x > 10 :
>     # This line is indented, so it belongs to the if-clause
>     print "5 is bigger than 10, apparently..."
> # This code is not indented, so doest belong to the if-clause and gets executed
> print "Hi, this gets printed whether 5 > 10 or not."
> ```
> Running this will result in:
> ```plaintext
> Hi! this gets printed whether 5 > 10 or not.
> ```

Okay, what should we actually do for this assignment again? Oh yeah, figure out
which of the three `priceX` variables is the biggest. How do we do that? Let's 
create a simple algorithm (in human language) for this:

- Assume `price1` is the highest of the three. 
- If `price2` is bigger than the highest, `price2` is the new temporary highest.
- If `price3` is bigger than the  highest of *those* two, `price3` is the actual
highest.

(This is just *one* way to caluclate the highest, you could think of a bunch
of other ways if you want - maybe even better, I don't know, I'm pretty tired 
right now...)

Translating this little 'alogrithm' to Python is not too hard, we can already
see the word 'if' being used al over the place, so we know where to use it.
We get:

```python
# Assume price1 is the highest for now
highest = price1
if price2 > highest :
    # If price2 is bigger, it is the highest of the two
    highest = price2
if price3 > highest :
    # If price3 is bigger than that, price3 is the highest
    highest = price3
```

Once we have the highest of the three in a variable, calculating the discount
and the total is trivial. Don't forget to put the discount percentage in a 
constant at the top of your file, though. The TA's *love* that kind of stuff.

The finished program looks as follows:

```python
DISCOUNT_MULTIPLIER = 0.15

price1 = float(raw_input("Enter the price of the first article: "))
price2 = float(raw_input("Enter the price of the second article: "))
price3 = float(raw_input("Enter the price of the third article: "))

highest = price1
if price2 > highest :
    highest = price2
if price3 > highest :
    highest = price3

discount = highest * DISCOUNT_MULTIPLIER

print "Discount: %0.2f" % discount
print "Total: %0.2f" % (price1 + price2 + price3 - discount)
```

Okay, [next assignment](othello2)