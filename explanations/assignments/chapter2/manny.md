# Manny

> "*Rightfull* owners"? Really? Jesus Christ, you're supposed to be a 
university; you're supposed to be smart... 

Anyway... we've arrived at the loops part! Do you already understand loops, and
how/why they are used? If not, read the part below:

> ## Why and when to use loops? 
> 
> Say, you have to write a program where you have to print something (let's say: 
> "Hello world") 1000 times. Are you gonna duplicate your `print`-statement a 
> 1000 times? Hell no! That sounds ridiculous. That is analogous to telling your 
> computer: "Hey, computer. Print 'Hello world'. Print 'Hello world'. Print 'Hello
> world'. Print 'Hello world'. \[etc... times a thousand\]". It would be *way* 
> better to tell your computer something like: "Hey, computer. Print 'Hello world'
> a thousand times". 
> 
> And you can - thanks to loops! So, in summary, loops are used to repeat code
> without having to duplicating it (duplicating code is *bad*; what if you have to
> make a change to the code? You'll have to make the change in every copy you
> duplicated. That gets really boring real quick).
> 
> Loops come in two flavours: a `for`-loop, and a `while`-loop. They differences
> are not too big, both are just used to repeat code, and in a lot of cases they
> can be used interchangeably. However, there *are* certain scenario's where usage
> of one over the other is a bit more sensible.
> 
> For loops are generally used more when you have to loop a know amount of times.
> Say you want to loop a constant number of times (like the stupid example above),
> or you want to loop over the items in a list (we know the length of a list,
> using the `len()` function).
> 
> While loops are generally used in situations where you have to loop an unknown
> number of times, and the number of times you loop depends on some external 
> condition.
> 
> These situations where one type of loop is favoured over the other is actually 
> not arbitrary, and it sort of finds its roots in the way we speak. An example:
> 
> "**For** each book in the bookstore, I want you to tell me the author and 
> release date.", or "Could you calculate the averages of the numbers **for** each
> row in this table of data?"
> 
> In code, this could look like:
> 
> ```python
> for book in bookstore :
>     # print book author
>     # print book release data
> ```
> and
> ```python
> for row in table :
>     # calculate average of columns
> ```
> 
> Same thing with while-loops:
> 
> "**While** my employer keeps paying me, I'll show up and do my job correctly", 
> or "I'm gonna console my girlfriend **while** she feels so sad", translates 
> to:
> 
> ```python
> while did_employer_pay_me :
>     # show up
>     # be a good employee
> ```
> and 
> ```python
> while gf_feels_sad :
>     # console her
> ```

Okay, so now you've had enough background on loops. Now you should know 
everything you need to finish the assignment. 

So, the assignment requires you to write a program that keeps asking the user 
for input, until the user enters a value is greater than 50.

Slightly rephrased, we can describe the assignment as: "*while* the entered 
input is smaller than 50, ask the user for input".

This rephrasing almost entirly describes the program. So the next step is to
simply implement it in Python. It gives us:

```python
entered_amount = 0
while entered_amount < 50 :
    entered_amount = float(raw_input("Enter the amount you want to donate:\n"))

print "Thank you very much for your contribution of %0.2f euro." % entered_amount
```