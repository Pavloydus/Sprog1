def partition1(left, right, seznam, step):
    pivot = seznam[round((left + right)/2)]
    mid = right
    while left <= right:
        step += 1
        while seznam[left] < pivot:
            step += 1
            left += 1
        while seznam[right] > pivot:
            step += 1
            right -= 1
        print(left, right)
        step += 1
        if left <= right:
            print(seznam)
            seznam[left], seznam[right] = seznam[right], seznam[left]
            left += 1
            right -= 1
    return left, mid, step

def re_quick1(left, right, seznam, step):
    step += 1
    if right - left > 1:
        left, right, step = partition1(left, right, seznam, step)
        print("aaaaaaaa")
        step = re_quick1(0, left-1, seznam, step)
        step = re_quick1(left, right, seznam, step)
    return step

def quick1(seznam):
    left = 0
    right = len(seznam)-1
    step = 0
    step = re_quick1(left, right, seznam, step)
    return step