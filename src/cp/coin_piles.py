n = int(input())
for t in range(n):
    a, b = tuple(map(int, input().split()))
    if a == 0 and b == 0: print('YES')
    elif (a+b)%3 != 0 or a == 0 or b == 0: print('NO')
    else:
        j = 2*b-a
        if j%3 != 0 or j//3 < 0 or b < 2*(j//3):
            print('NO')
        else: print('YES')
