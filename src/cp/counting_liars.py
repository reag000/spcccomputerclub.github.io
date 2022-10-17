from math import *


n = int(input())
less = []
greater = []
max_pos = -inf
min_pow = inf
for _ in range(n):
    a, b = input().split()
    b = int(b)
    if a == 'G':
        greater.append(b)
    else:
        less.append(b)
    max_pos = max(max_pos, b)
    min_pos = min(min_pos, b)
less.sort()
greater.sort()
min_liers = inf
for bessie_pos in range(min_pos - 1, max_pos + 2):
    cnt = 0
    for l in less:
        if l < bessie_pos:
            cnt += 1
    for g in greater:
        if g > bessie_pos:
            cnt += 1
    min_liers = min(min_liers, cnt)
