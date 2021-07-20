from collections import deque

n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i] = sorted(graph[i])

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] is False:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in graph[x]:
            if visited[i] is False:
                visited[i] = True
                q.append(i)

dfs(graph, v, [False]*(n+1))
print()

bfs(graph, v, [False]*(n+1))

