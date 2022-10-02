t = int(input())
for i in range(t):
    y, x = list(map(int, input().split()))
    m = max(x, y)
    if m%2 == 0:
        print(m*m - (m-y) - (x-1))
    else:
        print(m*m - (y-1) - (m-x))
