class r:
    def __init__(self):
        self.x1, self.y1, self.x2, self.y2 = map(int, input().split())

    def area(self):
        return (self.x2-self.x1)*(self.y2-self.y1)
    
def intercept(a, b):
    x_overlap = max(0, min(a.x2, b.x2)-max(a.x1, b.x1))
    y_overlap = max(0, min(a.y2, b.y2)-max(a.y1, b.y1))
    return x_overlap*y_overlap

a = r()
b = r()
x = a.area() - intercept(a, b) if (b.x2 >= a.x2 and b.x1 <= a.x1) or (b.y2 >= a.y2 and b.y1 <= a.y1) else a.area()
print(x)
