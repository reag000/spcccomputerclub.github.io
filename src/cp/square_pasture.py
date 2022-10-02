class r:
    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = map(int, input().split()) # bottom-left, top-right
        
a = r()
b = r()
l = max(max(a.x2, b.x2) - min(a.x1, b.x1), max(a.y2, b.y2) - min(a.y1, b.y1))
print(l*l)
