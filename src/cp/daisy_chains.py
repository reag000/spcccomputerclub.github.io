n = int(input())
pi = list(map(int, input().split()))
cnt = 0
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += pi[j]
        for k in range(i, j+1):
            if pi[k] == sum:
                cnt += 1
print(cnt)
