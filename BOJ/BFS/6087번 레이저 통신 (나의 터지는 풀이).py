from collections import deque, defaultdict
m,n = map(int, input().split())
A = []
for _ in range(n):
    A.append([i for i in input()])
# visited = [[[[-1]*4 for _ in range((m+1)*(n+1))] for _ in range(m)] for _ in range(n)]
# visited = [[-1]*m for _ in range(n)]
visited = defaultdict(int)
razor = []
for i in range(n):
    for j in range(m):
        if A[i][j] == 'C':
            # A[i][j] = '.'
            razor.append((i,j))
(x,y), (w,z) = razor[0], razor[1]
# print(x,y,w,z)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
# (x,y,거울의 개수,방향)까지 가는 최소 거리.
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m and A[nx][ny] == '.':
        visited[(nx,ny,0,i)] = 1
        q.append((nx,ny,0,i))
# (위치, 거울의 개수, 방향) -> 방향이 -1이면 맨 처음인 경우임.
# 방향은 위, 아래, 왼쪽, 오른쪽이 차례대로
# -> 0,1,2,3
while q:
    x,y,mir,d = q.popleft()
    # if (x,y) in [(2,12)]:
    #     print(x,y,mir,d,visited[x][y][mir])
    if A[x][y] == 'C':
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and A[nx][ny] == '.' and mir+1 < (n+1)*(m+1):
            # 거울 설치 안해도 되는 경우.
            if visited[(nx,ny,mir,i)] == 0:
                # 쌩 초반에 가는 곳이라면
                if d == -1:
                    q.append((nx,ny,mir,i))
                    visited[(nx,ny,mir,i)] = visited[(x,y,mir,d)]+1
                # 중간이라면
                else:
                    # 거울로 틀 수 없는 경우는
                    # 지금 바라보는 곳이 위인데 다음 동작이 아래이거나
                    # 지금 바라보는 곳이 오른쪽인데 다음 동작이 왼쪽이거나
                    if (d == 0 and i == 1) or (d == 1 and i == 0) or \
                        (d == 2 and i == 3) or (d == 3 and i == 2):
                        continue
                    # 거울 필요 없는 경우는 -> 방향 틀지 않는 경우
                    if d == i:
                        q.append((nx,ny,mir,i))
                        visited[(nx,ny,mir,i)] = visited[(x,y,mir,d)] + 1
            # 거울 설치하는 경우.
            if d != -1 and visited[(nx,ny,mir+1,i)] == 0:
                # 거울로 틀어야하는 곳이라면
                if (d in [0, 1] and i in [2, 3]) or (d in [2, 3] and i in [0, 1]):
                    q.append((nx, ny, mir + 1, i))
                    visited[(nx,ny,mir+1,i)] = visited[(x,y,mir,d)] + 1
ans = 1e100
result = []
for i in range(4):
    nw = w + dx[i]
    nz = z + dy[i]
    if 0 <= nw < n and 0 <= nz < m:
        for key in visited.keys():
            a,b,c,d = key
            if (a,b) != (nw,nz):
                continue
            if ans >= c:
                ans = c
                result.append(key)
            # values = visited[(key)]
            # for indx,dist in enumerate(values):
            #     if sum([i != -1 for i in dist]) >= 1 and ans > indx:
            #         ans = indx
            #         x = nw
            #         y = nz
            #         break
# print(visited[0][12])
# print(visited[1][12])
# print(visited[2][12])
# print(visited[3][12])
# print(visited[4][12])
# print(visited[4][13])
# print(visited[9][13])
# print(visited[9][5])
# print(visited[8][5])
# print(visited[8][4])
# print(visited[8][3])
# print(visited[8][2])
# print(visited[8][1])
# print(visited[8][0])
"""
15 10
...*...***.C..* 
.*.*.*........* 
.*...*...*....* 
.*.*....****.** 
.*..**........* 
.**..********.* 
.*...*...*..*.* 
.**..***.*.**.* 
C........*..... 
..***.......... 
"""
final_ans = []
for ele in result:
    x, y, mir, d = ele
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx,ny) == (w,z):
            if (d in [0,1] and i in [2,3]) or (d in [2,3] and i in [0,1]):
                final_ans.append(ans+1)
            else:
                final_ans.append(ans)
print(min(final_ans))
