from collections import deque
import sys
input = sys.stdin.readline

n,m,k,x = map(int, input().split())
array = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    array[a].append(b)

dist = [-100]*(n+1)
dist[x] = 0
q = deque([x])
while q:
    x = q.popleft()
    for v in array[x]:
        if dist[v] == -100 or dist[v] > dist[x]+1:
            dist[v] = dist[x]+1
            q.append(v)
result = [i for i,d in enumerate(dist) if d==k ]
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in result:
        print(i)