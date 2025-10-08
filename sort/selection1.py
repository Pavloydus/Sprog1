def selection1(seznam):
    sorted = 0
    step = 0
    while sorted != len(seznam):
        change = False
        min = seznam[sorted]
        for x in range(sorted+1, len(seznam)):
            step +=1
            if seznam[x] < min:
                min = seznam[x]
                minx = x
                change = True
        if change == True:
            seznam[sorted], seznam[minx] = seznam[minx], seznam[sorted]
        sorted += 1
    return step