from math import *
n = int(input())
m = floor(log(n)/log(5))
l = 0
for i in range(1, m+1):
    l += n//(5**i)
print(l)
