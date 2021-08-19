from collections import deque
n = 8
A = []
for i in range(n):
    A.append(input())
wall = []
for i in range(n):
    for j in range(n):
        if A[i][j] == '#':
            wall.append((i,j))
visited = [[-1]*n for _ in range(n)]

dx = [-1,1,0,0,-1,1,1,-1]
dy = [0,0,-1,1,1,1,-1,-1]
stay = False

start = (7,0,wall,stay)
visited[7][0] = 0
q = deque()
q.append(start)

while q:
    x,y,wall,stay = q.popleft()
    moved_wall = []
    for i,j in wall:
        if 0 <= i+1 < n:
            moved_wall.append((i+1,j))
    all_wall = wall + moved_wall
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if (visited[nx][ny] == -1) and (nx,ny) not in all_wall:
                if stay is False:
                    visited[nx][ny] = visited[x][y] + 1
                else:
                    visited[nx][ny] = visited[x][y] + 2
                q.append((nx,ny,moved_wall,False))
    if (x,y) not in all_wall and len(all_wall) >= 1:
        q.append((x,y,moved_wall,True))
print(1 if visited[0][7] != -1 else 0)
print(visited[0][7])

"""
........
........
........
........
........
#.......
.#......
.#......
"""