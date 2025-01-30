x = int(input("Zadej číslo: "))
xstr = str(x)

min = x
max = 0
for i in range(len(xstr)):
    if int(xstr[i]) > max:
        max = int(xstr[i])
    if int(xstr[i]) < min:
        min = int(xstr[i])
print(f"Největší číslo: {max}, nejmenší číslo: {min}.")