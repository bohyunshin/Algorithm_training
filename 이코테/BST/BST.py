# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     else:
#         return binary_search(array, target, mid+1, end)

def binary_search(array, targer, start, end):

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            star = mid+1
    return None

n, target = map(int, input().split())
array = [1,3,5,7,9,11,13,15,17,19]

result = binary_search(array, target, 0, len(array)-1)
if result is None:
    print('결과없음')
else:
    print(result)