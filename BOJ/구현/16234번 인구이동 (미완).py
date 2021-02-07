n, l, r = map(int, input().split())
graph = []
status = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    status.append([0]*n)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs_original(graph, status, x, y, result, coordinate):
    if x < 0 or y < 0 or x >= n or y >= n:
        return status, result, False
    if status[x][y] != 0:
        # 방문 처리
        status[x][y] = 0
        result.append(graph[x][y])
        coordinate.append((x,y))

        dfs_original(graph, status, x-1, y, result, coordinate)
        dfs_original(graph, status, x+1, y, result, coordinate)
        dfs_original(graph, status, x, y-1, result, coordinate)
        dfs_original(graph, status, x, y+1, result, coordinate)

        return status, result, True
    return status, result, False

def dfs(graph, status, x,y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return

    a = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if status[nx][ny] == 1:
            continue
        if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
            status[nx][ny] = 1
            a += 1
            dfs(graph,status,nx,ny)

    if a != 0:
        status[x][y] = 1
    return graph, status

count = 0
graph_ = []
for g in graph:
    graph_.append(g.copy())

while True:
    status_ = []
    for g in status:
        status_.append(g.copy())
    for i in range(n):
        for j in range(n):
            graph_, status_ = dfs(graph_,status_,i,j)
    union = []
    pop_sum = []

    tmp = 0
    for g in status_:
        tmp += sum(g)
    if tmp == 0:
        print(count)
        break
    else:
        count += 1
        result = []
        union = []
        coordinate = []
        for i in range(n):
            for j in range(n):
                status_, result, FIN = dfs_original(graph_, status_, i, j, result, coordinate)
                if FIN is True:
                    for cor in coordinate:
                        x = cor[0]
                        y = cor[1]
                        graph_[x][y] = int(sum(result)/len(result))
                    result = []
                    union = []
                    coordinate = []
        print(graph_)



        #         if status_[i][j] == 1:
        #             union.append((i,j))
        #             pop_sum.append(graph_[i][j])
        # print(int(sum(pop_sum) / len(pop_sum)))
        # print(pop_sum)
        # for i in union:
        #     x,y = i[0], i[1]
        #     graph_[x][y] = int(sum(pop_sum) / len(pop_sum))
        # print(graph_)