# Exam 2017 with solutions

## Question 1
```python
"""
The parameters a_list1 and a_list2 are both a list of int's. The
parameter n is an int >= 0.
The function f1() should return a new list that contains n times the
result of putting the elements of a_list2 after the elements of a_list1.

Example:
f1([1, 2], [3, 4], 3) should return [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
"""
def f1(a_list1, a_list2, n):
    return n * (a_list1 + a_list2)
```

## Question 2
```python
"""
The parameter a_list is a list of strings. Each of these strings only
contains digits.
The function f2() should return a list of int's. The first int should
be the number in the first string of a_list, the second int the number in
the second string of a_list and so on.

Example:
f2(["12", "345", "6789"]) should return [12, 345, 6789]
"""
def f2 (a_list)
    return map(int, a_list)
```

## Question 3
```python
"""
The function f3() should return a list with all the numbers
from -100 upto and including 1000 that are divisible by 5.
"""
def f3():
    return range(-100, 1001, 5)
```

## Question 4
```python
"""
The parameter a_list is a list of int's. The number of elements
in a_list is 135. The function f4() should return a new list that contains the elements
from a_list that start with the element with index 35 up to and
including the element with index 93.
"""
def f4(a_list):
    return a_list[35:94]
```

## Question 5
```python
"""
The parameter a_list is a list of int's with more than 1 element.
The function f5() should return True when the values of the elements of
a_list are decreasing and False otherwise. In other words, the second
number in a_list should be smaller than the first number, the third
number should be smaller than the second number, and so on, until the last
number which should be smaller than the second last number.

Examples:
f5([1, 2, 3, 4, 5]) should return False
f5([5, 4, 3, 2, 1]) should return True
f5([5, 4, 4, 3, 2, 1]) should return False
"""
def f5 (a_list):
    for i in range(1, len(a_list)):
        if a_list[i] >= a_list[i-1]:
            return False
    return True
```

## Question 6
```python
"""
The parameter a_str is a string. The parameter n is an int > 0.
The function f6() should return the first n characters of a_str if
a_str has a length >= n, or the empty string if a_str has a length < n.

Example:
f6("abcdef", 3) == "abc"
f6("abcdef", 30) == ""
"""
def f6 (a_str, n):
    if len(a_str) >= n:
        return a_str[:n]
    else: # len(a_str) < n
        return ""
```

## Question 7
```python
"""
The parameter a_list is a list of int's. The parameter n is an int.
The function f7() should return a new list that contains all the values
from a_list that are bigger or equal than n. The elements in the
returned new list should be in the same order as in a_list

Examples:
f7([1, 2, 3, 1, 2, 1, 8], 2) should return [2, 3, 2, 8]
f7([4, 5, 6, 7, 8], 12) should return []
"""
def f7 (a_list, n):
    result = []
    for value in a_list:
        if value >= n:
            result.append(value)
        return result
```

## Question 8
```python
"""
The parameter n is an int and n > 0.
The function f8() should return the biggest seventh power that is not
bigger than n.

Example:
f8(10000) should return 2187 as 3**7 == 2187 (and is not bigger
than 10000) and the next 7th power, 4**7 == 16384, is bigger than 10000.
"""

def f8 (n):
    i = 0
    seventh_power = i ** 7
    while (i+1) ** 7 <= n:
        i += 1
        seventh_power = i ** 7
    return seventh_power
```

## Question 9
```python
"""
The parameter a_list is a list of int's. The parameter n is an int.
The function f9() should return a list that contains (exactly once)
each number in a_list that occurs n times in a_list.

Example:
f9([1, 1, 7, 7, 7, 3, 3, 3, 4, 4, 5, 5], 3) should return [7, 3]
(as 7 and 3 are the only numbers that occur 3 times in a_list)
"""
def f9 (a_list, n):
    result = []
    for number in a_list:
        if a_list.count(number) == n and not number in a_list:
            result.append(number)
    return result
```

