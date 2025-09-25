def bubble2(seznam, skip=0, step=0, flip=1):
    spravne = 0
    if flip == 1:
        for x in range(skip, len(seznam)-1):
            step += 1
            print(seznam[x])
            print(seznam[x+1])
            if seznam[x] > seznam[x+1]:
                prehoz = seznam[x]
                seznam[x] = seznam[x+1]
                seznam[x+1] = prehoz
            else:
                spravne += 1
            print(seznam)
            print(step)
    else:
        for x in range(len(seznam)-1-skip, 0, -1):
            step += 1
            print(seznam[x])
            print(seznam[x-1])
            if seznam[x] < seznam[x-1]:
                prehoz = seznam[x]
                seznam[x] = seznam[x-1]
                seznam[x-1] = prehoz
            else:
                spravne += 1
            print(seznam)
            print(step)
    flip = -flip
    skip += 1
    if skip == (len(seznam)-2) or spravne == len(seznam)-1:
        return seznam, step
    else:
        bubble2(seznam, skip, step, flip)