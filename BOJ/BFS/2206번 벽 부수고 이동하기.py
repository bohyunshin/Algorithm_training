from collections import deque
n,m = map(int, input().split())
array = []
for _ in range(n):
    array.append(list(map(int, input())))
c = [[[-1]*2 for _ in range(m)] for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((0,0,0))
    # x, y는 좌표이고 z가 0이라면 벽을 안 뜷은 상태, 1이라면 뚫은 상태임
    # 시작좌표는 (0,0)이고 벽을 아직 안 뚫었으니 z=0
    c[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 밖에 있다면 나간다.
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 현재 상태에서 벽이 없고 최초 방문이라면
            if array[nx][ny] == 0 and c[nx][ny][z] == -1:
                c[nx][ny][z] = c[x][y][z] + 1
                q.append((nx, ny, z))
            # 현재 상태가 벽이 있고, 벽을 뚫지 않았으면 벽을 뚫어보는 것임
            # 벽을 안 뚫으면 (z=0) 원래 방문하지 않은 상태가 유지
            elif array[nx][ny] == 1 and z == 0 and c[nx][ny][z+1] == -1:
                c[nx][ny][z+1] = c[x][y][z] + 1
                q.append((nx, ny, z+1))
bfs()
ans1, ans2 = c[n-1][m-1][0], c[n-1][m-1][1]
if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))

