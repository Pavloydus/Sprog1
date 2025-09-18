seznam = [5, 2, 7, 8, 6, 1]

def bubble1(skip, step):
    for x in range(len(seznam)-1-skip):
        step += 1
        if seznam[x] > seznam[x+1]:
            prehoz = seznam[x]
            seznam[x] = seznam[x+1]
            seznam[x+1] = prehoz
        print(seznam)
    skip += 1
    print(step)
    if skip == (len(seznam)-2):
        return seznam
    else:
        bubble1(skip, step)

def bubble2(skip, step, flip):
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
        return seznam
    else:
        bubble2(skip, step, flip)

print(bubble2(0, 0, 1))