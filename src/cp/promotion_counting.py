a1, a2 = (map(int, input().split()))
b1, b2 = (map(int, input().split()))
c1, c2 = (map(int, input().split()))
d1, d2 = (map(int, input().split()))
n = (a2+b2+c2+d2)-(a1+b1+c1+d1)
b = c = d = 0
b = a1 + n - a2
c = b1 + b - b2
d = d2 - d1
print(b, c, d, sep='\n')
