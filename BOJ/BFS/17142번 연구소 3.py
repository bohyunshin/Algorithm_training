from collections import deque
from itertools import combinations
n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
virus = []
for i in range(n):
    for j in range(n):
        if A[i][j] == 2:
            virus.append((i,j))
            A[i][j] = 0
ans = 1e100
for c in combinations(virus,m):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    # 바이러스 활성화시키기.
    for x,y in c:
        q.append((x,y))
        visited[x][y] = 0
        A[x][y] = 2
    # 그 이외의 바이러스는 비활성화 = 벽으로 만들기.
    nonactive = list(set(virus) - set(c))
    for x,y in nonactive:
        A[x][y] = -2
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and A[nx][ny] != 1:
                if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    MAX_time = -1
    FLAG = False
    for i in range(n):
        for j in range(n):
            if (A[i][j] == 0 or A[i][j] == 2) and visited[i][j] >= 0:
                MAX_time = max(MAX_time, visited[i][j])
            if A[i][j] == 0 and visited[i][j] == -1:
                FLAG = True
    if FLAG == False:
        ans = min(ans,MAX_time)
    # 다음 차례를 위해 바이러스 다시 빼두기.
    for x,y in c:
        A[x][y] = 0
    # non active virus도 다시 빈칸으로 만들어두기.
    for x,y in nonactive:
        A[x][y] = 0
print(-1 if ans == 1e100 else ans)

"""
5 1
0 0 0 0 0
0 0 0 0 0
0 0 2 0 0
0 0 0 0 0
0 0 0 0 0

5 1
0 0 0 0 0
0 0 1 0 0
0 1 2 1 0
0 0 1 0 0
0 0 0 0 0

5 2
0 0 0 0 2
0 0 0 1 0
0 0 2 1 0
0 0 0 1 0
0 0 0 1 0

5 1
0 0 0 1 2
0 0 0 1 0
0 0 2 1 0
0 0 0 1 0
0 0 0 1 0

5 2
1 1 1 1 1
1 1 2 1 1
1 1 2 1 1
1 1 1 1 1
1 1 1 1 1

5 1
1 1 1 1 1
1 1 2 1 1
1 1 2 1 1
1 1 1 1 1
1 1 1 1 1

5 1
2 2 2 1 1
0 1 1 1 1
2 1 1 1 1
2 1 1 1 1
2 2 2 1 1

5 1
2 2 2 1 1
0 1 1 1 1
2 1 1 1 1
0 1 1 1 1
2 2 2 1 1

5 1
2 2 2 1 1
0 1 1 1 1
2 1 1 1 1
2 1 1 1 1
0 2 2 1 1

<반례>!!!
비활성 바이러스를 벽으로 두지 않는 것이었음.
5 2
2 2 2 1 1
0 1 1 1 1
2 1 1 1 1
2 1 1 1 1
0 2 2 1 1
"""