def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n = int(input())
N = list(map(int, input().split()))
N.sort()
m = int(input())
M = list(map(int, input().split()))

for i in M:
    if binary_search(N,i,0,len(N)-1) is not None:
        print('yes',end=' ')
    else:
        print('no',end=' ')