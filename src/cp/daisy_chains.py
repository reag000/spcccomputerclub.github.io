n = int(input())
flowers = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1, n+1):
        slice = flowers[i:j]
        avg = sum(slice)/(j-i)
        if avg in slice:
            cnt += 1
print(cnt)
