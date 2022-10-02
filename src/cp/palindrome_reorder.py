from string import *
s = [*input()]
d = dict(zip(ascii_uppercase, [0 for i in range(26)]))
for c in s:
    d[c] += 1
s = ascii_uppercase
b = False
k = 26
for i in range(0, 26):
    if d[s[i]]%2 != 0:
        if b: 
            print('NO SOLUTION')
            exit()
        else: 
            b = True
            k = i
for i in range(0, 26):
    print(s[i]*(d[s[i]]//2), end='')
if k < 26:
    print(s[k], end='')
for i in range(25, -1, -1):
    print(s[i]*(d[s[i]]//2), end='')
