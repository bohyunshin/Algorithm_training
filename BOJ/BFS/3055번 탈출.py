from collections import deque, defaultdict
n,m = map(int,input().split())
a = [input() for _ in range(n)]
water = [[1e100]*m for _ in range(n)]
init = []
rock = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            water[i][j] = 0
            init.append((i,j))
        if a[i][j] == 'D':
            water[i][j] = 1e100
            end = (i,j)
        if a[i][j] == 'S':
            start = (i,j)
        if a[i][j] == 'X':
            water[i][j] = 1e100
def bfs():
    q = deque()
    visited = [[False]*m for _ in range(n)]
    for x,y in init:
        q.append((x,y))
        visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and \
                visited[nx][ny] == False and a[nx][ny] not in ['*','X','D']:
                visited[nx][ny] = True
                q.append((nx,ny))
                water[nx][ny] = water[x][y] + 1
bfs()
def bfs_goseum():
    q = deque()
    visited = [[-1]*m for _ in range(n)]
    x,y = start
    q.append((x,y))
    visited[x][y] = 0
    while q:
        x,y = q.popleft()
        if (x,y) == end:
            print(visited[x][y])
            exit()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if (0 <= nx < n and 0 <= ny < m and a[nx][ny] != 'X' and \
                visited[nx][ny] == -1 and visited[x][y] + 1 < water[nx][ny]) or (nx,ny) == end:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
    print('KAKTUS')
bfs_goseum()