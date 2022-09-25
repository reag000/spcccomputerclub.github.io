m, n, k = map(int, input().split())
print()
for _ in range(m):
    s = input()
    for __ in range(k):
        for c in s:
            print(c*k, end='')
        print()
