n, m = map(int, input().split())
rl, rs = [0]*n, [0]*n
for _ in range(n):
    rl[_], rs[_] = map(int, input().split())
cl, cs = [0]*n, [0]*n
for _ in range(m):
    cl[_], cs[_] = map(int, input().split())
l, j, k = 0, 0, 0
d = []
for i in range(m):
    while l < cl[i]:
        l += rl[k]
        k += 1 # l: cl[j] + ... + cl[k-1]
    d.append(-min(0, min(rs[j:k])-cs[i]))
    l -= cl[i]
    j = k-1 if l > 0 else k
print(max(d))
