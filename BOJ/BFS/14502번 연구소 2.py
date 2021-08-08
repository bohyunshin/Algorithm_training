from itertools import combinations
from copy import deepcopy
n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
# candidate: 벽을 세울 후보 위치. 바이러스도 없고 벽도 없는 부분.
# virus: 바이러스의 위치
candidate = []
virus = []
for i in range(n):
    for j in range(m):
        if A[i][j] == 0:
            candidate.append((i,j))
        if A[i][j] == 2:
            virus.append((i,j))
            # 현재 바이러스의 위치가 2로 되어있는데,
            # 그냥 얘네들을 모두 0으로 해주고 바이러스 위치에서 시작할때,
            # 1로 방문처리를 해줌.
            A[i][j] = 0
walls = []
# 벽을 3개 세울거니까 3개씩 뽑아서 Brute Force로 모든 경우를 확인해줌.
for c in combinations(candidate,3):
    walls.append(c)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# virus가 방문했으면 2, 아니면 0
def dfs(x,y):
    if R[x][y] != 0:
        return
    R[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            dfs(nx,ny)
answer = -1
# 세울 수 있는 벽의 모든 경우의 수에 대해서 진행해줌.
for wall in walls:
    safe = 0
    R = deepcopy(A)
    for i,j in wall:
        R[i][j] = 1
    for (i,j) in virus:
        dfs(i,j)
    for i in range(n):
        for j in range(m):
            if R[i][j] == 0:
                safe += 1
    if answer < safe:
        answer = safe
print(answer)