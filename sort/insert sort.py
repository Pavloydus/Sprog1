seznam = [4, 2, 9, 7, 3]

def place(seznam, x, skip):
    if seznam[x] < seznam[x-skip] and (x-skip) >= 0:
        place(seznam, x, skip + 1)
    else:
        seznam2 = []
        for y in range(len(seznam)-1):
            if y < x:
                seznam2.append(seznam[y])
            elif y == x:
                seznam2.append(seznam[x])
            else:
                seznam2.append(seznam[y+1])
            print(seznam2)
        seznam = seznam2
        return

def insert1(seznam):
    sorted = 1
    while sorted != len(seznam):
        place(seznam, sorted, 1)
        sorted += 1
    return seznam

print(insert1(seznam))


