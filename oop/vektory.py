import math

class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x}, {self.y}]"
    
    def __add__(self, jiny):
        x = self.x + jiny.x
        y = self.y + jiny.y
        return Vektor(x, y)
    
    def delka(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __mul__(self, jiny):
        if isinstance(jiny, Vektor):
            return self.x * jiny.x + self.y + jiny.y
        else:
            return Vektor(self.x * jiny, self.y * jiny)

v1 = Vektor(3, 4)
print(v1)

v2 = Vektor(7, 3)
print(v1 + v2)

print(v1.delka())

print(v1 * 8)
print(v1 * v2)