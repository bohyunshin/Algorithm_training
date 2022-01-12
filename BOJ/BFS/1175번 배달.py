from collections import deque
n,m = map(int,input().split())
a = [input() for _ in range(n)]
c = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            x,y = i,j
        if a[i][j] == 'C':
            c.append((i,j))
visited = [[[[-1]*4 for _ in range(4)] for _ in range(m)] for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = deque()
for i in range(4):
    visited[x][y][i][2] = 0
    q.append((x,y,i,2))
ans = -1
while q:
    x,y,d,state = q.popleft()
    if state == 3:
        ans = visited[x][y][d][state]
        break
    for i in range(4):
        if i == d:
            continue
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] != '#':
            if a[nx][ny] == 'C':
                index = c.index((nx, ny))
                if state == 2 and visited[nx][ny][i][index] == -1:
                    visited[nx][ny][i][index] = visited[x][y][d][state] + 1
                    q.append((nx,ny,i,index))
                elif state in [0,1] and state != index and visited[nx][ny][i][3] == -1:
                    visited[nx][ny][i][3] = visited[x][y][d][state] + 1
                    q.append((nx, ny, i, 3))
            else:
                if visited[nx][ny][i][state] == -1:
                    visited[nx][ny][i][state] = visited[x][y][d][state] + 1
                    q.append((nx,ny,i,state))
print(ans)