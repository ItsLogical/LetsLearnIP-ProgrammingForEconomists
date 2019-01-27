# Othello 2

Again, this assignment starts off similarly as we've seen before:

- Ask user for input;
- Find out which is the biggest.

If you don't know how to do this, you can find out in the 
[previous walkthrough](electronics.md).

The only thing 'new' about this assignment is how to go from a number of 
milliseconds to a time in the format `HH:MM:SS`.

Well, this is just something you have to think about for a while, and then 
you'll find a solution. I'll show you the basic, logical rules, and then 
you can program the rules in Python.

- SECONDS = MILLISECONDS / 1000
- MINUTES = SECONDS / 60
- HOURS = MINUTES / 60

(And then to display then as `HH:MM:SS`, the minutes and seconds have to be
*modulo'ed* (%) of course, since those number shouldn't exceed 60)

> To pad a an `int` in a format string with (a maximum of) two leading zeroes,
you use the format token `%02d`, 

The finished program looks as follows:

```python
time1 = int(raw_input("Enter the time the black player thought: "))
time2 = int(raw_input("Enter the time the white player thought: "))

human_time = time1
if time2 > time1 :
    human_time = time2

human_time_h = human_time / 1000 / 60 / 60
human_time_m = human_time / 1000 / 60 % 60
human_time_s = human_time / 1000 % 60

print "The time the human player has spent thinking is %02d:%02d:%02d" % (human_time_h, human_time_m, human_time_s)
```