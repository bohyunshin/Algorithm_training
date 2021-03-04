import heapq
n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap,int(input()))
result = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_val = one+two
    heapq.heappush(heap,sum_val)
    result += sum_val
print(result)