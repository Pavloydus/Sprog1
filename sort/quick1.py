"""def partition1(left, right, seznam, step):
    pivot = seznam[round((left + right)/2)]
    print("pivot", pivot)
    start = left
    end = right
    while left < right:
        step += 1
        while seznam[left] < pivot:
            step += 1
            left += 1
        while seznam[right] > pivot:
            step += 1
            right -= 1
        print(left, right)
        step += 1
        if left < right:
            print(seznam)
            seznam[left], seznam[right] = seznam[right], seznam[left]
            left += 1
            right -= 1
    return left, start, end, step

def re_quick1(left, right, seznam, step):
    step += 1
    if right - left > 2:
        mid, left, right, step = partition1(left, right, seznam, step)
        print(mid, left, right)
        step = re_quick1(left, mid-1, seznam, step)
        step = re_quick1(mid, right, seznam, step)
    else:
        print("konec")
    return step

def quick1(seznam):
    left = 0
    right = len(seznam)-1
    step = 0
    step = re_quick1(left, right, seznam, step)
    print(seznam)
    return step

print(quick1([2, 4, 3, 1, 6, 15, 23, 66, 12, 1]))"""

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
            print(seznam, left, right, pivot)
            left += 1
            right -= 1
        else:
            print("end")
            return left, seznam, step

def re_quick1(start, end, seznam, step):
    step += 1
    if end - start > 0:
        mid, seznam, step = partition1(start, end, seznam, step)
        print("left", start, mid - 1)
        step = re_quick1(start, mid - 1, seznam, step)
        print("right", mid, end)
        step = re_quick1(mid, end, seznam, step)
    return step

def quick1(seznam):
    return re_quick1(0, len(seznam)-1, seznam, 0)
        
#print(re_quick1(0, 8, [5, 12, 63, 4, 12, 3, 12, 24, 1], 0))