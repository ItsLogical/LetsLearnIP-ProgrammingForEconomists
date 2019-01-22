# VAT

Okay, so the first thing this program needs to do is to ask the user for input
with a certain prompt. We know how to do this, it's written in the  manual on 
paaaaggeee... okay nevermind, it's not written in the manual, Jesus...
Oh, no, well it *kind of* is. It's hidden in 'If statement' example on page 20, 
but it isn't explained anywhere. *(On second - uhh, 'search' - I also found it
in the first deliverable assignment - hello_world2 or something - but I can't
expect anyone to really be aware that they've used this, since most people just
copy-paste this assignment)*

But anyway, prompting a user for input is done with the `raw_input` function. 
If we want to ask the user for input, we write: 

```python
someVariable = raw_input("Please enter some input, dear user: ")
```

(Notice the `"`'s - double quotes - these should be here)

> What's happening here? Well, `raw_input` is a built-in Python function that
> takes as its first parameter a string, being the prompt that it will present
> to the user, and will *return* a string containing whatever the user entered.
> This string is then stored in the variable `someVariable` (which is a 
> **terrible** variable name, but I'm just showing you an example, so gimme a 
> break... Just a reminder: *variable names should be descriptive of its 
> contents*. Happy now?)
>
> If you don't know what I'm talking about with terms like 'function', 
> 'parameter', 'return', you'll learn about them in this course, so don't worry.
> But if you *really* can't wait to learn, I'll explain 'em [here]().

We want to print 'Enter the price of...'-blabla as a prompt, so we write in our
program:

```python
priceIncludingVAT = float(raw_input("Enter the price of an article including VAT: "))
```

> Notice the *beautifully* descriptive variable name (WOW!), anyone reading this 
> program - ever - will *exactly* know what the variable contains.
>
> Variable names can be long - no problem. Just try to find the right balance 
> between being descriptive and being a chore to type.

You'll probably have noticed that we have `float()` surrounding our `raw_input`
function. This is because `raw_input` returns a string by default, and we want
it to be a float since we need to perform some calculation on it. Since we're
talking about a *price* - which is money - we need it to be a float rather than
an int, so it can handle cents.

Okay, so now we have our user input in the variable `priceIncludingVAT`. What 
should we do if we want the price excluding VAT in a seperate variable. Well, 
that's just elementary school math. We add the following to our program:

```python
priceExludingVAT = priceIncludingVAT / 1.21
```

Grrreat! But wait... let's make the program a bit *nicer*. Let's make the VAT 
value (`1.21`) a constant, since it won't ever change in our program. Also, it
is a good programming practice to have all (literally) 'constant' values in your
program defined as constants at the top of your program.

> There is actually no difference between a normal variable and a constant in 
> Python (some languages *do* have differences between them), and you can even
> change the value of your 'constant' in your Python program (not that you ever
> *should*). This whole constant-stuff in Python is just purely cosmetic, so 
> you can easily identify variables as constant on a first glance.

So add the following line at the top of your program:

```python
VAT_PERCENTAGE = 21.00
```

and change the other line we just wrote to use the newly created constant:

```python
priceExludingVAT = priceIncludingVAT / ((100 + VAT) / 100)
```

Now, to finish our program we just add the following line:

```python
print "This article will cost %0.2f euro without %0.2f%% VAT." % (priceExcludingVAT, VAT_PERCENTAGE)
```
> What we see here is a *format string*. It's an easy way to include the value
of a variable inside of a string. Inside the string, you write `%`-something 
(like `%f` for a float, `%d` for an in, or `%s` for a string), and then that
part will be replaced by the variable *behind* the string, after the '%'.
With more tokens in the string, the first variable replaces the first token, and
so on. 

> The `%0.2f` stuff is just the way to round floats to two digits after the 
decimal point.

> Lastly, the `%%` is to 'escape' the formatting behaviour of percentage-signs,
and just print a literal '%'.

Our entire program looks like this:

```python
VAT_PERCENTAGE = 21.00

priceIncludingVAT = float(raw_input("Enter the price of an article including VAT: "))
priceExcludingVAT = priceIncludingVAT / ((100 + VAT_PERCENTAGE) / 100)
print "This article will cost %0.2f euro without %0.2f%% VAT." % (priceExcludingVAT, VAT_PERCENTAGE)
```

Grrreat! Done. [Next](plumber.md).