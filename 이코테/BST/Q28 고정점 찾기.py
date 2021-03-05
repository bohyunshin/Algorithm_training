def bst(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid-1
        else:
            start = mid+1
    return None

n = int(input())
array = list(map(int, input().split()))
result = bst(array,0,len(array)-1)
if result is None:
    print(-1)
else:
    print(result)