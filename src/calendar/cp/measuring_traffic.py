n = int(input())
sensors = []
low = []
high = []
for _ in range(n):
    __ = input().split()
    sensors.append(__[0])
    low.append(int(__[1]))
    high.append(int(__[2]))
a, b = 0, 0
for i in range(n):
    if sensors[i] == 'none':
        if i-1 >= 0 and sensors[i-1] != 'none':
            a, b = low[i], high[i]
        else: a, b = max(a, low[i]), min(b, high[i])
    elif sensors[i] == 'on':
        a += low[i]
        b += high[i]
    else:
        a -= high[i]
        b -= low[i]
c, d = 0, 0
for i in range(n-1, -1, -1):
    if sensors[i] == 'none':
        if i+1 < n and sensors[i+1] != 'none':
            c, d = low[i], high[i]
        else: c, d = max(c, low[i]), min(d, high[i])
    elif sensors[i] == 'on':
        c -= high[i]
        d -= low[i]
    else:
        c += low[i]
        d += high[i]
print(c, d, sep=' ')
print(a, b, sep=' ')
