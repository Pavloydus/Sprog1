def shell1(seznam):
    step = 0
    gap = round(len(seznam)/2)
    while gap > 0:
        for x in range(len(seznam)-gap):
            skip = 0
            while x + skip >= 0:
                step += 1
                if seznam[x + skip] > seznam[x + skip + gap]:
                    seznam[x + skip], seznam[x + skip + gap] = seznam[x + skip + gap], seznam[x + skip]
                    skip -= gap
                else:
                    break
        gap = round(gap/2)
    return step