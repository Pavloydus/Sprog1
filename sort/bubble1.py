def bubble1(seznam):
    skip = 0
    step = 0
    while skip != len(seznam)-2:
        for x in range(len(seznam)-1-skip):
            step += 1
            if seznam[x] > seznam[x+1]:
                prehoz = seznam[x]
                seznam[x] = seznam[x+1]
                seznam[x+1] = prehoz
        skip += 1
    return step