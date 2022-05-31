n = int(input())
arr = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))
arr.sort()
def lower_bound(x):
    left = 0
    right = len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            ans = mid
            right = mid-1
        elif arr[mid] > x:
            right = mid-1
        else:
            left = mid + 1
    return ans
def upper_bound(x):
    left = 0
    right = len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            ans = mid
            left = mid+1
        elif arr[mid] > x:
            right = mid-1
        else:
            left =  mid+1
    return ans
for i in num:
    left,right = lower_bound(i),upper_bound(i)
    if left == -1:
        print('0', end=' ')
    else:
        print(right-left+1, end=' ')