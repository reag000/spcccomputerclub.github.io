class r:
    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = map(int, input().split()) # left-bottom, right-upper
    
    def area(self):
        return (self.x2-self.x1)*(self.y2-self.y1)

def intercept(a, b):
    x_overlap = max(0, min(a.x2, b.x2)-max(a.x1, b.x1))
    y_overlap = max(0, min(a.y2, b.y2)-max(a.y1, b.y1))
    return x_overlap*y_overlap

rs = []
for _ in range(3):
    rs.append(r())
print(rs[0].area() + rs[1].area() - intercept(rs[0], rs[2]) - intercept(rs[1], rs[2]))
