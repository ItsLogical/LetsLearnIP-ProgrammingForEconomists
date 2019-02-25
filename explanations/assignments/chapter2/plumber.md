# Plumber

Okay, most of the stuff you need to know to complete this assignment was 
already discussed in the previous assignment. So if you find I'm glossing over 
some stuff, make sure you've read (and understand) the previous walkthrough.

Use the `raw_input` function to gather the info needed from the user. Also,
don't forget to cast the values to their correct data type. Both need to be 
floats, and then we'll round the hours worked to the nearest int after that.

```python
hourly_wages = float(raw_input("Enter the hourly wages: "))
hours_worked = float(raw_input("Enter the number of hours worked: "))
hours_worked_rounded = round(hours_worked)
```

> `round()` is a built-in Python function, it takes a float and returns the 
nearest int. It still returns it as a float though! So `4.5` will really be
`5.0` instead of `5`.

With the `hourly_wages` and `hours_worked_rounded` variables, calculating the
total cost is a piece of cake, of course. We just need to add the call-out cost,
and that is also a good example of something we'd want to declare as a constant.

Add the following to the top of your program:

```python
CALL_OUT_COST = 16.00
```` 

And add these last two lines at the end to finish your program:

```python
total_cost = hourly_wages * hours_worked + CALL_OUT_COST
print "The total cost of this repair is: %0.2f euro" % total_cost
```

> If you don't get the `%0.2f` stuff; explanation of format strings is given in 
the [VAT walkthrough](vat)

Our finished program looks as follows:

```python
CALL_OUT_COST = 16.00

hourly_wages = float(raw_input("Enter the hourly wages: "))
hours_worked = float(raw_input("Enter the number of hours worked: "))
hours_worked_rounded = round(hours_worked)
total_cost = hourly_wages * hours_worked_rounded + CALL_OUT_COST
print "The total cost of this repair is: %0.2f euro" % total_cost
```