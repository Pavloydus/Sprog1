def bubble4(seznam):
    start = 0
    end = 0
    change = True
    flip = False
    step = 0
    while start + end != len(seznam)-1 and change == True:
        change = False
        if flip == False:
            for x in range(start, len(seznam)-1-end):
                        step += 1
                        if seznam[x] > seznam[x+1]:
                            seznam[x], seznam[x+1] = seznam[x+1], seznam[x]
                            change = True
            flip = True
            end += 1
        else:
            for x in range(len(seznam)-1-end, start, -1):
                        step += 1
                        if seznam[x] < seznam[x-1]:
                            seznam[x], seznam[x-1] = seznam[x-1], seznam[x]
                            change = True
            flip = False            
            start += 1
    return step