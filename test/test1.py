a = float(input("Zadej délku první strany: "))
b = float(input("Zadej délku druhé strany: "))
c = float(input("Zadej délku třetí strany: "))

if a + b <= c or b + c <= a or a + c <= b:
    print(f"Strany {a}, {b}, {c} netvoří trojúhelník.")
else:
    if a == b or b == c or a == c:
        if a == b == c:
            print(f"Strany {a}, {b}, {c} tvoří rovnostranný trojúhelník.")
        else:
            print(f"Strany {a}, {b}, {c} tvoří rovnoramenný trojúhelník.")
    else:
         print(f"Strany {a}, {b}, {c} tvoří obecný trojúhelník.")

    # Bonus
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
        print(f"Strany {a}, {b}, {c} tvoří pravoúhlý trojúhelník.")
    elif a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and c**2 + b**2 > a**2:
        print(f"Strany {a}, {b}, {c} tvoří ostroúhlý trojúhelník.")
    else:
        print(f"Strany {a}, {b}, {c} tvoří tupoúhlý trojúhelník.")

    
 

    
    

























    