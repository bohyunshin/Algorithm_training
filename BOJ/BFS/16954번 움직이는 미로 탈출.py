from collections import deque
n = 8
a = [input() for _ in range(n)]
wall = [ [ [] for _ in range(n) ] for _ in range(n)]
init = []
start = (n-1,0)
end = (n-1,n-1)
for i in range(n):
    for j in range(n):
        if a[i][j] == '#':
            init.append((i,j))
            wall[i][j].append(0)
def move_wall():
    for x,y in init:
        t = 0
        wall[x][y].append(t)
        while True:
            x += 1
            if 0 <= x < n and 0 <= y < n:
                t += 1
                wall[x][y].append(t)
            else:
                break
move_wall()
def bfs_ook():
    q = deque()
    visited = [[-1]*n for _ in range(n)]
    dx = [-1, 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, -1, 1, 1, 1, -1, -1]
    x,y = start
    stay = False
    q.append((x,y,stay,0))
    visited[x][y] = 0
    while q:
        x,y,stay,stay_time = q.popleft()
        if stay:
            time = stay_time
        else:
            time = visited[x][y]
        if (x,y) == end:
            print(1)
            exit()
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and \
                 time + 1 not in wall[nx][ny] and \
                 time not in wall[nx][ny]:
                q.append((nx,ny,False,0))
                visited[nx][ny] = time + 1
        if time + 1 not in wall[x][y]:
            q.append((x,y,True,time+1))
bfs_ook()
print(0)

"""
........
........
........
........
........
########
.#......
........

#.......
##......
##......
##......
##......
########
.#......
........
"""