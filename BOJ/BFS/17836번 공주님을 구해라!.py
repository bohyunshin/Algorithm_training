from collections import deque
n,m,t = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited[0][0][0] = 0
q = deque()
# x,y,그람 소유 여부.
q.append((0,0,0))
while q:
    x,y,g = q.popleft()
    if x == n-1 and y == m-1:
        if visited[x][y][g] <= t:
            print(visited[x][y][g])
        else:
            print('Fail')
        exit()
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][g] == -1:
            if g == 1:
                visited[nx][ny][g] = visited[x][y][g]+1
                q.append((nx,ny,g))
            else:
                if A[nx][ny] == 0:
                    visited[nx][ny][g] = visited[x][y][g] + 1
                    q.append((nx, ny, g))
                elif A[nx][ny] == 2:
                    visited[nx][ny][1] = visited[x][y][g] + 1
                    q.append((nx,ny,1))
print('Fail')