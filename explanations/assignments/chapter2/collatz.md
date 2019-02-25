# Collatz

Okay, this program starts off quite simple: by asking the user for some number.
We've seen this before countless times, so we know what to do:

```python
start_number = int(raw_input("Please enter the number you'd like to start with: "))
```

Now, what should we do with that start number? Well, thankfully, it's written 
quite clearly in the assignment description. In fact, it describes the entire
algorithm we need to implement (and even parts on how to). Essentially, as long
as (*while*) the number is *not* 1 (because that's when it should terminate), it
should repeat the steps described in the manual:

- if `n` is even, `n = n / 2` (can also be written as `n /= 2`)
- else (`n` is odd), `n = 3 * n + 1`

> As is written in the assignment description; you can test whether a number is
even (or odd) using the modulo-operator (%). In case you didn't know, the modulo
operator returns the remainder of the division. So `5 % 2 = ` the remainer of 
`5 / 2`, which is `1`, of course. A second of thought will probably lead to the
realisation that if `n % 2 == 0`, `n` is even, and if `n % 2 == 1`, `n` is odd.

Well, now we've almost described the entire program in human language, so let's 
translate it int Python:

```python
number = int(raw_input("Please enter the number you'd like to start with: "))
print number ,
while number != 1 :
    if number % 2 == 0 :
        number /= 2
    else :
        number = 3 * number + 1
    print number ,
```

Voila! On to the [next](secondsmallest) (and last of the chapter)!