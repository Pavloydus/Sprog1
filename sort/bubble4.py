def bubble4(seznam):
    skip = 0
    change = True
    flip = False
    step = 0
    while skip != len(seznam)-1 and change == True:
        change = False
        if flip == False:
            for x in range(skip, len(seznam)-1-skip):
                        step += 1
                        if seznam[x] > seznam[x+1]:
                            seznam[x], seznam[x+1] = seznam[x+1], seznam[x]
                            change = True
            flip = True
        else:
            for x in range(len(seznam)-2-skip, skip-1, -1):
                        step += 1
                        if seznam[x] < seznam[x-1]:
                            seznam[x], seznam[x-1] = seznam[x-1], seznam[x]
                            change = True
            flip = False            
        skip += 1
    print(seznam)
    return step

print(bubble4([5, 7, 48, 6, 3, 4, 3, 999]))