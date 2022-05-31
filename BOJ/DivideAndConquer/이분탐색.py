arr = [1,3,5,7,9,10]
def binary_search(x):
    left = 0
    right = len(arr)-1
    mid = (left + right) // 2
    while left <= right:
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            right = mid - 1
        elif arr[mid] < x:
            left = mid + 1
        mid = (left + right) // 2
    return -1
print(binary_search(10))