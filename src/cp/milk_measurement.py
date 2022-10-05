n = int(input())
l = []
for _ in range(n):
    s = input().split()
    l.append((int(s[0]), s[1], int(s[2])))
l.sort()
cows = [7] * 3
m = 7
cnt = 0
for _, s, c in l:
    if s == 'Bessie':
        cows[0] += c
    elif s == 'Mildred':
        cows[1] += c
    else:
        cows[2] += c
    if max(cows) != m:
        m = max(cows)
        cnt += 1
print(cnt)
