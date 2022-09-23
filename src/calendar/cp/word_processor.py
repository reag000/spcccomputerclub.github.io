n, k = (map(int, input().split()))
c = 0
for w in input().split():
    if c+len(w) > k:
        print()
        print(w, end=' ')
        c = len(w)
    else:
        print(w, end=' ')
        c += len(w)
        