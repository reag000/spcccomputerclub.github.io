from math import *

x, y = map(int, input().split())
t = 0
d = 0
if x == y: t = 0
elif x < y: 
    t = 2*ceil(log(y-x, 4))+1
    d = x+2**(t-1)-y
else: 
    t = 2*ceil(log(2*(x-y), 4))
    d = y-(x-2**(t-1))
print(3*2**(t-1)-2-d)
