# Exam 2015 with solutions

## Question 1
```python
"""
The parameters a_list1 and a_list2 are both a list of int's.
The function f1() should return a new list that contains all the
elements of a_list1 followed by all the elements of a_list2.

Example:
f1([1, 2], [3, 4]) should return [1,2,3,4]
"""
def f1(a_list1, a_list2):
    return a_list1 + a_list2

def f1_v2(a_list1, a_list2):
    a_list1.extend(a_list2)
    return a_list1

def f1_v3(a_list1, a_list2):
    for i in a_list2:
        a_list1.append(i)
    return a_list1
```

## Question 2
```python
"""
The parameter an_int is an int. The parameters a_bool2 and
a_bool3 both is a boolean.
The function f2() should return True if
- an_int is even and a_bool3 is true
or if
- a_bool2 and a_bool3 are both not true
If the function f2() cannot return True, it should return False

Example:
f2(5, True, False) should return False
"""
def f2 (an_int, a_bool2, a_bool3):
    return (an_int % 2 == 0 and a_bool3) or \
    (not a_bool2 and not a_bool3)

def f2_v2(an_int, a_bool2, a_bool3):
    if an_int % 2 == 0 and a_bool3:
        return True
    if not a_bool2 and not a_bool3:
        return True
    return False

def f2_v3(an_int, a_bool2, a_bool3):
    if an_int % 2 == 0 and a_bool3 == True:
        return True
    if a_bool2 != True and a_bool3 != True:
        return True
    return False
```

## Question 3
```python
"""
The function f3() should return a list with all the numbers from
17000 upto and including 34000 that are divisible by 17.
"""
def f3():
    return range(17000, 34001, 17)

# The hard way
def f3_v2():
    result_list = []
    for i in range(17001):
        if i%%17 == 0:
            result_list.append(i+17000)
    return result_list
```

## Question 4
```python
"""
The parameter a_list is a list of int's. The number of elements
in a_list is 100.
The function f4() should return a new list that contains the 31st
element from a_list upto and including the 88th element of a_list.
"""
def f4(a_list):
    return a_list[30:88]

def f4_v2(a_list):
    result_list = []
    for i in range(30, 88):
        result_list.append(a_list[i])
    return result_list
```

## Question 5
```python
"""
The parameter a_list is a list of int's.
The function f5() should return the sum of the squares
of the elements of a_list

Example:
f5([1, 2, 3, 4, 5]) should return 55
(as 1 + 4 + 9 + 16 + 25 = 55)
"""
def f5(a_list):
    result = 0
    for number in a_list:
        result += number ** 2
    return result

def f5_v2(a_list):
    result = 0
    for (i in range(len(a_list)):
        result += a_list[i] * a_list[i]
    return result
```

## Question 6
```python
"""
The parameter a_str is a string. The parameter n is an int
The function f6() should return the first n characters of a_str if
a_str has a length >= n, or the empty string if a_str has a length < n

Example:
f6("abcdef", 3) == "abc"
f6("abcdef", 30) == ""

"""
def f6(a_str, n):
    if len(a_str) > n:
        return a_str[:n]
    return ""

def f6_v2(a_str, n):
    if len(a_str) > n:
        return a_str[0:n]
    else:
        return ""
```

## Question 7
```python
"""
The parameter a_list is a list of int's. The parameter n is an int.
The function f7() should return a new list that contains all the
values from a_list that are not equal to n.

Examples:
f7([1, 2, 3, 1, 2, 1, 2], 2) should return [1, 3, 1, 1]
f7([4, 5, 6, 7, 8], 2) should return [4, 5, 6, 7, 8]
"""
def f7(a_list, n):
    result_list = []
    for i in a_list:
        if i != n:
            result_list.append(i)
    return result_list

def f7_v2(a_list, n):
    result_list = []
    for i in a_list:
        if not i == n:
            result_list.append(i)
    return result_list

def f7_v3(a_list, n):
    while n in a_list:
        a_list.remove(n)
    return a_list
```

