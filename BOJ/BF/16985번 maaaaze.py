from copy import deepcopy
from itertools import permutations
from collections import deque
n = 5
def rotate(a):
    ans = []
    for j in range(n):
        col = []
        for i in range(n):
            col.append(a[i][j])
        ans.append(col[::-1])
    return ans
def bfs(maze):
    x,y,z = (0,0,0)
    visited = [[[-1]*n for _ in range(n)] for _ in range(n)]
    q = deque()
    visited[x][y][z] = 0
    q.append((x,y,z))
    while q:
        x,y,z = q.popleft()
        # if (x,y,z) == end:
        #     return visited[x][y][z]
        for i in range(6):
            nx,ny,nz = x+dx[i],y+dy[i],z+dz[i]
            if 0 <= nx < n and 0 <= ny < n and 0 <= nz < n and \
                    visited[nx][ny][nz] == -1 and maze[nx][ny][nz] == 1:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append((nx,ny,nz))
    return visited[n-1][n-1][n-1]
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
maze = []
for _ in range(n):
    tmp = []
    for i in range(n):
        tmp.append(list(map(int,input().split())))
    maze.append(tmp)
ans = -1
rotate_possible = []
cnt = [0,1,2,3]
lst = [-1]*5
def go(index):
    if index == 5:
        rotate_possible.append(lst.copy())
        return
    for i in range(4):
        lst[index] = i
        go(index+1)
go(0)

for p in permutations(range(5)):
    tmp = []
    for k in p:
        tmp.append(maze[k])
    for pos in rotate_possible:
        maze_rotated = []
        for i in range(len(pos)):
            m = tmp[i]
            for _ in range(pos[i]):
                m = rotate(m)
            maze_rotated.append(m)
        if maze_rotated[0][0][0] == 0 or maze_rotated[n-1][n-1][n-1] == 0:
            continue
        dist = bfs(maze_rotated)
        if dist == -1:
            continue
        if ans == -1 or ans > dist:
            ans = dist

print(ans)

"""
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 1
0 0 0 0 1
0 0 0 0 1
0 0 0 0 1
"""
