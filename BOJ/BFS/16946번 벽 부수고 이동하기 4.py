import sys
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append([int(i) for i in input()])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[-1]*m for _ in range(n)]
answer = [[0]*m for _ in range(n)]
grp2cnt = {}
def dfs(x,y):
    global cnt
    if visited[x][y] >= 1 or A[x][y] == 1:
        return
    visited[x][y] = grp
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            dfs(nx,ny)
grp = 0
for i in range(n):
    for j in range(m):
        cnt = 0
        if A[i][j] == 0 and visited[i][j] == -1:
            grp += 1
            dfs(i,j)
            grp2cnt[grp] = cnt

for x in range(n):
    for y in range(m):
        if A[x][y] == 1:
            tmp = []
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] != -1 and visited[nx][ny] not in tmp:
                        tmp.append(visited[nx][ny])
                        answer[x][y] += grp2cnt[visited[nx][ny]]
            answer[x][y] += 1

            answer[x][y] %= 10

for l in answer:
    print(''.join(list(map(str, l))))