## Question 8
```python
"""
The parameter n is an int and n > 0.
The function f8() should return the smallest fifth power that is
bigger than n.

Example:
f8(10000) should return 16807 as 6 ** 5 == 7776 (and is not bigger
than n) and the next 5th power, 7 ** 5 == 16807, is bigger than n.
"""
def f8(n):
    for i in range(n):
        pow = i**5
        if pow > n:
            return pow

def f8_v2(n):
    i = 0
    while i**5 < n:
        i+=1
    return i**5
```

## Question 9
```python
"""
The parameter a_list is a list of int's. The parameter n is an int.
The function f9() should return a list that contains exactly one of
each of the numbers in a_list that occurs exactly n times in a_list.

Example:
f9([1, 7, 7, 3, 3, 3, 4, 4, 5], 2) should return [7, 4] (as 7
and 4 are the only numbers that occur exactly 2 times in a_list)
"""
def f9(a_list, n):
    result_list = []
    for i in a_list:
        if a_list.count(i) == n:
            if not i in result_list:
                result_list.append(i)
    return result_list
```

## Question 10
```python
"""
The parameter a_str is a string. The function palindrome() should return
True if a_str is a palindrome. A string is a palindrome when you see
the same characters, in the same order, when you walk through the characters
from left to right as when you walk through them from right to left.

Example:
palindrome("parterretrap") should return True
palindrome("abcda") should return False
palindrome("aabaa") should return True
"""

def palindrome(a_str):
    return a_str == a_str[::-1]

def palindrome_v2(a_str):
    for i in range(len(a_str)):
        if a_str[i] != a_str[-(i+1)]:
            return False
    return True
```

## Question 11
```python
"""
Add parameters to the function f11() in such a way that this function
can be called with two int arguments, for instance f11(8, 34).
You can assume that when the function f11() is called, the first
argument is always smaller than the second argument.
The function f11() should return the product of
all the numbers x, with the first argument <= x and x <= second argument.

Example:
f11(3, 6) should return 360 (3 * 4 * 5 * 6)
f11(8, 24) should return 123104841613737984000 (8 * 9 * ... * 24)
"""
def f11(x, y):
    result = 1
    for i in range(x, y+1):
        result *= i
    return result
```

## Question 12
```python
"""
The parameters start and n are both int's. Furthermore n > 0.
The function f12() should return a list of int's that contains n
Elements. The first element (e) in the resulting list has to be start.
The successor of an element e is calculated as follows:
- if e is a threefold (e.g. n is divisible by 3),
then the next e is e / 3
- if e is not a threefold, then the next e is e + 7

Example:
f12(1, 5) should return [1, 8, 15, 5, 12]
f12(7, 11) should return [7, 14, 21, 7, 14, 21, 7, 14, 21, 7, 14]
"""
def f12(start, n):
    result = []
    for i in range(n):
        result.append(start)
        if start % 3 == 0:
            start /= 3
        else:
            start += 7
        result.append(start)
    return result
```

## Question 13
```python
"""
The parameter n is an int with value > 0.
The row of Fibonacci numbers is defined as
1 1 2 3 5 8 13 21 34 55 89 ........
The first two number are defined to be 1, all the next numbers are calculated
by adding the two previous numbers (1+1==2, 1+2==3, 2+3==5, .....).
The function fibonacci() should return a list with the first n numbers of the
row of Fibonacci.

Examples:
fibonacci(1) should return [1]
fibonacci(8) should return [1, 1, 2, 3, 5, 6, 13, 21]
"""
def fibonacci(n):
    if n == 1:
        return [1]
    if n == 2:
        return [2]

    result = [1,1]
    for i in range(n-2):
        end = result[-1] + result[-2]
        result.append(end)
    return result
```

## Question 14
```python
"""
The parameter text is a string containing words separated by
spaces. Every word only contains letters in lower case. The parameter
n is an int with a minimum value of 1.
The function f14() should return True if the number of words with a
length > n is smaller than the number of words that don't have a
length > n.

Examples:
f14("de het even groot geweldig ongelooflijk", 5) should return True
(as the number of words with length > n is 2, and the number of words
which don't have a length > n is 4)

f14("de het even groot geweldig ongelooflijk", 2) should return False
(as the number of words with length > n is 5, and the number of words
which don't have a length > n is 1)
"""
def f14(text, n):
    bigger = 0
    other = 0

    for word in text.split():
        if len(word) > n:
            bigger+=1
        else:
            other+=1
    return bigger < other
```