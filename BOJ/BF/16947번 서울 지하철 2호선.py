from collections import deque
n = int(input())
graph = [[]*(n+1) for _ in range(n+1)]
visited = [[-1]*(n+1) for _ in range(n+1)]
for i in range(n):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
