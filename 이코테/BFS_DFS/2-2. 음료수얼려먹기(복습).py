n,m = map(int, input().split())
array = []
for _ in range(n):
    array.append( list(map(int, input())) )

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(graph, x, y):
    if graph[x][y] == 1:
        return False
    graph[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1:
            continue

        dfs(graph, nx, ny)

        # return True
    return True
count = 0
for i in range(n):
    for j in range(m):
        if dfs(array, i, j) == True:
            count += 1
print(count)
print(array)