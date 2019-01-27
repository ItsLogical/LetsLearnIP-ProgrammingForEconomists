# Administration

Okay, so where to start with this assignment? It's actually not too different
from the [previous one](geographygrades.md), and we're gonna reuse a lot of
techniques we used there.

Okay, let's begin programming. We should start by reading the input. We'll use
the `readlines` method we used in the previous assignment. But you know what? 
This time, let's define the name of the file in a constant. It's a tiny bit nicer:

```python
INPUT_FILE = "input.txt"

''' Start Program '''
input = open(INPUT_FILE).readlines()
```

Now `input` will consist of a list where each item is a line in the file as a
string. The next sensible thing to do, would therefore be to loop over this
list and handle each line accordingly. Only thing is, not all lines should be
handled the same. 

However, every *two* lines *should* be handled the same. So if
we were able to do something like: "For each two lines in the input, handle
the first line like this, and handle the second line like this (and have the
next iteration of the loop start at the next *two* lines)", our lives would be
a lot easier. Luckily, we can! In fact, there's a lot of ways this kind of 
behaviour can be acchieved.

Here one way: 

Using the `range` function (you've probably seen it before), you can generate
a list of integers while *stepping* a certain amount. You may or may not have 
seen/used this before, but the `range` function takes a third optional 
parameter with the *step* amount (the default is 1, of course). This means:

```python
print range(0, 10)
# Will result in:
# > [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print range(0, 10, 2)
# Will result in:
# > [0, 2, 4, 6, 8]

print range(0, 10, 3)
# Will result in:
# > [0, 3, 6, 9]
```

You get it, right? Now, thankfully, this is just the kind of functionality we 
were looking for! We can now add the following to our program:

```python
for i in range(0, len(input), 2) :
    first_line = input[i]
    second_line = input[i + 1]
```

Great! Do you get what's going on here? On the first iteration of the loop,
`i` equals 0, and `first_line` contains whatever lies on the zero'th index of 
`input`. `second_line` contains whatever is on the (0 + 1)'th index of the 
`input` list (meaing, of course, `first_line` will contain a string of the 
`"Piet van Gogh____5 6 7 etc..."` type, and `second_line` will contain the
`"5=20=22=10 etc..."` type line). On the second iteration of the loop, `i` 
contains 2 (instead of 1), and `first_line = input[2]`, and 
`second_line = input[2 + 1]`. On the third iteration, `i` contains 4, and so 
on...

Now, for the further processing of the two lines, we'll create two seperate
functions that will take the line as a parameter, and will do whatever they need
to do.

Above the code we just wrote, define the following functions:

```python
# This function takes a string of the format:
#   [Student name][a number of underscores][grades]
# and prints the student name along with the average grade
def calculate_student_final_grade(line) :
    # We'll implement this later

# This function takes a string of the format:
#   [similarity_scores];[optional list of student names]
# and processes it accordingly
def process_similarity_scores(line) :
    # We'll implement this later
```

and call those functions from within the for-loop body. Add to the for-loop body
so it looks like this:

```python
for i in range(0, len(input), 2) :
    first_line = input[i]
    second_line = input[i + 1]
    calculate_student_final_grade(first_line)
    process_similarity_scores(second_line)
```

Okay, let's implement our `calculate_student_final_grade` function first. What
this function should do is actually very similar to the previous assignment.
The format of the line is similar (Name - underscores - grades), so we know what
to do:

- We have to split the line on underscores, and extract the first and last part.
- We have to further process the last part by splitting *it* on whitespace and
casting the grades to floats

It looks a lot like what we did previously:

```python
def calculate_student_final_grade(line) :
    split_line = line.split("_")
    student_name = split_line[0]

    list_len = len(split_line)
    grades_str = split_line[list_len - 1]
    grades_list = grades_str.split()
    average = get_grades_average(grades_list)
```

There, *is* a difference, however, in how our `get_grades_average` function 
looks. Instead of knowing that there's gonna be three grades, now it can be any
number of grades, so we'll have to handle that in a for-loop. Also we have 
to implement the '6-' logic, and the rounding to half functionality.

> But wait, how do you round to half? Well, an easy - and correct - solution is 
to simply multiply your float by 2, round *that* off, and then divide by 2.
> 
> A quick example with 7.3 (*quick maffs*):
> ```
> 7.3 * 2 = 14.6 => gets rounded to 15.0
> divided by 2 makes 7.5. Perfect!
> ```
>
> In Python, rounding is done with the `round` function

Our `get_grades_average` function looks as follows:

```python
# This function takes a string of grades seperated by spaces and return the
# average of grades as a string, since one of the posential return values is 
# '6-'
def get_grades_average(grades) :
    total = 0
    for grade in grades:
        total += float(grade)
    average = total / len(grades)
    if average >= 5.5 and average < 6 :
        return "6-"
    return round(average * 2) / 2
```

Then, we can add the following line to our `calculate_student_final_grade` 
function to finish it:

```python
    print "%s has an average of %s" % (student_name, average)
```

Great! Now let's proceed with our `process_similarity_scores` function. Slight
reminer: it should process the `5=20=22;Name,Name` type of lines. Right off the 
bat, it's obvious that the line consists of two distinct parts (seperated by the
';' - the semicolon). That calls for some more splitting:

```python
def process_similarity_scores(line) :
    split_line = line.split(";")
    similarity_scores = split_line[0]
    student_names = split_line[1]
```

Now that we have the two distinct parts, lets write two functions that will 
handle both parts accordingly. We should write one function that will process
the similarity scores graph, and one function to process the student names. 
Let's define the following funtions, and call those thos functions from within
`process_similarity_scores`:

