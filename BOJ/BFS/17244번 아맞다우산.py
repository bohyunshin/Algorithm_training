from itertools import permutations
from collections import deque
m,n = map(int,input().split())
A = []
for _ in range(n):
    A.append([i for i in input()])
stuff = []
for i in range(n):
    for j in range(m):
        if A[i][j] == 'X':
            stuff.append((i,j))
        if A[i][j] == 'S':
            start = (i,j)
        if A[i][j] == 'E':
            end = (i,j)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y,a,b):
    visited = [[-1]*m for _ in range(n)]
    q = deque()
    visited[x][y] = 0
    q.append((x,y))
    while q:
        x,y = q.popleft()
        if x == a and y == b:
            return visited[a][b]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and A[nx][ny] != '#' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
ans = 1e100
for p in permutations(stuff):
    tmp = 0
    p = [start] + [(x,y) for x,y in p] + [end]
    for i in range(len(p)-1):
        (x,y),(a,b) = p[i],p[i+1]
        tmp += bfs(x,y,a,b)
    ans = min(ans,tmp)
print(ans)
