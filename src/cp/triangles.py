from itertools import permutations


n = int(input())
fences = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    fences.append((x, y))
perms = list(permutations(fences, 3))
area = 0
for p in perms:
    if p[0][1] == p[1][1] and p[1][0] == p[2][0]:
        area = max(area, abs((p[1][0] - p[0][0]) * (p[2][1] - p[1][1])))
print(area)
