def bubble1(seznam):
    step = 0
    while step != (len(seznam)-1)**2:
        for x in range((len(seznam)-1)):
            step += 1
            if seznam[x] > seznam[x+1]:
                seznam[x], seznam[x+1] = seznam[x+1], seznam[x]
    return step