n, k = list(map(int, input().split()))
diamonds = [int(input()) for _ in range(n)]
mx = 0
for x in diamonds:
    display = [x]
    for y in diamonds:
        show = True
        for diamond in display:
            if abs(diamond - y) > k:
                show = False
                break
        if show: display.append(y)
    mx = max(mx, len(display)-1)
print(mx)
