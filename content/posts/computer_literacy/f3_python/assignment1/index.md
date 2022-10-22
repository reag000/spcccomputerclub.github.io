---
title: "F3 CL Python Assignment 1: Introduction to Python"
date: 2022-10-07T14:30:06+08:00
draft: false
math: true
tags: ["python", "computer-literacy"]
---

{{< lead >}} An Introduction to Python: A Powerful Programming Language {{< /lead >}}

## What is Python? Why Python?

### Powerful

Python is a powerful scripting langugae. You can use it to create games, web scrapers and automate works. You can use it to build softwares and web applications. You can use it for scientific computation and data analysis. You can use it for machine learning and deep learning. Being the third most popular language, it is so useful that over 40% of the developer respondents use it in their routine development in 2021, according to Stack Overflow's annual developer survey[[1]](https://insights.stackoverflow.com/survey/2021#most-popular-technologies-language-prof).

![maze2](https://i.im.ge/2022/10/04/1VJIwq.maze2.png "Using python to solve a maze and visulaize the path")

![3b1b manim](https://raw.githubusercontent.com/3b1b/manim/master/logo/graph.png 
"Math animation rendered with a python package [3b1b/manim](https://github.com/3b1b/manim)")

### Easy to Learn; Elegant to Write

Python has a much easier syntax compared to other programming languages. Below we show a program that prints 'Hello, World!' on the screen written in three different languages: [Python](https://en.wikipedia.org/wiki/Python_(programming_language)), [Java](https://en.wikipedia.org/wiki/Java_(programming_language)), and [C++](https://en.wikipedia.org/wiki/C%2B%2B).

```python
# Python hello_world.py
print('Hello, World!')
```

```c++
// C++ hello_world.cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

```java
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

You can always write fewer lines of code with Python. Here we quote the [The Zen of Python](https://peps.python.org/pep-0020/)-try to run this easter egg (of course later)!

```python
# Copy the following line of code and run it in the iteractive mode:
import this
```

## Installing Python

1. Go to the [Python official website](https://www.python.org/). Your browser should show the latest version for your OS by default. The latest release for both Windows and macOS is Python 3.10.7.

[![python_installation_1](https://i.im.ge/2022/10/07/1v7kOh.python-installation-1.png)](https://im.ge/i/1v7kOh)

2. Open the python-3.10.7 `.exe` or `.pkg` installer. The installer comes with **IDLE** (the Python integrated development environment), the code editor you will be using, and **pip**, a Python third-party package manager. Click continue and agree to the license. Install it in the default disk.

[![python_installation_2](https://i.im.ge/2022/10/07/1vDE7q.python-installation-2.png)](https://im.ge/i/1vDE7q)

3. After installing Python, go to the terminal:

{{<youtube aKRYQsKR46I>}}

{{<youtube 2dsnwlnNBzs>}}

In the terminal, enter the following commands line by line:

```
python3 --version
pip3 --version
```

These two commands show the versions of Python and pip. Verify no error is shown. Please use `python3` and `pip3` explicitly in the future even if the command `python` or `pip` works as well (use `python` and `pip` if and only if you have added Python 3.10 to PATH). Suppose there is any error, please approach us or the [Cyber Ambassadors](https://www.instagram.com/spcccyberambassadors/) or your CL teachers asap!

[![python_installation_3](https://i.im.ge/2022/10/07/1vinbr.python-installation-3.png)](https://im.ge/i/1vinbr)

## Using IDLE

**IDLE** (the Python Development and Learning Environment) is an editor came bundled with the installation of Python. Although there are other IDEs (integrated development environments) on the market, but the functions IDLE provides are sufficient for beginners.

Firstly, you should find the IDLE.app/exe. It should locate in the folder Python 3.10.

[![idle_1](https://i.im.ge/2022/10/07/1v0uhJ.idle-1.png)](https://im.ge/i/1v0uhJ)

### Interactive Mode

By default, IDLE is opened in **shell mode** (**interactive mode**). This is the best playground for testing any Python code snippets.

[![idle_shell_1](https://i.im.ge/2022/10/07/1v0W0a.idle-shell-1.png)](https://im.ge/i/1v0W0a)

In the shell mode, you start a Python command after a prompt (`>>>` or `...`). We should immediately go into some examples such that you can grasp the basic expressions in Python on your own. Try out the following commands in interactive mode.

#### Expressions

The following commands are some mathematical expressions in Python. The syntax is pretty straight-forward: if you know arithmetic, you have already mastered this part! You may want to pay attention to difference between the operators `/` and `//`. Try to evalute the expressions `4 / 3` and `4 // 3` in the shell. What is the result?

```python
# Only enter the commands AFTER the prompt >>>
>>> 1 + 1 # Addition
>>> 2 - 1 # Subtraction
>>> 3 * 3 # Multiplication
>>> 10 / 3 # Division
>>> (50 - 5*6) // 4 # // Integer division
>>> 8 ** 2 # 8 square
>>> 17 ** 34 # 17 to the power 34
>>> 7 % 3 # Modulus operator: returns the remainder after 7 is divided by 3
```

[![idle_shell_2](https://i.im.ge/2022/10/07/1v5QDY.idle-shell-2.png)](https://im.ge/i/1v5QDY)

#### Variables and Values

You can use the equal operator (`=`) to assign a **value** to a **variable**. No result is displayed afterwards before the next prompt.

```python
# Find the volume of a pyramid
>>> height = 10
>>> base_length = 5
>>> base_width = 8
# Variables can be ASSIGNED at the left hand side of =, 
# they are EVALUATED to their VALUES at the right hand side of =, and anywhere else
>>> volume = (height * base_length * base_width) / 3
>>> volume # This evaluates the variable volume and displays the result
```

[![idle_shell_3](https://i.im.ge/2022/10/07/1J4gnq.idle-shell-3.png)](https://im.ge/i/1J4gnq)

You can assgin values to a variable any times. Once you assign a new value to a variable, the original value is 'thrown away' and you cannot access to it anymore. In the following example, we assign the numbers 1-10 to the same variable and print it out on the screen.

```python
>>> x = 1
>>> # While x is smaller than or equal to 10, we first evaluate x, then
>>> # assign the value x + 1 to the variable x, and continue the iteration
>>> while x <= 10:
...     x # The indent is essential
...     x += 1
```

[![idle_shell_4](https://i.im.ge/2022/10/08/1Bqs4F.idle-shell-4.png)](https://im.ge/i/1Bqs4F)

##### Exercises

1. In Python expressions, approximate $\pi$ with:

$$
\pi = \frac{9801}{2206\sqrt{2}}
$$

To compute the square root of a number, try:

```python
>>> from math import sqrt
>>> sqrt(2)
```

[![sqrt_2](https://i.im.ge/2022/10/09/1GLsEr.sqrt-2.png)](https://im.ge/i/1GLsEr)

For the very mathematical-inclined, see [Ramanujan–Sato series](https://en.wikipedia.org/wiki/Ramanujan%E2%80%93Sato_series).

2. Assign a value to the variable `radius`, and assign values to the variables `perimeter` and `area` given that:

$$
perimeter = 2 \times pi \times radius
$$

$$
area = \pi \times radius^2
$$

You can get the constant $\pi$ by:

```python
>>> from math import pi
>>> pi
```

[![math_pi](https://i.im.ge/2022/10/09/1GL8dD.math-pi.png)](https://im.ge/i/1GL8dD)

3. For a set of simultaneous equations

$$
ax + by = e
$$

$$
cx + dy = f
$$

where $x$ and $y$ are variables and the remainings are constants. The roots are given by:

$$
x = \frac{ed - bf}{ad - bc}
$$

$$
y = \frac{af - ec}{ad - bc}
$$

Assign values to $a-f$, and compute the variables $x$ and $y$.

#### Strings

[Strings](https://en.wikipedia.org/wiki/String_(computer_science)) are sequences of characters, in other words, text. Strings are enclosed in either single quotes `'...'` or double quotes `"..."`. Do not mix single and double quotes together. Try out the following examples:

```python
>>> "Computer Club is the best club in spcc"
>>> 'Computer Club is the best club in spcc'
```

[![strings](https://i.im.ge/2022/10/09/1GUXLa.strings.png)](https://im.ge/i/1GUXLa)

In interactive mode, Python print strings with the quotes. To produce a more readable version, try:

```python
>>> print('Computer Club is the best club in spcc')
```

[![print_strings](https://i.im.ge/2022/10/09/1GUlxJ.print-strings.png)](https://im.ge/i/1GUlxJ)

Strings can be concatenated (joined together) with the `+` operator:

```python
>>> 'Computer Club'
>>> ' is the best club in spcc'
>>> 'Computer Club' + 'is the best club in spcc'
>>> print('Computer Club' + ' is the best club in spcc')
```

[![string_concatenate](https://i.im.ge/2022/10/09/1GhLhG.string-concatenate.png)](https://im.ge/i/1GhLhG)
