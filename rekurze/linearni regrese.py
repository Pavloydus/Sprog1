body = {1:2, 2:4, 3:6}
n = 3

def linear(k):
    suma = 0
    for x in body.keys():
        suma += ((x * k) - (body[x]))**2
    return suma / n

def costFunction(k1, step, presnost):
    k2 = k1 + step
    print(k1)
    if (linear(k1) - linear(k2)) / (k2 - k1) == 0 or presnost == 0:
        return k1
    elif (linear(k1) - linear(k2)) / (k2 - k1) > 0:
        costFunction(k1 - k1 / 2, step * 0.95, presnost - 1)
    else:
        costFunction(k1 + k1 / 2, step * 0.95, presnost - 1)

print(costFunction(1, 0.95, 100))