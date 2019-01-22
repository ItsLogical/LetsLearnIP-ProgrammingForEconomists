# SecondSmallest

Okay, this assignment, again, starts off recognizable; the user is asked for 
input. Only now, there is a slight difference: here instead of only entering a 
single number, you have to enter a list of numbers, seperated by spaces.

We run into a problem, though. In the previous assignments, whatever was 
returned by the `raw_input` function, we could just assume that the input was
correct and we could cast it right away to the data type we needed. However, 
since this input represents multiple int's instead of a single one, we can't do
that.

By default, `raw_input` returns the entered value as a string. If we want to 
process this input further into multiple int's, we have to use the `split()` 
method. The `split` method splits a string on whitespace, and returns the
separate parts of the string in a list (which you can easily iterate though
using a for-loop).

> You might not know what methods (or functions) exactly are, but it will be 
explained in the next chapter. Consider everything you learn now about functions
and methods as a bonus which will make your life a bit easier in the following 
chapter

Here is a small example of what the `split()` method does:

```python
someSentence = "If I ever get around to living"
words = someSentence.split()
# words now contains ['If', 'I', 'ever', 'get', 'around', 'to', 'living']

for word in words :
    print word
```

If you'd run this little example program, you get:

```
If
I
ever
get
around
to
living
```
(Which is the song that's currently playing in the background while I write
this...)

Okay, but now back to our program. If we write the following:

```python
string_of_numbers = raw_input()
list_of_numbers = string_of_numbers.split()
```

And give "10 12 2 5 15" as input, `list_of_numbers` will contain `['10', '12', 
'2', '5', '15']`. This is pretty good! Only thing is, all items in the list are
`string`s, not `int`s. We need them to be `int`s, so when we use them, we have to
cast them to `int`s. We just have to keep that in mind.

Okay, proceeding. According to the description of the program, we can assume 
that the first number is smallest than the second, so we can already add this
assumption to our program:

```python
smallest = int(list_of_numbers[0])
second_smallest = int(list_of_numbers[1])
```

Then, it's time to loop over the items of the `list_of numbers`, and find out 
which of the numbers is the second smallest. How do we figure out which one is 
the second smallest? Well, there are a *lot* of ways actually... One algorithm
to solve it would he something like this:

For each `number` in the list,

-  if the `number` is smaller than our current smallest, the old smallest value
will now be the second smallest value, and the `number` becomes our new smallest
- if the `number` is only smaller than the second smallest (and, thus, bigger
than the smallest) the `number` becomes the new second smallest 

Still get it? Okay, let's implement it:

```python
for number in list_of_numbers :
    number_int = int(number)    # Don't forget the cast
    if number_int < smallest :
        second_smallest = smallest
        smallest = number_int
    elif number_int < second_smallest :
        second_smallest = number_int
```

Great! That's actually all for this program, except for the final print 
statement; but that's trivial. Our finished program looks like: 

```python
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
```

Okay, grrrreat! You're done with the assignments for chapter 2! Make sure you
**really, really** understand everything from this chapter, though. This chapter
was relatively easy, and with the stress of having to reach a deadline gone, 
you can fully focus on understanding everything and learning more about
programming. 