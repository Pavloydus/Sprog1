class Dvojice:
    def __init__(self, hodnota):
        self.hodnota = hodnota
        self.pred = None

class Zasobnik:
    def __init__(self):
        self.top = None
    
    def push(self, hodnota):
        novy_top = Dvojice(hodnota)
        novy_top.pred = self.top
        self.top = novy_top

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
    
    def peek(self):
        if not self.isEmpty():
            return self.top.hodnota
    
    def pop(self):
        if self.isEmpty:
            return None
        elif self.top.pred == None:
            hodnota = self.top.hodnota
            self.top = None
            return hodnota
        else:
            hodnota = self.top.hodnota
            self.top = self.top.pred
            return hodnota
        


def kontrola_zavorek(priklad):
    zavorky = Zasobnik()
    for x in priklad:
        if x == "(":
            zavorky.push("(")
        elif x == ")":
            if zavorky.peek() == "(":
                zavorky.pop()
            else:
                return False
    return zavorky.isEmpty()

print(kontrola_zavorek(input("Zadej příklad: ")))