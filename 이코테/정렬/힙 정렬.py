import heapq
arr = [8,3,2,9,7,1,5,4]
def heap_sort(arr):
    h = []
    result = []
    for i in arr:
        heapq.heappush(h,i)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
print(heap_sort(arr))