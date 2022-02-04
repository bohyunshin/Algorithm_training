import sys
sys.setrecursionlimit(10**4)
from collections import defaultdict, deque
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
islands = defaultdict(list)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*n for _ in range(n)]
island_map = [[-1]*n for _ in range(n)]
cnt = 0
def dfs(x,y):
    if visited[x][y]:
        return
    visited[x][y] = True
    island_map[x][y] = cnt
    islands[cnt].append((x,y))
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 1:
            dfs(nx,ny)
def bfs(x,y,number):
    q = deque()
    visited = [[-1]*n for _ in range(n)]
    q.append((x,y))
    visited[x][y] = 0
    while q:
        x,y = q.popleft()
        if island_map[x][y] > 0 and island_map[x][y] != number:
            return visited[x][y]-1
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and \
                    ( a[nx][ny] == 0 or (a[nx][ny] == 1 and island_map[nx][ny] > 0 and island_map[nx][ny] != number) ):
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
    return -1
for x in range(n):
    for y in range(n):
        if visited[x][y] == False and a[x][y] == 1:
            dfs(x,y)
            cnt += 1
ans = -1

for island in islands.keys():
    for x,y in islands[island]:
        dist = bfs(x,y,island)
        if dist == -1:
            continue
        if ans == -1 or ans > dist:
            ans = dist
print(ans)