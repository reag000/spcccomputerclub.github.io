x, y, m = list(map(int, input().split()))
mx = 0
for i in range(m//x + 1):
    mx = max(mx, x*i+(m-x*i)//y*y)
print(mx)
