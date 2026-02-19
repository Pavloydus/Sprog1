import math

def kvad_rov(a, b, c):
    #výpočet a kontrola nezápornosti diskriminantu
    d = b**2 -4 * a * c
    if d < 0:
        return
    
    #výpočet a vrácení kořenů
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2

print(kvad_rov(1, -1, 6))