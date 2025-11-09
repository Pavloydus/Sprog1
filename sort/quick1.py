def partition1(left, right, seznam, step):
    pivot = seznam[round((left + right) / 2)]
    while True:
        while seznam[left] < pivot:
            left += 1
            step += 1
        while seznam[right] > pivot:
            right -= 1
            step += 1
        step += 1
        if left < right:
            seznam[left], seznam[right] = seznam[right], seznam[left]
            #print(seznam, left, right, pivot)
            left += 1
            right -= 1
        else:
            #print("end")
            return left, seznam, step

def re_quick1(start, end, seznam, step):
    step += 1
    if end - start > 1:
        mid, seznam, step = partition1(start, end, seznam, step)
        #print("left", start, mid - 1)
        step = re_quick1(start, mid - 1, seznam, step)
        #print("right", mid, end)
        step = re_quick1(mid, end, seznam, step)
    elif end - start > 0:
        step += 1
        if seznam[start] > seznam[end]:
            seznam[start], seznam[end] = seznam[end], seznam[start]
    return step

def quick1(seznam):
    return re_quick1(0, len(seznam)-1, seznam, 0)