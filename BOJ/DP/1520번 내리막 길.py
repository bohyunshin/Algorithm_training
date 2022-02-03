n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
c = [[-1]*m for _ in range(n)]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1
    if c[x][y] != -1:
        return c[x][y]
    c[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] < a[x][y]:
                c[x][y] += dfs(nx, ny)
    return c[x][y]
print(dfs(0, 0))

# dp = [[0]*m for _ in range(n)]
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# def go(x,y,cnt):
#     if dp[x][y] != 0:
#         return dp[x][y]
#     # if x == n-1 and y == m-1:
#     #     return 1
#     dp[x][y] += cnt
#     for i in range(4):
#         nx,ny = x+dx[i],y+dy[i]
#         if 0 <= nx < n and 0 <= ny < m and a[x][y] > a[nx][ny]:
#             dp[nx][ny] += go(nx,ny,dp[x][y])
#     return dp[x][y]
# go(0,0,1)
# for i in dp:
#     print(i)