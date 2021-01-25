array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while left <= right: # 교차되기 전까지 반복
        while left <= end and array[pivot] >= array[left]:
            left += 1
        while right > start and array[pivot] <= array[right]:
            right -= 1
        if left > right: # 교차된다면
            array[pivot], array[right] = array[right], array[pivot]
        else: # 교차가 안된다면
            array[right], array[left] = array[left], array[right]
    # 분할이 된 리스트를 재귀적으로 퀵 정렬함
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
quick_sort(array, 0, len(array)-1)
print(array)