#seznam = [4, 2, 9, 7, 3]

"""def place(seznam, x, skip):
    if seznam[x] < seznam[x-skip] and x-skip>-1:
        place(seznam, x, skip + 1)
    else:
        seznam2 = []
        for y in range(len(seznam)-1):
            if y < x:
                seznam2.append(seznam[y])
                print("1")
                print(seznam2)
            elif y == x:
                seznam2.append(seznam[x])
                print("2")
                print(seznam2)
            else:
                seznam2.append(seznam[y+1])
                print("3")
                print(seznam2)
        seznam = seznam2
        return

def insert1(seznam):
    sorted = 1
    while sorted != len(seznam):
        place(seznam, sorted, 1)
        sorted += 1
    return seznam"""

def insert1(seznam):
    sorted = 0
    step = 0
    while sorted != len(seznam)-1:
        skip = sorted
        while skip >= 0:
            step += 1
            if seznam[skip] > seznam[skip + 1]:
                shift = seznam[skip]
                seznam[skip] = seznam[skip + 1]
                seznam[skip + 1] = shift
                skip -= 1
            else:
                skip -= 1
                continue
        sorted += 1
    return step


#print(insert1(seznam))