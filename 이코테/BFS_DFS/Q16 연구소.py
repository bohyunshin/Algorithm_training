from itertools import combinations
from copy import deepcopy
from collections import deque
n,m = map(int,input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 벽을 세울 수 있는 빈칸의 위치 뽑아내기인
# 바이러스 위치 봅아내기
candi_walls = []
virus = []
for i in range(n):
    for j in range(m):
        if array[i][j] == 0:
            candi_walls.append((i,j))
        if array[i][j] == 2:
            virus.append((i,j))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = []
for c in combinations(candi_walls,3):
    array_copy = deepcopy(array)
    # 벽 세우기
    for wall in c:
        x,y = wall
        array_copy[x][y] = 1
    # 바이러스 퍼뜨리기
    # 각 바이러스별로 bfs 실행
    for v in virus:
        x,y = v
        q = deque()
        q.append((x,y))

        while q:
            x,y = q.popleft()
            # 상하좌우로 이동하는데
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위 벗어나면 패스
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                # 벽이 아니거나 바이러스가 퍼지지 않았다면
                # 바이러스를 퍼뜨림
                if array_copy[nx][ny] == 0:
                    array_copy[nx][ny] = 2
                    q.append((nx,ny))
    safety = 0
    for i in range(n):
        for j in range(m):
            if array_copy[i][j] == 0:
                safety += 1
    result.append(safety)
print(max(result))
