seznam = [2, 3, 1, 0, 5, 6, 4]

max = 0
min = seznam[0]
prum = 0
for x in seznam:
    if x > max:
        max = x
    if x < min:
        min = x
    prum += x
prum = prum/len(seznam)

print(min, max, prum)