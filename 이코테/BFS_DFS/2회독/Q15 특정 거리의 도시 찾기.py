from collections import deque
import sys
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [-1000]*(n+1)

input = sys.stdin.readline
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

visited = [False]*(n+1)
q = deque()
q.append(x)
dist[x] = 0
visited[x] = True

while q:
    x = q.popleft()
    for v in graph[x]:
        if dist[v] > dist[x] + 1 or visited[v] is False:
            dist[v] = dist[x] + 1
            q.append(v)
            visited[v] = True
cnt = 0
for i,d in enumerate(dist):
    if d == k:
        print(i)
        cnt += 1
if cnt == 0:
    print(-1)