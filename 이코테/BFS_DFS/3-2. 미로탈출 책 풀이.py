from collections import deque
n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append( list(map(int, input())) )

# 상 하 좌 우 정의
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 파이썬 인덱스를 위해 문제의 시작은 (1,1)이지만 코드상으로는 (0,0)으로 대입
x = 0
y = 0

def bfs(graph, x, y):

    queue = deque()
    queue.append( (x,y) )
    while queue:
        x, y = queue.popleft()
        # 상하좌우를 돌며 인접한 애들을 찾는다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로찾기 공간에서 벗어난다면
            # 무시함
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 만약 괴물이 있다면
            # 탐색하지 않음
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문 하는 경우에, (bfs를 생각해보라)
            # 위 두가지에 모두 해당이 안된다면
            # 큐에 추가하고 방문 처리함
            # 여기서 방문 처리를 그 이전 graph[][] 값에 1을 더해줌
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    return graph[n-1][m-1]
print(bfs(graph,x,y))