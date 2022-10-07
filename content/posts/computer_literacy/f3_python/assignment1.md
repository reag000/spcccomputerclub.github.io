---
title: "F3 CL Python Assignment 1: Introduction to Python"
date: 2022-10-07T14:30:06+08:00
draft: false
math: true
---

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

These two commands show the versions of Python and pip. Verify no error is shown. Please use `python3` and `pip3` explicitly in the future even if the command `python` or `pip` works as well. Suppose there is any error, please approach us or the [Cyber Ambassadors](https://www.instagram.com/spcccyberambassadors/) or your CL teachers asap!

[![python_installation_3](https://i.im.ge/2022/10/07/1vinbr.python-installation-3.png)](https://im.ge/i/1vinbr)

## Using IDLE

**IDLE** (the Python Development and Learning Environment) is an editor came bundled with the installation of Python. Although there are other IDEs (integrated development environments) on the market, but the functions IDLE provides are sufficient for beginners.

First, find the IDLE.app/exe. It should locates in the folder Python 3.10.

[![idle_1](https://i.im.ge/2022/10/07/1v0uhJ.idle-1.png)](https://im.ge/i/1v0uhJ)

By default, IDLE is opened in **shell mode** (**interactive mode**).

[![idle_shell_1](https://i.im.ge/2022/10/07/1v0W0a.idle-shell-1.png)](https://im.ge/i/1v0W0a)

In the shell mode, you start a Python command after a prompt (`>>>` or `...`). We should immediately go into some examples such that grasp the basic expressions in Python on your own. Try out the following commands in interactive mode:

```python
# Only enter the commands AFTER the prompt >>>
>>> 1 + 1 # Addition
>>> 2 - 1 # Subtraction
>>> 3 * 3 # Multiplication
>>> 10 / 3 # Division
>>> (50 - 5*6) // 4 # // Integer division
>>> 8 ** 2 # 8 square
>>> 17 ** 34 # 17 to the power 34
```

[![idle_shell_2](https://i.im.ge/2022/10/07/1v5QDY.idle-shell-2.png)](https://im.ge/i/1v5QDY)
