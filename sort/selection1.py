#seznam = [1, 58, 7, 6, 3, 1]

def selection1(seznam):
    sorted = 0
    step = 0
    while sorted != len(seznam):
        change = False
        min = seznam[sorted]
        for x in range(sorted, len(seznam)):
            step +=1
            if seznam[x] < min:
                min = seznam[x]
                minx = x
                change = True
        if change == False:
            sorted += 1
            continue
        shift = seznam[sorted]
        seznam[minx] = shift
        seznam[sorted] = min
        sorted += 1
    return step

#print(selection1(seznam))