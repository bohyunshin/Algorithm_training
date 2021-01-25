from collections import deque
from itertools import combinations

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph, start, end):
    q = deque()
    q.append((start,end))

    while q:
        x,y = q.popleft()

        if graph[x][y] == 2:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if graph[nx][ny] == 1:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    q.append((nx,ny))
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                result += 1
    return result

def dfs(graph, x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return graph
    if graph[x][y] == 1:
        return graph
    a = 0
    if graph[x][y] == 0:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                pass
            else:
                if graph[nx][ny] == 2:
                    graph[x][y] = 2
                    a += 1

    if a == 0:
        return graph

    if graph[x][y] == 2:

        dfs(graph, x-1, y)
        dfs(graph, x+1, y)
        dfs(graph, x, y-1)
        dfs(graph, x, y+1)
        return graph
# for i in range(n):
#     for j in range(m):
#         a = dfs(graph, i,j)
# print(a)

# 벽을 세울 수 있는 위치를 뽑아냄
location = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            location.append((i,j))

safe_zone = []

v = {}
for loc in combinations(location, 3):
    tmp = []
    for i in graph:
        tmp.append(i.copy())
    v[loc] = tmp

# 벽세우고 바이러스 퍼뜨리기
for key in v.keys():

    graph = v[key]
    # print(graph)

    for wall in key:
        x = wall[0]
        y = wall[1]
        graph[x][y] = 1


    for i in range(n):
        for j in range(m):
            graph = dfs(graph,i,j)
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                result += 1
    safe_zone.append(result)

print(max(safe_zone))

