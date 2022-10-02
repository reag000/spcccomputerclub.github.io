from re import S


n = int(input())
a = list(map(int, input().split()))
p = a[0]
s = 0
for i in range(1, len(a)):
    if a[i] < p:
        s += p - a[i]
    if a[i] > p:
        p = a[i]
print(s)