```python
# This function takes a string of the format "X=X=X...", where X is an integer
# and prints the similarity scores graph
def print_similarity_scores_graph(similarity_scores_string) :
    # implementation to follow

# This function takes a string of the format "name,name,name...", where the
# number of names might be 0 (student_names == "")
def print_student_names(student_names) :
    # implementation to follow

def process_similarity_scores(line) :
    split_line = line.split(";")
    similarity_scores = split_line[0]
    student_names = split_line[1]

    print_similarity_scores_graph(similarity_scores)
    print_student_names(student_names)
```

So, now all we have to do is impement the two new function, and our assignmet is
finished! Let's start with the first one. What should this function do? We 
defined our function to take the `5=20=22...` string as a parameter, so the
first thing this function should do is to split the string on `=`. Since we
want to print the similarity scores graph as a single string (on one line), the
best way we can go about it, is to construct it score by score. We do this
by initializing the eventual graph as an empty string, and adding each `_`, `-`,
or `^` one by one to the string as we loop through the scores. Then, at the end
of the loop, we can print our final graph.

(Also, as we see in the assignment description, our printed graph should be
indented with a TAB. We could just prepend our graph with the `\t` character,
but - since we also have to use this prefix while printing the student names - 
I think it's a bit nicer to have this prefix in a seperate constant at the top 
of the file)

Implementing the above looks as follows:

```python
# put this 'similarity score prefix' constant at the top of your file
SS_PREFIX = "\t"

def print_similarity_scores_graph(similarity_scores_string) :
    similarity_scores = similarity_scores_string.split("=")
    graph = ""
    for sim_score in similarity_scores :
        sim_score_int = int(sim_score)
        if sim_score_int == 0 :
            graph += "_"
        elif sim_score_int < 20:
            graph += "-"
        else :
            graph += "^"
    print "%s%s" % (SS_PREFIX, graph)
```

Great! Now let's move on to the last part: printing the student names. Luckily,
this is not all to difficult - in fact, it is one of the more easy tasks of this
assignment. We start our function checking whether the parameter equals `""`, 
which would mean that the part of the line *after* the ';' was empty. In this 
case, we should print `'No matches found"`. If it *isn't* empty, it means
the parameter *does* contain a string with student names, which would make us 
have to split the string on commas (`,`) to create a list of student names. Once we 
have a list of student names, we simply loop through the list and print the
names. *Don't forget to include the SS_PREFIX in all of the `print` statements
in this function as well to make our strings indented.*:

> Also, I've noticed that - in every line - the last of the student names has a
newline character (`\n`) appended to it. This isn't a *real* big deal, but it
gives us a extra newline in our output that we don't want. Therefore, I call
the `rstrip` function on the student names right before I print them. `rstrip`
strips the string of all trailing whitespace (including newlines, of course), 
and does absolutely nothing is there is none. Just makes our output a bit nicer.

```python
# This function takes a string of the format "name,name,name...", where the
# number of names might be 0 (student_names == "").
def print_student_names(student_names) :
    if student_names == "" :
        print "%sNo matches found" % SS_PREFIX
    else :
        student_names_list = student_names.split(",")
        for student_name in student_names_list :
            print "%s%s" % (SS_PREFIX, student_name.rstrip())
```

O-kayy! We're done! Only [one assignment](housemarket.md) to go!

Our finished program looks like this (I've kept the important comment in there,
they help make the program *a lot* better understandable):

```python
''' Assignment: Administration
    Created on [whenever]
    @author: [Whoever]'''

INPUT_FILE = "administration_input.txt"
SS_PREFIX = "\t"

# This function takes a string of grades seperated by spaces and return the
# average of grades as a string, since one of the posential return values is 
# '6-'
def get_grades_average(grades) :
    total = 0
    for grade in grades:
        total += float(grade)
    average = total / len(grades)
    if average >= 5.5 and average < 6 :
        return "6-"
    return "%0.1f" % (round(average * 2) / 2)

# This function takes a string of the format:
#   [Student name][a number of underscores][grades]
# and prints the student name along with the average grade
def calculate_student_final_grade(line) :
    split_line = line.split("_")
    student_name = split_line[0]

    list_len = len(split_line)
    grades_str = split_line[list_len - 1]
    grades_list = grades_str.split()
    average = get_grades_average(grades_list)
    print "%s has an average of %s" % (student_name, average)

# This function takes a string of the format "X=X=X...", where X is an integer
# and print the similarity_scores_graph
def print_similarity_scores_graph(similarity_scores_string) :
    similarity_scores = similarity_scores_string.split("=")
    graph = ""
    for sim_score in similarity_scores :
        sim_score_int = int(sim_score)
        if sim_score_int == 0 :
            graph += "_"
        elif sim_score_int < 20:
            graph += "-"
        else :
            graph += "^"
    print "%s%s" % (SS_PREFIX, graph)

# This function takes a string of the format "name,name,name...", where the
# number of names might be 0 (student_names == "").
def print_student_names(student_names) :
    if student_names == "" :
        print "%sNo matches found" % SS_PREFIX
    else :
        student_names_list = student_names.split(",")
        for student_name in student_names_list :
            print "%s%s" % (SS_PREFIX, student_name.rstrip())


# This function takes a string of the format:
#   [similarity_scores];[optional list of student names]
# and processes it accordingly
def process_similarity_scores(line) :
    split_line = line.split(";")
    similarity_scores = split_line[0]
    student_names = split_line[1]
    print_similarity_scores_graph(similarity_scores)
    print_student_names(student_names)
    

''' Start Program '''
input = open(INPUT_FILE).readlines()
for i in range(0, len(input), 2) :
    first_line = input[i]
    second_line = input[i + 1]
    calculate_student_final_grade(first_line)
    process_similarity_scores(second_line)
```