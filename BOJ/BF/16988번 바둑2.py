from collections import defaultdict
from itertools import combinations
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
black = defaultdict(list)
zero = []
visited = [[-1]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
def dfs(x,y):
    if visited[x][y] != -1:
        return
    visited[x][y] = cnt
    black[cnt].append((x,y))
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and \
                visited[nx][ny] == -1 and a[nx][ny] == 2:
            dfs(nx,ny)
def baduk(loc):
    for x,y in loc:
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0:
                    return 0
    return len(loc)
for x in range(n):
    for y in range(m):
        if visited[x][y] == -1 and a[x][y] == 2:
            dfs(x,y)
            cnt += 1
        if a[x][y] == 0:
            zero.append((x,y))
ans = -1
for c in combinations(zero,2):
    for x,y in c:
        a[x][y] = 1
    tmp = 0
    for i in black.keys():
        tmp += baduk(black[i])
    if ans == -1 or ans < tmp:
        ans = tmp
    for x,y in c:
        a[x][y] = 0
print(ans)
"""
3 3
2 2 2
2 2 2
1 2 0
"""