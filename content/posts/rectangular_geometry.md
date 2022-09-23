---
title: "Rectangular Geometry"
date: 2022-09-23T20:37:23+08:00
draft: false
math: true
---

# Rectangular Geometry

## Rectangle Object

A rectangle can be defined by two points: $(x_1, y_1)$ the bottom-left point and $(x_2, y_2)$ the top right point, where $x_2 \geq x_1$ and $y_2 \geq y_1$. The area of it is given by $(x_2 - x_1) \cdot (y_2 - y_1)$.

```python
class rectangle:
    def __init__(self):
        self.x_1, self.y_1, self.x_2, self.y_2 = map(int, input().split())
    
    def area(self):
        return (self.x_2-self.x_1)*(self.y_2-self.y_1)
```

## Intersection of Two Line Segments

A line segment can be defined by two points: $(a, b)$ where $b > a$. The intersection of two line segments $(a, b)$ and $(c, d)$ is given by $\max(0, \min(b, d) - \max(a, c))$.

```python
class line:
    def __init__(self):
        self.a, self.b = map(int, input().split())
    
def l_intersection(l1, l2):
    return max(0, min(l1.b, l2.b) - max(l1.a, l2.a))
```

## Intersection of Two Rectangles

Two rectangles defined by $(x_1, y_1), (x_2, y_2)$ and $(x_3, y_3), (x_4, y_4)$ have an area of the intersection $A \geq 0$. $A$ is given by the product of the intersection in length and the intersection in width:

$$
A = max(0, min(x_2, x_4) - max(x_1, x_3)) \cdot max(0, min(y_2, y_4) - max(y_1, y_3))
$$

```python
def r_intersection_area(r1, r2):
    x_intersect = max(0, min(r1.x_2, r2.x_2)-max(r1.x_1, r2.x_1))
    y_intersect = max(0, min(r1.y_2, r2.y_2)-max(r1.y_1, r2.y_1))
    return x_intersect*y_intersect
```

Suppose $A > 0$, the intersection of two rectangles $a$ and $b$ is a rectangle defined by $(max(x_{a1}, x_{b1}), max(y_{a1}, y_{b1}))$ and $(min(x_{a2}, x_{b2}), min(y_{a2}, y_{b2}))$, the bottom-left and top-right points.

