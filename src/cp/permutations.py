n = int(input())
if n == 1:
    print(1)
elif n < 4:
    print('NO SOLUTION')
else:
    i = 1
    while 2*i <= n:
        print(2*i, end=' ')
        i += 1
    i = 0
    while 2*i+1 <= n:
        print(2*i+1, end=' ')
        i += 1
