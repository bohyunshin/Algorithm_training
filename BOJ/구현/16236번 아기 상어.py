from collections import deque

def eatable_fish(space,baby_shark_size):
    n = len(space)
    result = []
    for i in range(n):
        for j in range(n):
            if 1 <= space[i][j] < baby_shark_size:
                result.append((i,j))
    return result

def bfs(space,baby_shark_loc,baby_shark_size,fish_list):
    n = len(space)
    visited = [[-1]*n for _ in range(n)]
    q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    x,y = baby_shark_loc
    q.append((x,y))
    visited[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and \
                visited[nx][ny] == -1 and baby_shark_size >= space[nx][ny]:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
    MIN_DIST = 1e100
    MIN_DIST_fish_list = []
    for x,y in fish_list:
        if visited[x][y] != -1 and MIN_DIST > visited[x][y]:
            MIN_DIST = visited[x][y]
    for x,y in fish_list:
        if visited[x][y] == MIN_DIST:
            MIN_DIST_fish_list.append((x,y))
    MIN_DIST_fish_list.sort(key=lambda x: (x[0],x[1]))
    if MIN_DIST == 1e100:
        return [],1e100
    else:
        return MIN_DIST_fish_list[0],MIN_DIST

n = int(input())
space = []
for _ in range(n):
    space.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            baby_shark_loc = (i,j)
            space[i][j] = 0
            break
baby_shark_size = 2
fish_list = eatable_fish(space,baby_shark_size)
eaten_size = 0
total_time = 0
while len(fish_list) != 0:
    eaten_fish, time = bfs(space,baby_shark_loc,baby_shark_size,fish_list)
    if time == 1e100:
        break
    else:
        total_time += time
        eaten_size += 1
        # 물고기 빈칸 만들기.
        x,y = eaten_fish
        space[x][y] = 0
        # 아기 상어 키우기.
        if baby_shark_size == eaten_size:
            baby_shark_size += 1
            eaten_size = 0
        # 아기 상어 위치 옮기기.
        baby_shark_loc = x,y
        fish_list = eatable_fish(space,baby_shark_size)
print(total_time)