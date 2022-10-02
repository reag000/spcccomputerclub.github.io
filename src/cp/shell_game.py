n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
s = [False]*4

def f(s):
    m = 0
    for i in range(n):
        s[d[i][0]], s[d[i][1]] = s[d[i][1]], s[d[i][0]]
        if s[d[i][2]]: m += 1
    return m

s[1] = True
m1 = f(s)
s[1], s[2] = s[2], s[1]
m2 = f(s)
s[2], s[3] = s[3], s[2]
m3 = f(s)
print(max(m1, m2, m3))