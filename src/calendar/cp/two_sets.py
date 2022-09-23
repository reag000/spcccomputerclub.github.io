n = int(input())
if n%4 == 0:
    print('YES')
    print(n//2)
    print(' '.join([str(x) for x in range(1, n+1) if x%4 == 1 or x%4 == 0]))
    print(n//2)
    print(' '.join([str(x) for x in range(1, n+1) if x%4 == 2 or x%4 == 3]))
elif n == 3:
    print('YES\n1\n3\n2\n1 2')
elif n%4 == 3:
    print('YES')
    print((n-1)//2+1)
    s = [x for x in range(1, (n//4)*4) if x%4 == 1 or x%4 == 2]
    s.extend([n-3, n])
    print(' '.join(list(map(str, s))))
    print((n-1)//2)
    print(' '.join([str(x) for x in set(range(1, n+1)).difference(s)]))
else:
    print('NO')
        