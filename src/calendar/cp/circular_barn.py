n = int(input())
r = [int(input()) for _ in range(n)]
m = 100*n
for i in range(n):
    c = 0
    for j in range(n):
        c += r[(i+j)%n]*j
    m = min(m, c)
print(m)
