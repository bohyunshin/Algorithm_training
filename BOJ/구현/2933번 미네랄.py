from collections import deque
from copy import deepcopy
r,c = map(int,input().split())
A = []
for _ in range(r):
    A.append([1 if i == 'x' else 0 for i in input()])
n = int(input())
height = list(map(int,input().split()))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    visited = [[False]*c for _ in range(r)]
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cluster = [(x,y)]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == False and A[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx,ny))
                cluster.append((nx,ny))
    return cluster
def check(cluster,A):
    A = deepcopy(A)
    # cluster를 한 칸 아래로 움직일 수 있는지 알아보는 함수임.
    # cluster를 움직여봄.
    moved_cluster = []
    for x,y in cluster:
        nx,ny = x+1,y
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            return False
        if 0 <= nx < r and 0 <= ny <= c:
            A[nx][ny] += 1
            A[x][y] -= 1
            moved_cluster.append((nx,ny))
    # 확인해서 미네랄이 2인 곳이 있으면 옮길 수 없는 경우임.
    for x,y in moved_cluster:
        if A[x][y] >= 2:
            return False
    return True
def move(cluster,A):
    while check(cluster,A):
        moved_cluster = []
        for x,y in cluster:
            nx,ny = x+1,y
            A[nx][ny] += 1
            A[x][y] -= 1
            moved_cluster.append((nx,ny))
        cluster = moved_cluster[:]
    return A
for i,h in enumerate(height):
    if i%2 == 0:
        y = 0
        d = 1
    else:
        y = c-1
        d = -1
    h = r-h
    ny = y
    for j in range(c):
        y = ny + d*j
        # 미네랄을 만날 때까지 창을 이동시킴.
        if A[h][y] == 0:
            continue
        # 미네랄을 만난 경우에, 우선 그곳의 미네랄을 파괴시켜야 함.
        A[h][y] -= 1
        # 파괴한 후에, 모든 좌표와 연관된 클러스터를 확인함.
        visited = [[False]*c for _ in range(r)]
        FLAG = False
        for x in range(r):
            for y in range(c):
                if A[x][y] == 1 and visited[x][y] == False:
                    cluster = bfs(x,y)
                    # 우선 해당 클러스터를 방문처리 해줌.
                    for k,l in cluster:
                        visited[k][l] = True
                    # 이 클러스터를 이동시킬 수 있으면 이동 시킴.
                    if check(cluster,A):
                        A = move(cluster,A)
                        FLAG = True
                        break
            if FLAG:
                break
        # 미네랄 만나고 창은 떨어진다.
        break
for k in range(r):
    print(''.join(['.' if i == 0 else 'x' for i in A[k]]))

"""
7 7
.......
..xx...
...x...
...x...
...x...
...x...
.xxx...
4
2 2 2 2
"""
# cluster = bfs(1,2)
# for i in move(cluster,A):
#     print(i)