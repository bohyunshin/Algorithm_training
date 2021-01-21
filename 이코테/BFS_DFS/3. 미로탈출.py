from collections import deque

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [ [0]*m for _ in range(n) ]

def return_neighbor(graph, x, y):

    result = []
    # 상
    if x-1 != -1 and graph[x-1][y] == 1:
        result.append( (x-1, y) )
    # 하
    if x+1 != n and graph[x+1][y] == 1:
        result.append( (x+1, y) )
    # 좌
    if y-1 != -1 and graph[x][y-1] == 1:
        result.append( (x, y-1) )
    # 우
    if y+1 != m and graph[x][y+1] == 1:
        result.append( (x, y+1) )
    return result

def bfs(graph, x, y, visited):

    # 파이썬 인덱스를 위해 1씩 빼줌
    x -= 1
    y -= 1

    queue = deque([(x, y)])
    # 방문했다고 표시해줌
    visited[x][y] = 1
    # 방문한 횟수를 더해줌
    graph[x][y] += 1
    # 첫번째 칸도 세어줌
    block = 1

    while queue:
        # 큐에서 가장 먼저 들어온 애를 popup
        tup = queue.popleft()
        x = tup[0]
        y = tup[1]

        # 방문 칸수를 늘려줌
        block += 1
        print(x,y)
        # 얘와 인접한 애들을 뽑는다
        # 얘네를 큐에 추가시키고다 만약 탐색이
        # 안되었다면 탐색했다고 처리한다
        neighbors = return_neighbor(graph, x, y)
        for neighbor in neighbors:
            x_n = neighbor[0]
            y_n = neighbor[1]
            if visited[x_n][y_n] != 1:
                # 큐에 추가함
                queue.append( (x_n, y_n) )
                # 방문했다고 표시해줌
                visited[x_n][y_n] = 1
                # 방문한 횟수를 더해줌
                graph[x_n][y_n] = block
bfs(graph, 1, 1, visited)
print(graph)
