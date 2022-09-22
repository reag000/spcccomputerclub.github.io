---
title: "CSES Weird Algorithm"
date: 2022-09-20T15:30:27+08:00
draft: false
---

# CSES Weird Algorithm

## Solution

[Problem Description](https://cses.fi/problemset/task/1068)

```python
n = int(input())
while n != 1:
    print(n, end=' ')
    if n%2 == 0: n //= 2
    else: n = n*3 + 1
print(1, end='')
```
