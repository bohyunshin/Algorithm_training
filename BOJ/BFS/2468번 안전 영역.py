import sys
sys.setrecursionlimit(10**5)
n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
MAX = -1
for i in range(n):
    for j in range(n):
        if MAX == -1 or a[i][j] > MAX:
            MAX = a[i][j]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    global cnt
    if visited[x][y] != -1:
        return
    visited[x][y] = cnt
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] > rain:
            dfs(nx,ny)
ans = 0
# 비가 안내리는 경우도 있음!!
for rain in range(0,MAX):
    visited = [[-1]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > rain and visited[i][j] == -1:
                dfs(i,j)
                cnt += 1
    tmp = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1 and visited[i][j]+1 > tmp:
                tmp = visited[i][j]+1
    if ans == 0 or ans < tmp:
        ans = tmp
print(ans)