from collections import deque
n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append([int(i) for i in input()])
visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 초기 상태는 벽을 0개 부순 상태임.
# (0,0)까지 벽을 0개 부셨을 때 최단 거리를 의미.
visited[0][0][0] = 0
q = deque()
q.append((0,0,0))
while q:
    x,y,w = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if A[nx][ny] == 1 and w == 0:
                # visited[nx][ny][w+1] > visited[x][y][w] + 1
                if visited[nx][ny][w+1] == -1:
                    visited[nx][ny][w+1] = visited[x][y][w] + 1
                    q.append((nx,ny,w+1))
            if A[nx][ny] == 0:
                if visited[nx][ny][w] == -1 or visited[nx][ny][w] > visited[x][y][w] + 1:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    q.append((nx,ny,w))
if max(visited[n-1][m-1]) == -1:
    print(-1)
else:
    print(min([i for i in visited[n-1][m-1] if i != -1]) + 1)