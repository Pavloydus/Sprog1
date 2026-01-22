class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def popis(self):
        return f"[{self.x}, {self.y}]"

class Rectangle:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

        self.len_x = max(self.p1.x, self.p2.x, self.p3.x, self.p4.x) -  min(self.p1.x, self.p2.x, self.p3.x, self.p4.x)
        self.len_y = max(self.p1.y, self.p2.y, self.p3.y, self.p4.y) -  min(self.p1.y, self.p2.y, self.p3.y, self.p4.y)
    
    def move(self, dx=0, dy=0):
        self.p1.x = self.p1.x + dx
        self.p1.y = self.p1.y + dy

        self.p2.x = self.p2.x + dx
        self.p2.y = self.p2.y + dy

        self.p3.x = self.p3.x + dx
        self.p3.y = self.p3.y + dy

        self.p4.x = self.p4.x + dx
        self.p4.y = self.p4.y + dy

    def area(self):
        return abs(self.len_x * self.len_y)
    
    def contains_point(self, point):
        if self.p1.x <= point.x <= self.p2.x and self.p1.y <= point.y <= self.p4.y:
            return True       
        return False
    
    def scale(self, factor):
        self.len_x = self.len_x * factor
        self.len_y = self.len_y * factor

        anchor = Point(min(self.p1.x, self.p2.x, self.p3.x, self.p4.x), min(self.p1.y, self.p2.y, self.p3.y, self.p4.y))

        self.p1 = anchor
        self.p2.x = anchor.x + self.len_x
        self.p2.y = anchor.y
        self.p3.x = anchor.x + self.len_x
        self.p3.y = anchor.y + self.len_y
        self.p4.x = anchor.x
        self.p4.y = anchor.y + self.len_y

    def __str__(self):
        return f"Obdélník má body {self.p1.popis()}, {self.p2.popis()}, {self.p3.popis()}, {self.p4.popis()}"


"""p = Point(2, 3)
print(p.x, p.y)

r = Rectangle(
    Point(1, 2),
    Point(5, 2),
    Point(5, 6),
    Point(1, 6)
)

print(r.p1.x, r.p1.y)
print(r.p3.x, r.p3.y)

r.move(0, -1)
print(r.p1.x, r.p1.y)
print(r.p4.x, r.p4.y)

print(r.area())

inside = Point(4, 3)
outside = Point(10, 10)

print(r.contains_point(inside))
print(r.contains_point(outside))"""

"""r = Rectangle(
    Point(1, 1),
    Point(3, 1),
    Point(3, 2),
    Point(1, 2)
)

r.move(1, 1)
r.scale(3)

print(r.area())"""

"""r = Rectangle(
    Point(-1.5, 1),
    Point(2.5, 2),
    Point(2.5, 1),
    Point(-1.5, 2)
)

print(r.contains_point(Point(0, 1)))
r.scale(-0.5)
print(r.area())
print(r)"""