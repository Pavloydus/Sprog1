class Zasobnik:
    def __init__(self):
        self.zasobnik = []

    def push(self, prvek):
        self.zasobnik.append(prvek)
    
    def isEmpty(self):
        if len(self.zasobnik) == 0:
            return True
        else:
            return False
    
    def pop(self):
        if not self.isEmpty():
            return self.zasobnik.pop()
        else:
            return None
        
    def peek(self):
        if not self.isEmpty():
            return self.zasobnik[-1]
        else:
            return None
    
    def clear(self):
        self.zasobnik = []
    
    def __str__(self):
        return str(self.zasobnik)


zasobnik = Zasobnik()
print(zasobnik.isEmpty())
zasobnik.push(5)
zasobnik.push(-3)
print(zasobnik)
print(zasobnik.pop())
print(zasobnik.peek())
print(zasobnik.isEmpty())
zasobnik.clear()
print(zasobnik.isEmpty())
zasobnik.pop()