n = int(input())
arr = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))
arr.sort()
def binary_search(x):
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2
    while left <= right:
        if arr[mid] == x:
            return 1
        elif arr[mid] > x:
            right = mid-1
        else:
            left = mid+1
        mid = (left+right) // 2
    return 0
for i in num:
    print(binary_search(i), end=' ')