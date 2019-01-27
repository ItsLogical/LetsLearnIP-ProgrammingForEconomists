# HouseMarket

There we go - the *last* assignment.

Okay, so after reading the assignment description, we have a pretty clear way -
and order - of doing things. The description lists six steps we have to take to 
finish this assignment, so we'll just stick with that list.

> We *could*, of course, finish the in assignment any number of ways, but since
we get such a well structured list of tasks, we don't really have to think of
*another* way to do it.

Okay, so, first step: read in the `houses_sold` data.

This is something that has to be for almost all of these assignments, so I
won't really go in depth in how to solve this. If you need any more help, or
don't understand certain things in the code below, more info can be found in the
previous assignment walkthroughs. *Make sure you understand every one of them!
You need the knowledge and - more importantly - the programming experience to
to be able to finish this one*

After writing the code that reads in the `houses_sold` file, our program looks
somehting like this:

```python
''' Assignment: HouseMarket
    Created on 19 jan 2019
    @author: Whoever'''

def read_house_data_file(filename) :
    house_data = []
    file_contents_lines = open(filename).readlines()
    for line in file_contents_lines :
        split_line = line.split(';')
        size = float(split_line[0])
        price = int(split_line[1])
        house = [size, price]
        house_data.append(house)
    return house_data

''' Start Program '''
# Read in and plot the houses_sold data
houses_sold_data = read_house_data_file('houses_sold.txt')
```

*One thing to note here, is that - in contrary to the previous assignment - we
put the reading of the file in a seperate function. We do this because - a 
little bit later in this program - we will have to read in the other data file.
Since that data file has the exact same structure and format, we can simply 
reuse the input-reading code by calling that function again.*

Okay, anyway, what's next? Oh yeah, the linear regression stuff!