## Question 10
```python
"""
The parameter a_list is a list of strings. The parameter c is
a character (a string with one element).
The function f10() should return a new list that contains all the
elements from a_list that contain the character c or end with that
character.

Examples:
f10(["aap", "noot", "mies", "polo"], "o") should return ["noot", "polo"]
f10(["aap", "noot", "mies:, "aan"], "n") should return ["noot", "aan"]
f10(["aap", "noot", "mies", "aan"], "q") should return []
"""
def f10(a_list, c):
    result = []
    for element in a_list:
        if c in element:
            result.append(element)
    return result
```

## Question 11
```python
"""
The parameter a_dict is a dictionary with strings as keys and int's as
corresponding values. The parameter n is an int.
The function f11() should return a list with all the strings whose
corresponding value is not bigger than n.

Example:
f11({"Klaas":18,"Remco":19, "Maria":20, "Lea":18}, 18)
should return ["Klaas", "Lea"]
f11({"Klaas":18,"Remco":19, "Maria":20, "Lea":18}, 10)
should return []
"""
def f11 (a_dict, n):
    result = []
    for key in a_dict.keys():
        if a_dict[key] <= n:
            result.append(key)
    return result
```

## Question 12
```python
"""
The parameter a_list is a list of int's. All elements of a_list have a
different value. The parameter n is an int > 1.
The function f12() should remove (if possible) the nth smallest element
from a_list and sort a_list. The new value of a_list should be returned
as the function result.

Example:
f12([8, 7, 6, 5, 4], 2) should return [4, 6, 7, 8]
f12([4, 8, 5, 7, 6], 3) should return [4, 5, 7, 8]
f12([4, 5, 8, 6, 7], 13) should return [4, 5, 6, 7, 8]
"""
def f12 (a_list, n):
    a_list.sort()
    if len(a_list) >= n: # a_list contains an nth smallest element
        nth_smallest = a_list[n-1]
    a_list.remove(nth_smallest)
    return a_list
```

## Question 13
```python
"""
The parameter a_list is a list of strings. The parameter s is a string.
The parameter n is an int >= 0.
Assume there are m (m>=0) elements in a_list that contain s as a substring.
If m>=n, the function f13() should create and return a new list by removing
the first n elements of a_list that contain s as a substring.
If m<n, the function f13() should create and return a new list by removing
all elements of a_list that contain s as a substring.

Example:
f13(["aap", "noot", "mies", "baard", "wim", "teun", "aal"], "aa",2)
should return ["noot", "mies", "wim", "teun", "aal"]
f13([], "abc", 3) should return []
f13(["ab", "abc", "abcd", "abcde"], "ab", 4) should return []
"""
def f13 (a_list, s, n):
    result = []
    count = 0
    for element in a_list:
        if not s in element:
            result.append(element)
        else:
            count += 1
            if count > n:
                result.append(element)
    return result
```

## Question 14
```python
"""
The parameter book is a string that contains the text of a book. The
parameter message is a string that contains a text.
The function f14() should encode the text in message and thus create an
encoded message and return that encoded message. The encoding should be
done with a book code. To explain how a book code works we will give
an example with a really short book that only contains the sentence
"Python is a very popular scripting programming language.\n" and a
(also) short message "school".
Using a book code to encode a text is done by replacing each character

in the message with a location of the same character in the text of the
book. The searching for the first character in the message ("s" in the
example) should start at the beginning of the book. In the example the first
time "s" is found is on the index position 8 of the string that contains the
text of the book. So this "s" is encoded with 8. Searching for each following
character of the message in the book is done to the right of the last
character used from the book. So the "c" becomes 26, and the first
"o" (of "school") becomes 37. When, while searching for the next character in
the book, the end of the book is reached, the search continues from the
beginning of the book. So the second "o" of "school" is encoded with 4
and the "l" is encoded with 47. the completed encoded message for the
example is [8, 26, 37, 4, 47].
You can assume that all characters in the message can be found in the book.

Examples:
f14("Python is a very popular scripting programming language.\n", "school")
should return [8, 26, 37, 4, 47]
f14("abcde", "edca"] should return [4, 3, 2, 1, 0]
f14("acabc", "aacbc"] should return [0, 2, 4, 3, 4]
"""
def f14(book, message):
    result = []
    start = 0
    for char in message:
        if book[start:].find(char) == -1:
            start = 0
            code = book[start:].find(char)
            start = code + 1
        result.append(code)
    return result
```