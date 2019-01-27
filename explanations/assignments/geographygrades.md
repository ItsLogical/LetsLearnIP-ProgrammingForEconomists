# Geography Grades 1

> For this walkthrough, I'm not gonna assume that you've followed the [previous
walkthroughs](chapter2/index.md) from chapter 2. I've found that most people
will just copy-paste their way through those assignments with the help of 
friends, or find some other way to finish 'em without really understanding them. 
>
> So for this walkthrough, I'll be assuming that this is where you start with
these walkthoughs, and I'll be explaining it accordingly. This means I *might* 
be repeating a lot of what you know already. Don't sweat it, though. It can 
never do any harm to re-read stuff you already know.

Okay, so first off, for this assignment you might wonder: where do I start?

(Apart from the basics used in every assignment for this course, of course,
being something like this:)

```python
''' Assignment: Geograph Grades 1
    Created on [whenever]
    @author: [whoever]'''


'''Start Program'''

```

Well, we already know what we want as our end result; it's the 'report-type-thing'
printed as output. A good way to solve these kinds of problems is with a
top-down approach (since we know what we want, but don't exactly know how
to get there). So how do we generate our report? Well... it has a 'header'
("Report for group 2b"), a 'footer' ("End of report"), and a bunch of stuff (the
actual report) in the middle. So lets write this down below the '''Start Program'''
line:

```python
print "Report for group 2b"
print_report()  # this function is going to take care of printing the actual report
print "End of report"
```

Now, you might think: where the hell does this `print_report()` function come from?
Well, nowhere at the moment... you are going to implement it! In fact, if you
try to run the program now, you'll get an error because the `print_report`
function isn't defined yet. So let's define it:

Write the following down somewhere above the '''Start Program''' line:

```python
def print_report():
    print "Anne Adema has an average grade of 5.5"
```

If you run the program now, it'll work! And it'll print the following:

```text
Report for group 2b
Anne Adema has an average grade of 5.5
End of report
```

Looking pretty good already! Looks a lot like the final deliverable. However,
since it isn't actually generating a report based on an input file, this program
will probably get you a 1.0 on *your* report... (But we're making progress! Not
too far from that 10.0 now!)

So the `print_report` function should generate a report based on an input file,
but is isn't really doing anything like that at the moment. So let's fix that.

The first thing the `print_report` function should do is read in the input file,
since all of the data the function needs is inside of it. Now, how do we read in
a file? The answer to this is given in the programming manual (but you have to
really look for it, though. The programming manual suuuucks...).

On line 46 of the Hatzelklatzer-whatever example program (on pages 27-28), you'll
find `lines = open('input.txt').readlines()`. Let's break it down a bit:

The `open()` function opens the file that you give as its sole argument. So
`open('input.txt')` will look inside of the current directory* - the directory
your Python script is in - and **opens** it. Now, take note to the fact that
*opening* is not the same as *reading* (you could also, for example, open a
file just to *write* to it). So *first* you have to open a file, and *then* you can
read it - which, of course, is what the `readlines()` function is doing.
`readlines()` returns an array of strings (the lines in the file), and the
result is stored in the `lines` variable. (You could also have used `read()` to
read input of course. The difference is explained in the manual on page 28).

Now that we know that, change your `print_report` function to the following:
(And make sure the `input.txt` file is in the same directory as your python file!)

```python
def print_report():
    lines = open('input.txt').readlines()
    for line in lines:
        print line
```

If you run your program now, you'll get (don't mind the newlines you get in 
between):

```text
Report for group 2b
Anne Adema____________6.5 5.5 4.5

Bea de Bruin__________6.7 7.2 7.7

Chris Cohen___________6.8 7.8 7.3

Dirk Dirksen__________1.0 5.0 7.7
[etc]
End of report
```

Looks good! The program is actually reading data from a file, and we know that
the `line` variable will contain a string - a single line of the input file. So
where to go from here? Well, we need to turn the raw input line of the format
`[Fname] [Lname]___[bunch of underscores]___[grade1] [grade2] [grade3]` into the
line we actually want (`[Fname] [Lname] has an average grade of [avg grade]`),
and print that, of course.

Right now, we have one entire line in the variable `line` each time the for-loop
iterates over the `lines` list. What we'll really want - to be able to print 
what we want to print - is the name of a student in its own variable, and have 
the average grade in its own variable. If we have those, we can easily print the
string we want to print.

Lets start off by putting this functionality in a seperate function, which will
take the `line` as a parameter, and will process the line further to perform all
of we work that we want to achieve:

```python
def process_input_line(line):
    # will be implemented in a second

def print_report():
    lines = open('input.txt').readlines()
    for line in lines:
        process_input_line(line)
```

Now, how do we get the student name and the grades into seperate variables? 
Well, starting off simpler, how do we even get the name of the student and a 
string of his/her grades in seperate variables (so we'd have, for example, a 
variable `student` containing `Anne Adema`, and a variable `grades` containing 
`6.5 5.5 4.5`)?

Well, lets see... each `line` is really made up of two distinct parts, divided by
(a number of) underscores. If we could split up our `line` on underscores, the
first part would be the name of the student, and the last part would be a string
of the grades. Thankfully, there is a very helpful function for python string to
do this. Each string in python has a method called `split()`, which does exactly
what we want. It returns a list of the parts of the string that were divided by 
its first argument (if it is called with no arguments, it splits on
whitespaces).

