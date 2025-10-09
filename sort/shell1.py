def shell1(seznam):
    step = 0
    gap = round(len(seznam)/2)
    while gap > 0:
        #print(gap)
        for x in range(len(seznam)-gap):
            skip = 0
            while x + skip >= 0:
                step += 1
                #print(seznam)
                if seznam[x + skip] > seznam[x + skip + gap]:
                    seznam[x + skip], seznam[x + skip + gap] = seznam[x + skip + gap], seznam[x + skip]
                    skip -= gap
                else:
                    #print("break")
                    break
        gap = round(gap/2)
    return step

#print(shell1([45, 77, 69, 3, 7, 5, 1, 7, 9, 66]))