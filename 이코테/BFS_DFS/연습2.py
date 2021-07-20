from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False]*9
start = 1

def dfs():
    s = []
    s.append(start)
    while s:
        node = s.pop()
        child = graph[node]
        if visited[node] is False:
            visited[node] = True
            print(node, end=' ')
            s.extend(child)
def bfs():
    q = deque()
    q.append(start)
    visited[start] = True
    print(start, end=' ')
    while q:
        x = q.popleft()
        for v in graph[x]:
            if visited[v] is False:
                visited[v] = True
                q.append(v)
                print(v,end=' ')
bfs()