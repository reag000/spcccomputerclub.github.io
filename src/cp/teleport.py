a, b, x, y = tuple(map(int, input().split()))
print(min(abs(a-b), abs(a-x)+abs(b-y), abs(a-y)+abs(b-x)))