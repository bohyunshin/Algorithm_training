from collections import deque
n,m,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dice = {'h':[4,1,3,6], 'v':[2,1,5,6]}
map_direction = {0:2, 1:3, 2:0, 3:1}
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def move_dice(dice,d):
    h = dice['h'].copy()
    v = dice['v'].copy()
    if d == 0:
        v = v[1:] + [v[0]]
        h[1],h[3] = v[1],v[3]
    if d == 2:
        v = [v[-1]] + v[:3]
        h[1],h[3] = v[1],v[3]
    if d == 1:
        h = [h[-1]] + h[:3]
        v[1],v[3] = h[1],h[3]
    if d == 3:
        h = h[1:] + [h[0]]
        v[1],v[3] = h[1],h[3]
    return {'v':v, 'h':h}
def bfs(x,y):
    ans = []
    b = a[x][y]
    visited = [[False]*m for _ in range(n)]
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    ans.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and \
                visited[nx][ny] == False and a[nx][ny] == b:
                visited[nx][ny] = True
                q.append((nx,ny))
                ans.append((nx,ny))
    return b * len(ans)
x,y = 0,0
d = 1
score = 0
for _ in range(k):
    flag = 0
    nx,ny = x+dx[d],y+dy[d]
    if not (0 <= nx < n and 0 <= ny < m):
        d = map_direction[d]
        flag = 1
    if flag == 1:
        nx,ny = x+dx[d],y+dy[d]
    dice = move_dice(dice,d)
    A = dice['v'][3]
    B = a[nx][ny]
    if A > B:
        d = (d+1)%4
    elif A < B:
        d = (d-1)%4
    score += bfs(nx,ny)
    x,y = nx,ny
print(score)