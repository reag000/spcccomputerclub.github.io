class r:
    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = map(int, input().split())
    
    def area(self):
        return (self.x2-self.x1)*(self.y2-self.y1)

class r1:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

def intercept(a, b):
    x_overlap = max(0, min(a.x2, b.x2)-max(a.x1, b.x1))
    y_overlap = max(0, min(a.y2, b.y2)-max(a.y1, b.y1))
    return x_overlap*y_overlap

rs = []
for _ in range(3):
    rs.append(r())
a = intercept(rs[1], rs[2])
a_r = r1(max(rs[1].x1, rs[2].x1), max(rs[1].y1, rs[2].y1), min(rs[1].x2, rs[2].x2), min(rs[1].y2, rs[2].y2)) if a > 0 else r1()
if rs[0].area()-intercept(rs[0], rs[1])-intercept(rs[0], rs[2])+intercept(a_r, rs[0]) > 0: print('YES')
else: print('NO')
