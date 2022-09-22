---
title: "CSES Missing Number"
date: 2022-09-20T15:43:54+08:00
draft: false

---

# Solution

[Problem Description](https://cses.fi/problemset/task/1083)

```python
n = int(input())
a = set(range(1, n+1))
b = set(map(int, input().split()))
print(next(iter(a.difference(b))))
```
