n,m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

# def binary_serach(array, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     H = array[mid]
#
#     cut = [i-H for i in array[mid:]]
#
#     if sum(cut) == m:
#         return H
#     elif sum(cut) > m:
#         return binary_serach(array, mid+1, end)
#     else:
#         return binary_serach(array, start, mid-1)
# H = binary_serach(array, 0, len(array)-1)

def binary_search(array, start, end):
    while start <= end:
        H = (start + end) // 2
        cut = [i-H for i in array if i-H >= 0]

        if sum(cut) == m:
            return H
        elif sum(cut) > m:
            result = H
            start = H+1
        else:
            end = H-1
    return result
H = binary_search(array,0,max(array))
print(H)