Now, I'll be honest with you: this is actually the most difficult part of the
assignment (for me, at least!), because will have to know *how* to calculate 
those coefficients (I didn't know how to do that by heart; sue me). So, you'll
have to have some knowledge on basic math and statistics, and if you don't have
that (like me...), you're forced to go look it on Google (or whatever)...

But, this is a *programming* course! You should learn about linear regression in
your elementary statistics courses, so I'll just hand you all the knowledge you
need.

We need to calculate a *simple linear regression* line of a bunch of (x,y) data
points. We *have* our data points, it's in the `houses_sold` variable as a list
of [`size`, `price`] values (which is also why I returned the data from the
`read_house_data_file` as I did; it makes the further calculations and plots a
lot simpler).

Okay, since we need to calculate a *line* (which, as we all know, is represented
by a formula `a + bx`), we need a *slope* (the `b`) and an *intercept* 
(the `a`). But, how do we calculate the `a` and `b`? *Let's call 'em *alpha* and
*beta* from now, it's a bit more conventional*

Not too hard actually: 
> *alpha* = *the mean of the Y values* - (*beta* * *the mean of X values*)

Calucating the means of the X and Y values is trivial, but how do we get *beta*?

> *beta* = *covariance of X and Y* / *variance of X*

Okaaaay, and how do we calculate said covariance and variance?

> covariance(X, Y) = sum_of((xi - mean of X) * (yi - mean of Y) / (N - 1)

> variance(X) = sum_of((xi - mean of X)^2) / N

Where `i = from 0 to N` and `N = length of X (or Y, same thing)`.

Okay, that might be a bunch to take in, but let's get right into implementing 
it, and you'll get it along the way.

Let's write a function that takes the data vector as an argument, and returns
the *alpha* and *beta* both at once, as a list (then, we don't need to write to
different functions to calculate both the alpha and the beta). 

We add the following to our program:

```python
''' Start Program '''
houses_sold_data = read_house_data_file('houses_sold.txt')

slr_data = get_slr_line(houses_sold_data)
alpha = slr_data[0]
beta = slr_data[1]
```

Which means we're gonna write a function `get_slr_line` which will give us the 
values we want. Let's add it just above the 'Start Program'-stuff:

```python
# Get simple linear regression line
# Takes a list of [x,y] data pairs, so the data params will look like:
#   [[x1, y1], [x2, y2], ..., [xn, yn]]
# Return the alpha and beta (as floats) of the line in a list, as:
#   [alpha, beta] 
def get_slr_line(data) :
    # implementation will go here
```

Okay, we know how to proceed from here and implement this function, so why 
aren't we? Well, there's just a tiny little thing I have to mention. *Because*,
as you might remember from my *fan-tas-tic* explanation just then on how to 
calculate everything, all those mathematical function like the `mean`, 
`covariance`, and `variance` operate on one-dimensional vectors. (Think about it,
you calculate the mean over the one-dimensional list of numbers, of course.
Like, you calculate mean of 1, 3, 4, 7, 10 as 5, and if you want to calculate 
the mean of (x, y) data pairs, you'd just be calcuating the mean *twice*. Once 
of the `x`'s, and once over the `y`'s).

So, to pass those vectors of *just* `x` values and *just* `y` values to the 
mathematical functions we'll write in a minute or so, we first have to extract
these vectors from our `data` parameter (which looks like 
`[[x1, y1], [x2, y2], ..., [xn, yn]]`).

Now, we could do something like that as follows:

```python
x = []
for x_y in data:
    x.append(x_y[0])
```

We *could*, however, since it's such a simple operation (just create a list of
all of the item on index 0 or 1), it'd be nicest if we could waste as few lines 
as possible on it. And we can! Thanks to a cool little Python feature called 
*list comprehension* (you probably won't be taught this in the course, but it's 
cool, so I'm gonna show it to you).

Basically, thanks to list comprehension, the code above can literally be 
summarized as:

```python
x = [x_y[0] for x_y in data]
```

Great! Only one line! Now, remember: the code above and the code above that, are
completely identical.

Okay, now, let's proceed with the implementation of our function using the 
knowledge we've gathered above:

```python
# Get simple linear regression line
# Takes a list of [x,y] data pairs, so the data params will look like:
#   [[x1, y1], [x2, y2], ..., [xn, yn]]
# Return the alpha and beta (as floats) of the line in a list, as:
#   [alpha, beta] 
def get_slr_line(data) :
    x = [x_y[0] for x_y in data]
    y = [x_y[1] for x_y in data]
    beta = covariance(x, y) / variance(x)
    mean_x = mean(x)
    mean_y = mean(y)
    alpha = mean_y - beta * mean_x
    return [alpha, beta]
```

This function exactly implements the logic described above. 

Now, next up is to actually implement the three mathematical/statistics 
functions. For these as well, the algorithm is explained above (except for the
*mean*, I assume you'll probably already know how to do that):

```python
def mean(x) :
    sum = 0
    for xi in x :
        sum += xi
    # cast sum to a float to avoid integer division
    return float(sum) / len(x)

# Takes vectors x and y
# Quick reminder:
#   covariance = sum_of((xi - xmean) * (yi - ymean)) / (N -1) 
def covariance(x, y) :
    mean_x = mean(x)
    mean_y = mean(y)
    n = len(x)
    sum = 0
    for i in range(0, n) :
        sum += ((x[i] - mean_x) * (y[i] - mean_y))
    # cast the sum to a float to avoid integer division
    return float(sum) / (n - 1)

# Returns the variance of a vector x as a float.
# Quick reminder:
#   variance = sum_of((xi - xmean)^2) / n
def variance(x) :
    mean_x = mean(x)
    sum = 0
    for xi in x :
        sum += ((xi - mean_x) ** 2)
    # cast sum to a float to avoid integer division
    return float(sum) / len(x)
```

Grrreat! We've come a long way. Most of the hard stuff from this assignment are
acutally done now, but there's just one thing that still might need some 
explaining, and it's also the next thing up for us to do (point 3 in the 
assignment description).

We have now - at the bottom of our file, below the 'Start Program' stuff - in 
our `houses_sold` variable the house data as `(size, price)` (i.e. `(x, y)`) 
pairs, ready to be plotted, and we have our `alpha` and `beta`, ready to be 
plotted. So let's plot them.

> How to plot these values is shown in the assignment description, but it's not
> explained at all *what* is happening exactly. More specifically, the first two 
> lines of the example code in the assignment description are probably a bit 
> strange.
> 
> See, what you're doing with that first line (`import ipy_lib`), is *importing
> a library*. It's a way for programs to import a lot of code and, therefore, a
> lot of functionality. Why would you do this? Well, it's actually *always* done
> in progamming so you don't have to write all of the code yourself. In this 
> case, writing code in Python for a window to pop up and to able to plot values
> in it can be quite hard. In fact, the `ipy_lib.py` file contains about 1500 (or 
> so) lines; imagine you'd have to write that much code each time you want to use
> some functionality it provides (okay, the `ipy_lib` contains a lot more code
> then only the stuff related to plotting and the HouseMarker assignment, but 
> still...).
> 
> In fact, for *all* of the programs you've written so far, you've probably used
> a library, you only didn't know it. The Python 'Standard Library' is 
> automatically included in every Python program. Almost everything (data types,
> string functions like `split`, file functions like `open` and `readlines`, you
> name it) are all part of the Python Standard Library.
> 
> A library will always consist of very general functionality that could be used
> by anyone. For example, the `mean`, `covariance`, and `variance` functions you
> just wrote are prime examples of functions that should go in a library. A bunch
> of people will - at some point - write a program where they need to calculate 
> these values, and why write them again (and possibly make errors in your 
> implementation) instead of reusing code that has already been written, tried, 
> and tested? (Of course, the people who created this course didn't want you
> to use a library for these functions, and wanted you to write them yourself. But
> *normally*, in any other situation, you could've/*should've* just imported a 
> library that contained these functions.)
> 
> Okay, hope you got all of that. Moving on. The second line in that example
> code (`ui = ipy_lib.HouseMarketUserInterface()`) does the following:
> 
> Inside of the `ipy_lib`, there is a `class` called `HouseMarketUserInterface`.
> Here, you simply instantiate that class into and object and store it in the `ui`
> variable. Now, the obvious problem here is that you've not been taught about
> classes and objects yet - which was a decision made by the teachers and TA's of
> this course - but *somehow* you're expected to use them.
> 
> Basically, an object is a container of variables and functions, and a class is 
> a blueprint of that container. It's (conveniently) called an *object*, because
> it is of great use to model real-world objects (in the most general definition
> of the word, i.e., *anything*). These variables (called *properties* in the 
> context of object) and functions (called *methods*) can be accessed with a dot
> ('`.`'). A (commonly used) example usage of classes and objects is the 
> following:
> 
> Say, we want to model a person in a program; we could define a class `Person`.
> A person has a number of *properties* (think of: age, name, height, weight,
> whatever, the list in inexhaustive), so our `Person` class would contain these
> properties. A person also has a number of things he/she can *do*, and these are
> modelled as methods (which are exactly the same as functions, we just call 'em
> differently for some reason). A person can exercise, for example, and that bit
> of exercise will probably have an impact in his/her weight. 
> 
> To model what we just described in Python, would look something like:
> 
> ```python
> class Person :
>     def __init__(self, name, age, height, weight):
>         self.name = name
>         self.age = age
>         self.height = height
>         self.weight = weight
> 
>     def exercise() :
>         # let's just say we live beautiful world where every time a person
>         # exercises, he/she loses 2 kilos.
>         self.weight -= 2
> ```
> 
> If we have our `Person` class defined as above, we can use it to create `Person`
> objects, which are just instantiated classes. It looks like:
> 
> ```python
> person1 = Person("John Doe", 28, 185, 85)
> print person1.weight # will print 85
> 
> person1.exercise()
> print person1.weight # will print 83
> 
> person2 = Person("Don Joe", 82, 169, 62)
> print person2.weight # will print 62
> 
> person2.exercise() 
> print person2.weight # will print 60 (and let's hope our 82 year old is still alive...)
> ```
> 
> So, that's all on objects and classes that I'll teach ya for now, it should be
> enough to understand how the stuff from the `ipy_lib` works for this assignment.
> 
> Also, you may have noticed some similarities between functions and classes,
> and if so, you're right! They're very similar, in that:
> 
> - You define something beforehand which won't execute anything at first
> - You can 'bring the function/class to life' later in your program by *calling 
> it*, or *instantiating it*, respectively.
> - You use parentheses ('`()`') to *really* use them

Okay, where were we in our program? Oh yeah, point 3 of the assignment 
description; we have to plot the regression line, and plot the houses as dots.
First, before we can plot anything, we need to import the `ipy_lib` and 
instantiate the `HouseMarketUserInterface` class inside of it. So, put this line
at the very top of your file:

```python
import ipy_lib
```

And put this line at the top of your 'Start Program' part, above anything thats
under the 'Start Program' part right now:

```python
''' Start Program '''
ui = ipy_lib.HouseMarketUserInterface()
```

Let's start with the plotting of the houses. We'll write that bit of code in a
seperate function, because we'll be needing to reuse it a bit later for the 
`houses_for_sale` data. The function we need to write should take the house 
data, the color of the dots, and the `ui` object as parameters, as it needs 
those three things to do its job.

So lets define it (somewhere above the 'Start Program' part): 

```python
# Plots a list of the form [[x1, y2], [x2, y2], ..., [xn, yn]] as dots using
# the ipy_lib's UI functions (ipy_lib's UI object is passed as the first param).
# The color param is passed directly to the plot_dot function.
def plot_house_data(ui, data, color) :
    for x_y in data :
        ui.plot_dot(x_y[0], x_y[1], color)
```

And call it at the bottom of your program:

```python
plot_house_data(ui, houses_sold_data, 'b')
```

Then, below that, we add the plotting of the line (this doesn't need to be in a
seperate function, since it's only one line, really):

```python
ui.plot_line(alpha, beta)
```

Now, if you want to run your program, and see the beauty you've created, you 
can. *But*, you shouldn't forget to add `ui.show()` at the *very* bottom of the
file (it'll take care of the actual *showing* of the plot. If you call it, you
won't see anything).

Great, now that we've done that, we can move on to points 4 and 5 of the 
description, and, whoa wait a minute! We've already done these things! Only now,
we have to do them with a different input file. Thanks to the neat way we've
structured our code, however, this is a piece of cake! (It's also a nice 
reminder of how *God damn* important it is to structure your code *neatly* and 
*logically*!)

To finish point 4 and 5, all we need to do is:

```python
# Read in and plot the houses_for_sale data
houses_for_sale_data = read_house_data_file('houses_for_sale.txt')
plot_house_data(ui, houses_for_sale_data, 'r')
```

Boom. Done. Next, on to the sixth and final task of our assignment, and we're 
fully done!

We should write some code that prints whether the houses in a house_data list 
are affordable of expensive, based on whether the majority is above or below 
a linear regression line. Let's put that functionality in a seperate function,
which will handle all of that for us:

```python

# This function does the calculation on whether the houses in the houses_data
# param are either expensive or affordable. It uses the alpha and beta params
# as the norm 
def print_houses_affordability(houses_data, alpha, beta) :
    # implementation
```

Well, logically thinking, this function should do something like:

- Loop through each 'house' in the `house_data` list
- Check for each house whether the price (the y-value) is higher than the 
`alpha + beta * x` formula
- Keep track of the amount of expensive ones vs. affordable ones
- If expensive ones > affordable ones, print something, otherwise, print 
something else

Okay, that's not too hard. The second point might be a thinker for a few 
minutes, but it's nothing more than middle school math, basically. The fourth
point, the keeping track part, I think is most simply done with one counter 
which we will increment and decrement. Saves us from keeping track of two
variables.

So to implementation looks like:

```python
def print_houses_affordability(houses_data, alpha, beta) :
    expensive_houses_counter = 0
    for house in houses_data :
        # test y > alpha + beta*x
        if house[1] > (alpha + house[0] * beta) :
            expensive_houses_counter += 1
        else :
            expensive_houses_counter -= 1
    if expensive_houses_counter > 0 :
        print "The houses are expensive"
    else :
        print "The houses are affordable"
```

Okay, now let's call it at the bottom of the program:

```python
print_houses_affordability(houses_for_sale_data, alpha, beta)
```

Great, now run it (and make sure the `ui.show()` is at the absolute bottom
of the file). Aaaand... done! Great, you're fully done, and I'm tired of writing
these walkthroughs, so I'm gonna take a rest.

The *full*, finished program looks like this (again, comments are good to leave
in for readability):

```python
import ipy_lib

''' Assignment: HouseMarket
    Created on 19 jan 2019
    @author: Whoever'''

def read_house_data_file(filename) :
    house_data = []
    file_contents_lines = open(filename).readlines()
    for line in file_contents_lines :
        split_line = line.split(';')
        size = float (split_line[0])
        price = int(split_line[1])
        house = [size, price]
        house_data.append(house)
    return house_data

def mean(x) :
    sum = 0
    for xi in x :
        sum += xi
    # cast sum to a float to avoid integer division
    return float(sum) / len(x)

# Takes vectors x and y
# Quick reminder:
#   covariance = sum_of((xi - xmean) * (yi - ymean)) / (N -1) 
def covariance(x, y) :
    mean_x = mean(x)
    mean_y = mean(y)
    n = len(x)
    sum = 0
    for i in range(0, n) :
        sum += ((x[i] - mean_x) * (y[i] - mean_y))
    # cast the sum to a float to avoid integer division
    return float(sum) / (n - 1)

# Returns the variance of a vector x as a float.
# Quick reminder:
#   variance = sum_of((xi - xmean)^2) / n
def variance(x) :
    mean_x = mean(x)
    sum = 0
    for xi in x :
        sum += ((xi - mean_x) ** 2)
    # cast sum to a float to avoid integer division
    return float(sum) / len(x)

# Get simple linear regression line
# Takes a list of [x,y] data pairs, so the data params will look like:
#   [[x1, y1], [x2, y2], ..., [xn, yn]]
# Return the alpha and beta (as floats) of the line in a list, as:
#   [alpha, beta] 
def get_slr_line(data) :
    x = [x_y[0] for x_y in data]
    y = [x_y[1] for x_y in data]
    beta = covariance(x, y) / variance(x)
    mean_x = mean(x)
    mean_y = mean(y)
    alpha = mean_y - beta * mean_x
    return [alpha, beta]

# Plots a list of the form [[x1, y2], [x2, y2], ..., [xn, yn]] as dots using
# the ipy_lib's UI functions (ipy_lib's UI object is passed as the first param).
# The color param is passed directly to the plot_dot function.
def plot_house_data(ui, data, color) :
    for x_y in data :
        ui.plot_dot(x_y[0], x_y[1], color)

# This function does the calculation on whether the houses in the houses_for_sale
# param are either expensive or affordable. It uses the alpha and beta params
# as the norm 
def print_houses_affordability(houses_data, alpha, beta) :
    expensive_houses_counter = 0
    for house in houses_data :
        # test y > alpha + beta*x
        if house[1] > (alpha + house[0] * beta) :
            expensive_houses_counter += 1
        else :
            expensive_houses_counter -= 1
    if expensive_houses_counter > 0 :
        print "The houses are expensive"
    else :
        print "The houses are affordable"


''' Start Program '''
ui = ipy_lib.HouseMarketUserInterface()

# Read in and plot the houses_sold data
houses_sold_data = read_house_data_file('houses_sold.txt')
plot_house_data(ui, houses_sold_data, 'b')

# Calculate and plot the simple linear regression line
slr_data = get_slr_line(houses_sold_data)
alpha = slr_data[0]
beta = slr_data[1]
ui.plot_line(alpha, beta)

# Read in and plot the houses_for_sale data
houses_for_sale_data = read_house_data_file('houses_for_sale.txt')
plot_house_data(ui, houses_for_sale_data, 'r')

print_houses_affordability(houses_for_sale_data, alpha, beta)

ui.show()
```