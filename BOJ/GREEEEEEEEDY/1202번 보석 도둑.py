import heapq
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
l = []
q = []
for _ in range(n):
    m,v = map(int,input().split())
    l.append((m,v))
for _ in range(k):
    c = int(input())
    l.append((c,))
l.sort(key=lambda x: x[0])
ans = 0
for i in range(n+k):
    if len(l[i]) == 2:
        m,v = l[i]
        heapq.heappush(q,(-v,m))
    elif len(q) >= 1:
        v,m = heapq.heappop(q)
        v = -v
        ans += v
print(ans)

# while l:
#     v,m = heapq.heappop(l)
#     v = -v
#     to_add = []
#     flag = False
#     while True:
#         c = heapq.heappop(bag)
#         if m <= c:
#             flag = True
#             break
#         else:
#             to_add.append(c)
#
#         if len(bag) == 0:
#             break
#     if flag:
#         ans += v
#     for c in to_add:
#         heapq.heappush(bag,c)
#     if len(bag) == 0:
#         break
# print(ans)

"""
2 1
10000 1000
5000 500
4999
"""