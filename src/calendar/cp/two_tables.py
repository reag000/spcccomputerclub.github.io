class rectangle:
    def __init__(self):
        self.x_1, self.y_1, self.x_2, self.y_2 = map(int, input().split())
        
t = int(input())
for _ in range(t):
    W, H = map(int, input().split())
    r = rectangle()
    w, h = map(int, input().split())
    lf = abs(min(0, r.x_1-w))
    rh = abs(min(0, W-w-r.x_2))
    up = abs(min(0, H-h-r.y_2))
    bt = abs(min(0, r.y_1-h))
    l = []
    if r.x_2+lf <= W: l.append(lf)
    if r.x_1-rh >= 0: l.append(rh)
    if r.y_1-up >= 0: l.append(up)
    if r.y_2+bt <= H: l.append(bt)
    if len(l) == 0: print(-1)
    else: print(min(l))    
        