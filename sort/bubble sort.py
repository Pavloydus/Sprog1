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
    x = 0
    while not skip == (len(seznam)-2):
        step += 1
        if seznam[x] > seznam[x+1]:
            prehoz = seznam[x]
            seznam[x] = seznam[x+1]
            seznam[x+1] = prehoz
            flip = -flip
        if x in range(len(seznam)):
        x + flip
        print(seznam)
    skip += 1
    print(step)

print(bubble2(0, 0, 1))