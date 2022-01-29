from collections import deque
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append([int(i) for i in input()])
visited = [[-1]*m for _ in range(n)]
q = deque()
visited[0][0] = 1
q.append((0,0))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while q:
    x,y = q.popleft()
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and a[nx][ny] == 1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))
print(visited[n-1][m-1])