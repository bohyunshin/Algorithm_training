from collections import deque
n,m = map(int,input().split())
map_ = []
for _ in range(n):
    map_.append(input())
def bfs(x,y):
    q = deque()
    visited = [[-1]*m for _ in range(n)]
    q.append((x,y))
    visited[x][y] = 0
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    ans = -1
    while q:
        x,y = q.popleft()
        if ans == -1 or ans < visited[x][y]:
            ans = visited[x][y]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and \
                    visited[nx][ny] == -1 and map_[nx][ny] == 'L':
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y]+1
    return ans
ans = -1
for i in range(n):
    for j in range(m):
        if map_[i][j] == 'L':
            tmp = bfs(i,j)
            if ans == -1 or ans < tmp:
                ans = tmp
print(ans)