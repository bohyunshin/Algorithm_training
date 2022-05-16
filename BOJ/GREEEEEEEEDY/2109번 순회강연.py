import heapq
n = int(input())
a = []
v = -1
for _ in range(n):
    p,d = map(int,input().split())
    v = max(v,d)
    a.append((d,p))
for i in range(1,v+1):
    a.append((i,))
a.sort(key = lambda x: (-x[0]))
q = []
ans = 0
for i in range(len(a)):
    if len(a[i]) == 2:
        d,p = a[i]
        heapq.heappush(q,-p)
    elif len(q) >= 1:
        p = heapq.heappop(q)
        ans += -p
print(ans)
"""
index error 반례.
1
1 10
"""
# if len(a) == 1:
#     print(a[0][0])
#     exit()
# ans = 0
# val,take = a[0]
# for i in range(1,n):
#     p,d = a[i]
#     if take == d:
#         val = max(val,p)
#     else:
#         ans += val
#         val = p
#         take = d
#     if i == n-1:
#         ans += val
# print(ans)