from collections import deque
from itertools import combinations

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
status = []
for g in graph:
    status.append( [0 if i != 1 else -1 for i in g] )

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 바이러스를 놓을 수 있는 곳을 기록
potential_virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            potential_virus.append((i,j))
            # 추후에 dfs 쉽게하려고 0으로 바꿔줌
            # 어차피 2인 지점은 저장했으니 상관 없음
            graph[i][j] = 0

v = {}
for loc in combinations(potential_virus, m):
    tmp = []
    for i in status:
        tmp.append(i.copy())
    v[loc] = tmp

# bfs 함수 정의
def bfs(status, start, end):
    q = deque()
    q.append((start, end))

    while q:
        x,y = q.popleft()

        if status[x][y] != -1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if status[nx][ny] == -1:
                    continue
                if status[nx][ny] == 0 or status[nx][ny] >= status[x][y] + 1:
                    status[nx][ny] = status[x][y] + 1
                    q.append((nx,ny))

    status[start][end] = 0
    return status

# 가능한 바이러스 위치에 대해서 bfs 실행
# brute force 임
result = []
for c in v.keys():
    status_copy = v[c]
    for point in c:
        x = point[0]
        y = point[1]
        status_copy[x][y] = 0
        status_copy = bfs(status_copy, x, y)

    flag = 0
    max_time = 0
    for i in range(n):
        for j in range(n):
            if (i, j) not in c and status_copy[i][j] == 0:
                flag += 1
                break
            else:
                if max_time < status_copy[i][j]:
                    max_time = status_copy[i][j]
        if flag >= 1:
            break

    if flag >= 1:
        result.append(-1)
    else:
        result.append(max_time)

if len(set(result)) == 1 and set(result) == {-1}:
    print(-1)
else:
    result = [i for i in result if i != -1]
    print(min(result))