So, if we have a list of strings, how do we get the first and the last part?
Well, getting the first part is obvious of course: it is the item on index 0.
But for the last part, we don't know upfront of how many parts the list will
consist, so we'll have to compute the index number. Thankfully, it is not the 
hardest of things to compute. The index number of the last item of a list will 
always be equal to `the length of the list - 1`. (Which, of course, is logical
if you think about it, since indices start at 0. Think of a list of length 2; 
the last item will be at index 1. Length 3; index 2, and so on...). The length 
of a list can be gotten using the `len()` function.

> A more widely used term for a 'list' in other languages is an 'array'. While
programming, you'll come across that term *a lot*

So, let's put into practice what we just read. Each time the for-loop loops, our
`line` variable will contain one line of the input, so we call `split("_")` on
it, and extract the student name and grades. So we change our `print_report`
function to:

```python
def process_input_line(line):
    split_line = line.split("_")
    student_name = split_line[0]

    list_len = len(split_line) 
    grades = split_line[list_len - 1]

    # student_name now contains a string of the student name
    # grades now contains a string of the grades;
    print student_name + " - " + grades
```

Running the program now results in:

```
Report for group 2b
Anne Adema - 6.5 5.5 4.5

Bea de Bruin - 6.7 7.2 7.7

Chris Cohen - 6.8 7.8 7.3

Dirk Dirksen - 1.0 5.0 7.7
[etc]
```

Not *too* different from what we just had. But *now* we have the student name 
and (more importantly) the grades in seperate variables, meaning we could 
perform further operations on 'em. Which is great, because we still have some 
work to do regarding the grades. 

What we have now (in the variable `grades`) is a string with contents like 
"6.5 5.5 4.5" or "6.8 7.8 7.3" or w/e. We can't calculate averages from that.
To calculate an average from those numbers, we need to extract the three grades
seperately as `floats` (as they are floating-point numbers). Then, we can, of 
course, use elementary school math to calculate the average of the three.

Luckily, we already know how to divide a string in seprate parts based on a 
common delimiter. If we use the `split` function on the grades, it returns us
an array of the seperate grades *as strings*.

Let's do that now:

```python
def process_input_line(line):
    split_line = line.split("_")
    student_name = split_line[0]

    arr_len = len(split_line) 
    grades = split_line[arr_len - 1]

    split_grades = grades.split()   # we don't need an argument. No arguments in the split function means 'split on whitespace'
    print split_grades[0] + " " + split_grades[1] + " " + split_grades[2]
```

Run the program, it will print the grades.

Great! We now have the grades as seperate values. So can we do arithmetic on
them to calculate the averages yet? Well, almost. As I just mentioned, the 
values are strings, i.e. the data types of the values are *string*. We can't 
*really* do arithmetic on strings. String arithmetic will result in something
like "1" + "1" = "11" (go ahead - try it!), which is *not* what we want.

We can convert strings containing numbers to *actual* numbers by using 
`int()` for integers, and `float()` for floating-point number.  Since we're 
dealing with floating point numbers, we need to use `float()` of course. Once we
have the grades as floats, we can calculate the average of the three just as 
you'd imagine. 

Because this bit of code is also pretty *general*, let's write it in a seperate
function as well.

Our program now looks like:

```python
def get_grades_average(grades):
    grade1 = float(grades[0])
    grade2 = float(grades[1])
    grade3 = float(grades[2])
    return (grade1 + grade2 + grade3) / 3

def process_input_line(line):
    split_line = line.split("_")
    student_name = split_line[0]

    list_len = len(split_line)
    grades = split_line[list_len - 1]
    split_grades = grades.split() 
    average = get_grades_average(split_grades)
    print "%s has an average grade of %0.1f" % (student_name, average)
```

> If you haven't seen the format string stuff before (the `%s` and `%0.1f`); the
`%`-sign tokens simply get replaced by the value of the variable behind the 
string (after the sepearte %-sign) *in the order of appearance*. Here, the 's'
in `%s` simply stand for `string`, the `f` means `float`, and we don't see it 
here, but a `d` means `int`. Futhermore, the `%0.1f` simply means: round the 
float to 1 digit behind the decimal point.

Okay, let's run it. We'll get:

```text
Report for group 2b
Anne Adema has an average grade of 5.5
Bea de Bruin has an average grade of 7.2
Chris Cohen has an average grade of 7.3
Dirk Dirksen has an average grade of 4.6
[etc]
End of report
```

Grrreat! We're done!

Our finished program looks like: 

```python
''' Assignment: Geograph Grades 1
    Created on [whenever]
    @author: [Whoever]'''

def get_grades_average(grades):
    grade1 = float(grades[0])
    grade2 = float(grades[1])
    grade3 = float(grades[2])
    return (grade1 + grade2 + grade3) / 3

def process_input_line(line):
    split_line = line.split("_")
    student_name = split_line[0]

    list_len = len(split_line)
    grades = split_line[list_len - 1]
    split_grades = grades.split() 
    average = get_grades_average(split_grades)
    print "%s has an average grade of %0.1f" % (student_name, average)

def print_report():
    lines = open('input.txt').readlines()
    for line in lines:
        process_input_line(line)

'''Start Program'''
print "Report for group 2b"
print_report()  # this function is going to take care of printing the actual report
print "End of report"
```