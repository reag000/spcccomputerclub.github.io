n = int(input())
xy = []
x = y = 0
mn = 101
k = 0
xy.append((0, 0))
for _ in range(n):
    s = input().split()
    c, m = s[0], int(s[1])
    ox = oy = 0
    if c == 'N': oy = 1
    elif c == 'S': oy = -1
    elif c == 'E': ox = 1
    elif c == 'W': ox = -1
    for i in range(m):
        k += 1
        x += ox
        y += oy
        c = (x, y)
        if c in xy:
            for j in range(len(xy)-1, -1, -1):
                if xy[j] == c:
                    mn = min(mn, k-j)
                    break
        xy.append((x, y))
    ox = oy = 0
        
print(mn)
