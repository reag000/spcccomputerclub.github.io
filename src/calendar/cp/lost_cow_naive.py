x, y = map(int, input().split())
d = 1
i = 1
a = x
t = 0
while a != y:
    while a != x+i*d:
        a += i
        t += 1
        if a == y:
            break
    i *= -1
    d *= 2
print(t)
