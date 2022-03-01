import heapq
from collections import deque
n,m = map(int,input().split())
a = [deque(sorted(list(map(int,input().split())))) for _ in range(n)]

heap = []

min_val = int(1e9)
max_val = 0

for i in range(n):
    v = a[i].popleft()
    max_val = max(max_val, v)
    min_val = min(min_val, v)
    heapq.heappush(heap, (v,i))
s = max_val - min_val

while heap:
    prev_min_val, pos = heapq.heappop(heap)
    if not a[pos]:
        break
    new_val = a[pos].popleft()
    heapq.heappush(heap, (new_val, pos))
    if max_val < new_val:
        max_val = new_val
    min_val = heap[0][0]
    s = min(s, max_val - min_val)
print(s)


# visited = [[False]*m for _ in range(n)]
# a = [-1]*n
# ans = -1
# def go(index):
#     global ans
#     if index == n:
#         MAX = max(a)
#         MIN = min(a)
#         if ans == -1 or ans > MAX-MIN:
#             # print(a)
#             ans = MAX-MIN
#         return
#     for j in range(m):
#         a[index] = cap[index][j]
#         go(index+1)
# go(0)
# print(ans)