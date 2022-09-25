c, m = [0]*3, [0]*3
for _ in range(3):
    c[_], m[_] = map(int, input().split())
i = 0
for _ in range(100):
    j = (i+1)%3
    a = min(c[j]-m[j], m[i])
    m[i] -= a
    m[j] += a
    i = j
for _ in range(3):
    print(m[_])
