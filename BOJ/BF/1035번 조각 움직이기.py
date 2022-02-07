from collections import deque, defaultdict
n = 5
a = []
for _ in range(n):
    a.append(input())
stars = []
for i in range(n):
    for j in range(n):
        if a[i][j] == '*':
            stars.append((i,j))
stars = tuple(stars)
def check(x,y):
    global conn
    for k in range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == False:
            if (nx,ny) in stars:
                v[nx][ny] = True
                conn += 1
                check(nx,ny)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = {}
q = deque()
visited[stars] = 0
q.append(stars)
while q:
    stars = q.popleft()
    conn = 1
    v = [[False] * n for _ in range(n)]
    sx, sy = stars[0]
    check(sx, sy)
    if conn == len(stars):
        print(stars)
        print(visited[stars])
        break
    for i in range(len(stars)):
        x,y = stars[i]
        for k in range(4):
            tmp = list(stars).copy()
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                tmp[i] = (nx,ny)
                tmp = tuple(sorted(list(tmp)))
                if tmp not in visited.keys():
                    visited[tmp] = visited[stars]+1
                    q.append(tmp)