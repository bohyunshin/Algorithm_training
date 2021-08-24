import sys
sys.setrecursionlimit(10**6)
n = int(input())
A = []
for _ in range(n):
    A.append(input())
B = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if A[i][j] in ['R','G']:
            B[i][j] = 'R'
        else:
            B[i][j] = 'b'

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y,color,A):
    if visited[x][y] != 0:
        return True
    visited[x][y] = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and A[nx][ny] == color:
            dfs(nx, ny, color, A)
    return True

visited = [[0]*n for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            if dfs(i,j,A[i][j],A):
                cnt += 1
a = -1
for i in range(n):
    for j in range(n):
        a = max(a,visited[i][j])

visited = [[0]*n for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            if dfs(i,j,B[i][j],B):
                cnt += 1
b = -1
for i in range(n):
    for j in range(n):
        b = max(b,visited[i][j])
print(a,b)
