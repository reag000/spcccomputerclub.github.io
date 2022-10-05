---
title: "Python Assignment 1: Introduction to Python"
date: 2022-10-02T14:41:09+08:00
draft: false
math: true
---

{{< alert >}}
This note is not meant to be complete! Please read through the CL note before reading this supplementary note.
{{< /alert >}}

## What is Python? Why Python?

Python is a powerful scripting language. Pythonists use it to script games and web scrapers and automate works. Data scientists use it for scientific computation, data analysis and visualisation, for instance, Big Data. Many professionals and researchers use it to build neural network and do machine learning. 

![Social Network Analysis Visualization](https://upload.wikimedia.org/wikipedia/commons/9/9b/Social_Network_Analysis_Visualization.png "By Martin Grandjean, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons")

![maze2](https://i.im.ge/2022/10/04/1VJIwq.maze2.png "Solving a maze: The red square is the starting point, and green square is the goal. The optimal path is found by searching through all possible paths 'simultaneously'")

![3b1b manim](https://raw.githubusercontent.com/3b1b/manim/master/logo/graph.png 
"Math animation created with manim, a python package: [3b1b/manim](https://github.com/3b1b/manim)")

Python is also easy to learn. Let's compare it syntax to other languages:

```python
# python
print('Hello, World!')
```

```cpp
// C++
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

```java
// java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Python definitely looks easier to learn. It is beginner-friendly as well as you can explore the language in its interactive mode. For those who want to know more, Python as a 'glue language' can be easily embeded in `C/C++` codes (to make life easier) and has a nice community providing you the glues (tons of packages!). Check this [awesome list](https://github.com/vinta/awesome-python) to see all the awesome things you can do with Python!

Python has a rich history as well. For more, pleas read: [Wikipedia: Python](https://en.wikipedia.org/wiki/Python_(programming_language)#:~:text=Python%20was%20conceived%20in)

[python.org](https://www.python.org/) has a nice appetizer to python as well: [1. Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)

### Installation of Python

Setting up the environment is genuinely easy if you have followed the guide step by step. However, if you have any difficulties in installing Python or using the editor, feel free to contact us or the [Cyber Ambassadors](https://www.instagram.com/spcccyberambassadors/)!

## An Informal Introduction to Python

### TL;DR One

{{< youtube x7X9w_GIm1s >}}

### Longer One

```python
print('Hello, World!') # Say 'Hello, World!' whenever you learn a new programming language
```

A 'Hello, World!' program is such a tradition, that it is always used as a sanity check and to expose the beginners with the language's basic syntax. We should learn Python from first analysing this simple program. Try to run this line of code in your shell/ editor.

Here, `print` is a Python built-in function. You can call a Python built-in function anywhere. To call a function, you must also supply a pair of brackets, where in between you can supply the arguments, which are just inputs for a function. A `print` function outputs whatever `string` (characters enclosed in quotation marks e.g., `'this is a string'`) you supply as an argument on the screen. Some functions also return a value when you call it, like the built-in `input` function returns whatever the user typed as a `string`.

The line after `'#'` is a comment. Comments are not actual code; they don't instruct computers, they instruct humans. Always write comments to give yourself (and others) hints, or you will typically forget everything after 3 days!

![hello_world](https://i.im.ge/2022/10/04/1f2RX8.hello-world.png)

## Basics

### TL;DR

{{< youtube I2wURDqiXdM >}}

### Variables and Values

In Python, a **variable** has a **type** and stores a **value**. Like in mathematics, we let $x = 2$, $y = 3$, $z = x + y$, we can define variables in Python.

```python
computer_club = "the best club in spcc"
year = 2022
```

Here `computer_club` and `year` are the variables, and `'the best club in spcc'` and `2022` are the values. We assign the values to the variables with the **operator** `=`.
So the basic syntax:

Note that in Python, the type of a variable is determined by the value!

{{< alert >}}
Python is a **dynamically-typed** language!
```python
computer_club = "the best club in spcc"
```
Now `computer_club` has the **type** of a `string`.

```python
computer_club = 2022
```
In the same program, you can always assign whatever values you want to a variable, and thus changing its type! Now, `computer_club` has the **type** of an `int` (integer type; should be self-evident enough)

Always keep in mind the **type** and **value** of a variable at any moment.
{{< /alert >}}

### Naming of Variables

Variables are identified by their names, and these identifiers have to be recognizable by Python. Rules for naming variables:

1. Start the variables names with either an underscore '_' or an letter; do not start with a number
2. A variable name can only contain letters, numbers or underscores
3. Variable names are case-sensitive: `vArIaBLE` is not equivalent to `VaRiAble`

Some general suggestive rules for naming variables:

1. The name should be descriptive: a name like `count_fish` is better than just `n`
2. Follow the convention: for now, the variable name should be in lowercase and each word should be separated by an underscore

Name your variables consistently! You don't want to search through a mess!

### Why is the Type so Important?

The **type** determines what you can do on a **value** or a **variable** (yeah a value has a type as well). You can do arithemetics on integers, but of course you can't do the same thing on strings (recall that strings are just basically characters). This is why we have to differentiate and pay attention to the types.

```python
print(1 + 2) # It makes sense
print(100 + 'THIS MAKES NO SENSE') # Adding numbers to characters definitely make no snese; or say, it is ambiguous
```

### Many Many More Types

```python
print(type(123)) # <class 'int'>
print(type(3.14156)) # <class 'float'>; this is basically just decimal numbers
print(type(True)) # <class 'bool'>; True and False
print(type('Computer club is the best club in spcc')) # <class 'str'>; this is the string type we have been talking about
print(type([1, 2, 3])) # <class 'list'>
print(type((1, 2, 3))) # <class 'tuple>
print(type({1, 2, 3})) # <class 'set'>
```

### Tips on Arithmetics

There are many arithmetics you can do on `int` and `float`, like `+` `-` `*` `/` `//` `**` `%`.

Just remember: whenever you want to write something like $a(b + c)$ in mathematics, please type `a * (b + c)` in your actual code.

### Type Conversion!

{{< alert >}}
Be careful and do not do:

```python
number = input('Enter a number: ')
print(number + 3) # number is a string! Be careful! This addition is an error
```

{{< /alert >}}

Python does not do extra work for you! You must convert a `string` to an `int` before you can do arithmetic, like:

```python
# these type-conversion functions are easy to remember: just remember how python calls these types!
number = int(input('Enter a number: '))
print(number + 3)
```
