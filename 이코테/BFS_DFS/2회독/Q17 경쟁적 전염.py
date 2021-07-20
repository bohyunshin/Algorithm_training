from copy import deepcopy

n,k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append( list(map(int, input().split())) )
s,x,y = map(int, input().split())

# 0초라면 현재 위치의 바이러스 출력
if s == 0:
    print(graph[x-1][y-1])
    exit(0)

vir2loc = {}
for i in range(1,k+1):
    vir2loc[i] = []

visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        else:
            vir2loc[ graph[i][j] ].append((i,j))
            visited[i][j] = 1

def dfs(graph,x,y,k):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] != 0:
            continue

        graph[nx][ny] = k
        vir2loc[k].append((nx,ny))
        visited[nx][ny] = 1
    return graph

time = 0

next_loc = {}
while True:
    # 순차적으로 번호를 돌며 감염을 시킨다.
    for i in range(1,k+1):
        vir_list = vir2loc[i].copy()
        for a,b in vir_list:
            if visited[a][b] != 0:
                graph = dfs(graph,a,b,i)
    time += 1
    # print(graph)
    # print(vir2loc)
    # print()

    if time == s:
        break

    a = 0
    for l in visited:
        a += sum(l)
    if a == n*n:
        break

if graph[x-1][y-1] == 0:
    print(0)
else:
    print(graph[x-1][y-1])