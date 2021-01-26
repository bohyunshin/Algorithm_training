array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

def quick_sort(array, start, end):
    if start >= end:
        return
    left = start + 1
    right = end
    pivot = start
    while left <= right:
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)
quick_sort(array,0,len(array)-1)
print(array)