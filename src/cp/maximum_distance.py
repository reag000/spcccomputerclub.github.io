n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
m = 0
for i in range(n):
    for j in range(i+1, n):
        distance = (y[j]-y[i])**2 + (x[j]-x[i])**2
        m = max(m, distance)
print(m)
