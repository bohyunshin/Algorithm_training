from collections import deque
m,n = map(int, input().split())
A = []
for _ in range(n):
    A.append([int(i) for i in input()])
visited = {}
q = deque()
start = (0,0)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
# wall
visited = [[1e100]*m for _ in range(n)]
visited[0][0] = 0
q.append(start)

while q:
    x,y = q.popleft()
    w = visited[x][y]
    # if x == n-1 and y == m-1:
    #     break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if A[nx][ny] == 0:
                if visited[nx][ny] == 1e100 or visited[nx][ny] > visited[x][y]:
                    visited[nx][ny] = visited[x][y]
                    q.append((nx,ny))
            else:
                if visited[nx][ny] == 1e100 or visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))

answer = 1e100
print(visited[n-1][m-1])
