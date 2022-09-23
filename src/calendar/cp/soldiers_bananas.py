k, n, w = (map(int, input().split()))
t = w*(w+1)//2*k
if n >= t: print(0)
else: print(t - n)