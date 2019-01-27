# Alphabet

The assignment description teaches us about the existence of the `ord` and 
`chr` functions. These are vital for this assignment.

- `ord` takes a character, and returns the corresponding 
[Unicode](https://unicode-table.com/en/) index
- `chr` does the opposite; takes a Unicode index as a parameter, and returns 
the character as a string.

> If you've never heard - or don't know - about Unicode or ASCII, it's quite
worthy to read up on 'em; they're the mechanisms with which computers 
represent letters, symbols, etc. from their native bytes (Unicode and ASCII
provide mappings between bytes (representing numbers) and characters). But since
they're used so extensively, it's always good to know how they work. (Think of a
world where computers aren't able to represent characters, that'd suck!)

So, for this assignment, you have to loop from the numeric value of `'a'` 
through the numeric value of `'z'`. 

This would be a good time to mention that, if you want to perform a loop from 
a certain start number through an end number (non-inclusive), there's a great 
and easy way to do this with for-loops. It looks like this:

If you want to loop from 0 through 10:

```python
for i in range(0, 10) :
    print i
```

This prints the numbers 0 through 9 (since the range is non-inclusive).

Now, this also kind of looks like what we should do for our assignment. Only a
few slight differences:

Instead of looping from 0 to 9, we need to loop from \[numeric value of 'a'\]
to \[numeric value of 'z'\] + 1 (the plus one is to include 'z' in the range).

If we properly define our start- and end-points in constants, we get:

```python
START_CHAR = 'a'
END_CHAR = 'z'

for char_int in range(ord(START_CHAR), ord(END_CHAR) + 1) :
    print char_int , 
```

This prints all of our characters, only... as ints! Thanks to the `chr` 
function, though, we can easily convert those back to characters. It makes our
finished program look like this:

```python
START_CHAR = 'a'
END_CHAR = 'z'

for char_int in range(ord(START_CHAR), ord(END_CHAR) + 1) :
    print chr(char_int) , 
```