from collections import deque
n,m = map(int,input().split())
A = []
def convert(x):
    x = int(x)
    if x >= 2:
        return 0
    else:
        return x
for _ in range(n):
    A.append(list(map(int,input().split())))
# 가만히 있는 경우까지 포함임.
dx = [-1,0,1,0,0]
dy = [0,1,0,-1,0]
bridges = []
for x in range(n):
    for y in range(n):
        if A[x][y] == 0:
            tmp = []
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0 <= nx < n and 0 <= ny < n and A[nx][ny] == 0:
                    tmp.append(i)
            tmp = set([j%2 for j in tmp])
            if len(tmp) == 1:
                bridges.append((x,y))
ans = 1e100
for a,b in bridges:
    A[a][b] = m
    x,y = 0,0
    # visited[i][j][k]: k초 경과 후에, 맵의 (i,j)까지 갔는지 여부를 알려줌.
    visited = [ [ [False]*201 for _ in range(n)] for _ in range(n)]
    q = deque()
    visited[x][y][0] = True
    q.append((x,y,0))
    while q:
        x,y,k = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and k+1 <= 200 and \
                visited[nx][ny][k+1] == False and A[nx][ny] >= 1:
                # 일반적으로 건널 수 있는 땅이라면,
                if A[nx][ny] == 1:
                    visited[nx][ny][k+1] = True
                    q.append((nx,ny,k+1))
                # 오작교가 놓여져 있더라면, 오작교의 주기에 맞게 건널 수 있는 타임이이어야함!!
                else:
                    if (k) % m == 0:
                        visited[nx][ny][k+1] = True
                        q.append((nx,ny,k+1))
    for time,b in enumerate(visited[n-1][n-1]):
        if b:
            ans = min(ans,time)
    print(visited[n-1][n-1])
    A[a][b] = 0
print(ans)
"""
5 5
1 1 1 1 0
0 6 0 0 0
1 1 0 1 0
1 1 0 1 0
1 1 0 1 0
"""