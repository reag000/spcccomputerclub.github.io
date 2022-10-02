n = int(input())
a = set(range(1, n+1))
b = set(map(int, input().split()))
print(next(iter(a.difference(b))))
