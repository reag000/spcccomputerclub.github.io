n = int(input())
o = list(map(int, input().split()))
d = list(map(int, input().split()))
for _ in range(3):
    t = []
    for i in range(n):
        t.append(d[o[i]-1])
    d = t
for c in d:
    print(c)