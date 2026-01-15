from zasobnik2 import *

def zkontroluj_zavorky(priklad):
    zavorky = Stack()
    for x in priklad:
        if x == "(":
            zavorky.push("(")
        elif x == "[":
            zavorky.push("[")
        elif x == "{":
            zavorky.push("{")
        elif x == ")":
            if zavorky.peek() == "(":
                zavorky.pop()
            else:
                return False
        elif x == "]":
            if zavorky.peek() == "[":
                zavorky.pop()
            else:
                return False
        elif x == "}":
            if zavorky.peek() == "{":
                zavorky.pop()
            else:
                return False
    if zavorky.isEmpty():
        return True
    else:
        return False
    
print(zkontroluj_zavorky(input("Zadej příklad: ")))