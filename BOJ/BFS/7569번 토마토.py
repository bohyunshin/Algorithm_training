from collections import deque
m,n,h = map(int,input().split())
a = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int,input().split())))
    a.append(tmp)
q = deque()
visited = [[[-1]*m for _ in range(n)] for _ in range(h)]
for k in range(h):
    for x in range(n):
        for y in range(m):
            if a[k][x][y] == 1:
                q.append((k,x,y))
                visited[k][x][y] = 0
direction = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
while q:
    k,x,y = q.popleft()
    for dh,dx,dy in direction:
        nk,nx,ny = k+dh,x+dx,y+dy
        if 0 <= nk < h and 0 <= nx < n and 0 <= ny < m and \
                a[nk][nx][ny] == 0 and visited[nk][nx][ny] == -1:
            visited[nk][nx][ny] = visited[k][x][y]+1
            q.append((nk,nx,ny))
day = 0
for k in range(h):
    for x in range(n):
        for y in range(m):
            if a[k][x][y] == 0:
                if visited[k][x][y] == -1:
                    print(-1)
                    exit()
                else:
                    day = max(day,visited[k][x][y])
print(day)