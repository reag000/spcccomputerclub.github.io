---
title: "F3 CL Python Assignment 4: Lists"
date: 2022-10-28T13:32:40+08:00
draft: false
tags: ["computer-literacy", "python"]
---

{{< lead >}} /*List: the most used complex data type in python*/ {{< /lead >}}

# What is a list?
## Data types
In Python, there are generally tow kinds of data type:  **Atomic** and **Collective**.
**Atomic** data types, as its name suggests, atomic data types cannot be further broken down. For example a *boolean* `True` or an *int* `69`.
## List
A *list* is a **collective** data type. It is made up of other atomic or collective data types. Here is an example:
```python
demo = [0, 1, 2, 3, 4] # this is an example of a list
```
Unlike many other languages, in Python you can put different kinds of data types in one single list.
```python
demo = ["computer", "club", "No." 1,] # a list made up of `str` and `int`
```
## Iterable
A *list* is an **iterable**. An iterable is any Python object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.    
```python
demo = [1, 2, 3]
for number in demo:
	print(number)
```
Output:
```
1
2
3
```
For further information, please refer to the school pdf of this lesson. Note that you can pass a number into pop() to remove an item with specific index.

# Exercise 
## Introduction
We are given a list `T` which represents temperatures of regions. Put that to your Python file first.
```python
T = [ 19.6, 18.7, 18.8, 20.1, 19.6, 19.6, 19.6, 18.2,
18.3, 18.5, 18.8, 18.8, 13.5, 17.9, 19.7, 19.1,
19, 19.3, 19.1, 18.7, 18.9, 19.7, 18.3, 18.6,
18.1, 12.8, 19, 13.6, 16, 18.4, 19.6, 17.6,
19.4, 19.7, 19.9, 19.2, 19.7, 18.6, 19.1]
```
Our job is to :
1. Evaluate the total number of regions
2. Count the number of regions with a temperature above 18.5 C.
3. Calculate the average temperature over all regions.

First think about what can we do to solve this with our previous knowledge!  

Ready?  

## 1. Total number of regions
The first one is too easy. We will just use a `len()`:
```python
total_number = len(T)
print(f"The total number of regions: {total_number}")
```
Note that we can put a `f` before the string and we can put our variable inside the curly brackets. it is equivalent to:
```python
print("The total number of regions:", len(total_number))
```

## 2. Number of regions with temp > 18.5
To count the total number of temperature above 18.5, we need to check every number in the list to check whether it is larger than 18.5 or not.  

Let's first create a variable to store our counts:
```python
count_larger = 0
```

To go through every item in the list, we can use a `for` loop. Since a list is an iterable we can put it in a `for` loop. Let's call each temperature in the list `temp`:
```python
for temp in T:
```
And finally, use a `if` to check if `temp` is larger than 18.5. If yes, we will add one to count:sum = 0
count = 0
```python
count_larger = 0
for temp in T:
	if temp > 18.5:
		count_larger += 1
print(f"Number of regions with temperature above 18.5 degC: {count_larger}")
```

Good. Now let's run the program and see if it returns 27:  
Output:
```
The total number of regions: 39
Number of regions with temperature above 18.5 degC: 27
```
## 3. Average

Now let's move to the next task.
To calculate the average of the numbers, we first have to get the sum of all the numbers. To do this, we first have to make a new variable to store the sum:
```python
sum = 0
```
What we are going to do is loop through the entire list and add each number to sum.  
Let's make a new `for` loop... Wait!  
Remember we have made a loop previously? Why not just modify that loop?
```python
sum = 0
count_larger = 0

for temp in T:
	sum += temp
	if temp > 18.5:
		count_larger += 1

print(f"Number of regions with temperature above 18.5 degC: {count_larger}")

print(f"sum: {sum}") # for testing only, should be deleted afterwards
```
Let's run the code first.  
Output:
```
The total number of regions: 39
Number of regions with temperature above 18.5 degC: 27
sum: 721.1000000000003
```
Note that the output is a bit weird. What is that `000000000003` ?
The computer club will soon publish and article about that, but now let's ignore that since it doesn't really matter.  
Next we will divide it by the total number of regions(length of the list) and round it off to 2 dp using `round()`.
```python
average = round(sum / total_number, 2) # the `2` specifies 2 decimal points
print(f"Average temperature: {average}")
```
Now everything is done. Let's run our program:  
Output:
```
The total number of regions: 39
Number of regions with temperature above 18.5 degC: 27
Average temperature: 18.49
```
## Bonus: Better ways?
Actually, we can use Python's built-in functions to simplify our program  e.g. `sum()`  returns the sum of a list.  
If you are pro enough, you can do it with one line like Nick:
```python
print(f"The total number of regions: {len(T)}\nNumber of regions with temperature above 18.5 degC: {len(list(filter(lambda x: x > 18.5, T)))}\nAverage temperature: {round(sum(T) / len(T), 2)}")
```
The `filter()` function takes two parameters. The first one is a function that returns a boolean(in this case we use a `lambda` function which receives a parameter and compare it with `18.5`). The second one is an iterable. After that `filter()` will execute the function for each item in the iterable and pass that item to the function as the parameter, and store the item into a `filter` object if it returns `True`. Next we will use `list()` to convert the object into a list.
# External
1. [Official Documentation: Built-in Python Functions](https://docs.python.org/3/library/functions.html)
2. [W3schools: Python Lists](https://www.w3schools.com/python/python_lists.asp)
