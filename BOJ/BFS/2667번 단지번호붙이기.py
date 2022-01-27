from collections import defaultdict
n = int(input())
a = []
for _ in range(n):
    tmp = [int(i) for i in input()]
    a.append(tmp)
visited = [[-1]*n for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y,cnt):
    if visited[x][y] != -1:
        return
    visited[x][y] = cnt
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 1:
            dfs(nx,ny,cnt)
cnt = 1
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and visited[i][j] == -1:
            dfs(i,j,cnt)
            cnt += 1
ans = defaultdict(int)
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and visited[i][j] != -1:
            ans[visited[i][j]] += 1
tmp = []
for k in ans.keys():
    tmp.append(ans[k])
tmp.sort()
print(len(tmp))
for i in tmp:
    print(i)