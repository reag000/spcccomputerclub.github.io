from string import *
n = int(input())
a = {ascii_lowercase[i]: 0 for i in range(26)}
for _ in range(n):
    w, x = input().split()
    b = {ascii_lowercase[i]: 0 for i in range(26)}
    c = {ascii_lowercase[i]: 0 for i in range(26)}
    for i in w:
        b[i] += 1
    for i in x:
        c[i] += 1
    for i in ascii_lowercase:
        a[i] += max(b[i], c[i])
for i in a.values():
    print(i)
