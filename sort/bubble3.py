def bubble3(seznam):
    change = True
    skip = 0
    step = 0
    while skip != len(seznam)-1 and change == True:
        change = False
        for x in range(len(seznam)-1-skip):
            step += 1
            if seznam[x] > seznam[x+1]:
                seznam[x], seznam[x+1] = seznam[x+1], seznam[x]
                change = True
        skip += 1
    return step