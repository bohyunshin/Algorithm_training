def bst(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

n,target = map(int, input().split())
array = list(map(int, input().split()))
index = bst(array,target,0,len(array)-1)

if index is None:
    print(-1)
    exit(0)

result = 1
# index보다 큰 지점을 살펴본다
while index <= len(array):
    index += 1
    if array[index] == target:
        result += 1
        index += 1
    else:
        break
# index보다 작은 지점을 살펴본다
while index > 0:
    index -= 1
    if array[index] == target:
        result += 1
        index -= 1
    else:
        break
print(result)