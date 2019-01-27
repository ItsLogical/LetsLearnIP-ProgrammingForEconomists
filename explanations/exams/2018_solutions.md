# Exam 2018 with solutions

## Question 1
```python
"""
The parameters a_list1 and a_list2 are both a list of int's. The
parameter n is an int >= 0.
The function f1() should return a new list that contains n times the
concatenation of a_list1 and a_list2.

Example:
f1([1, 2], [3, 4], 3) should return [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
f1([1], [7], 3) should return [1, 7, 1, 7, 1, 7]
"""
def f1(a_list1, a_list2, n):
    result = []
    for i in range(n):
        result.extend(a_list1)
        result.extend(a_list2)
    return result

def f1_v2(a_list1, a_list2, n):
    result = []
    for i in range(n):
        result += a_list1
        result += a_list2
    return result
```

## Question 2
```python
"""
The function f2() should return a list with all the numbers from
20 up to and including 5003 that are divisible by 20.
"""
def f2():
    return range(20, 5004, 20)
```

## Question 3
```python
"""
The parameter a_list is a list of int's. The number of elements
in a_list is 100.
The function f3() should return a new list that contains the elements
from a_list starting with the element on index 45 up to and including
the 55th element.
"""
def f3(a_list):
    return a_list[45:55]
```

## Question 4
```python
"""
The parameter a_str is a string. The parameter n is an int > 0.
The function f4() should return the last n characters of a_str if
a_str has a length >= n. If a_str has a length < n an empty string
should be returned.

Examples:
f4("abcdef", 3) == "def"
f4("abcdef", 30) == ""
"""
def f4(a_str, n):
    if len(a_str) >= n:
        return a_str[-n:]
    return ""

def f4_v2(a_str, n):
    if len(a_str) >= n:
        return a_str[len(a_str)-n:len(a_str):1]
    else:
        return ""
```

## Question 5
```python
"""
The parameter a_list is a list of int's. The parameter n is an int >= 0.
The function f5() should return a new list that contains all the values
from a_list that are bigger than n to the power 2 or smaller than n module 11.

Examples:
f5([500, 400, 300, 200, 100, 0], 20) should return [500, 0]
f5([226, 225, 3, 4], 15) should return [226, 3]
"""
def f5(a_list, n):
    result = []
    for i in a_list:
        if i > n**2 or i < n%11:
            result.append(i)
    return result
```

## Question 6
```python
"""
The parameter a_str is a string of length >= 0.
The function f6() should return the number of lower case letters in a_str.

Example:
f6("B-34;aJK+]>") should return 1 as "a" is the only lower case letter in the string.
"""
def f6(a_str, n):
    total = 0
    for i in a_str:
        if ord(i) >= ord("a") and ord(i) <= ord("z"):
            total += 1
    return total
```

## Question 7
```python
"""
The parameter a_list is a list of int's.
The function f7() should return a list of which all the elements
are slices of a_list. The first slice should be a list that
contains the first element of a_list. The second slice should be
a list that contains the first two elements of a_list and so on until
the last slice that should contain all the elements of a_list.

Examples:
f7([11, 12, 13, 14]) should return
[[11], [11, 12], [11, 12, 13], [11, 12, 13, 14]]
"""
def f7(a_list):
    result = []
    for i in range(len(a_list)):
        result.append(a_list[0:1+i])
    return result
```

## Question 8
```python
"""
The parameter a_list is a list of int's. The parameter n is an int > 0.
The function f8() should return the amount of different elements that
are exactly n times in a_list.

Example:
f8([1, 2, 3, 4, 5], 1) should return 5
(As the five numbers 1, 2, 3, 4, and 5 are each exactly 1 time in the list.)
f8([1, 3, 3, 5, 5, 7, 7, 9], 2) should return 3
(As the three numbers 3, 5 and 7 are each exactly 2 times in the list.)
f8([2, 2, 2, 2, 2], 5) should return 1
(As only the number 2 is exactly 5 times in the list.)
"""
def f8(a_list, n):
    done = []
    for i in a_list:
        if a_list.count(i) == n and not i in done:
            done.append(i)
    return len(done)
```

## Question 9
```python
"""
The parameter text is a string containing words seperated by
spaces. Every word only contains letters in lower case. The
parameter a_str is a string that only contains letters in lower case.
The function f9() should return the number of words in text that
contain a_str as a substring.

Examples:
f9("derde dergelijke wit zwart", "der") should return 2
(As the words "derde" and "dergelijke" each contain "der" as a substring.)
"""
def f9(text, a_str):
    total = 0
    for word in text.split():
        if a_str in word:
            total += 1
    return total
```

## Question 10
```python
"""
The parameter a_dict is a dictionary with int's as keys and float's as
corresponding values. The parameter n is an int.
The function f10() should return the average of all the float-values that
have a key that is not bigger than n.
If there are no such keys, the function f10() should return -1.0

Example:
f10({1: 2.0, 2: 3.0, 5: 7.0}, 4) should return 2.5
(As the keys 1 and 2 are not bigger than 4, their corresponding values
 are 2.0 and 3.0 and the average of 2.0 and 3.0 is 2.5)
"""
def f10(a_dict, n):
    average_list = []
    for i in a_dict.keys():
        if i <= n:
            average_list.append(a_dict[i])

    return sum(average_list)/len(average_list)
```

## Question
```python

```

## Question
```python

```

## Question
```python

```

## Question
```python

```

## Question
```python

```

## Question
```python

```