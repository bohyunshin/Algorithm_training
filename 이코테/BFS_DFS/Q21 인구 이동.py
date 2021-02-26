from collections import deque
N,L,R = map(int,input().split())
A = []

for _ in range(N):
    A.append(list(map(int, input().split())))

if N==1:
    print(0)
    exit(0)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

moving = 0

while True:
    visited = [[0] * N for _ in range(N)]
    index = 1
    for x in range(N):
        for y in range(N):
            whether_moving = 0
            if visited[x][y] != 0:
                continue
            q = deque()
            q.append((x, y))
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= N or ny >= N:
                        continue
                    if visited[nx][ny] != 0:
                        continue
                    if L <= abs(A[nx][ny] - A[x][y]) <= R:
                        visited[nx][ny] = index
                        q.append((nx, ny))
                        whether_moving += 1

            if whether_moving != 0:

                index += 1
    print(visited)
    alliance2loc = {}
    for i in range(N):
        for j in range(N):
            v = visited[i][j]
            if v == 0:
                continue
            else:
                try:
                    alliance2loc[v].append((i,j))
                except:
                    alliance2loc[v] = []
                    alliance2loc[v].append((i, j))
    if len(alliance2loc.keys()) == 0:
        break
    else:
        moving += 1
        for k in alliance2loc.keys():
            population = 0
            for x,y in alliance2loc[k]:
                population += A[x][y]
            for x,y in alliance2loc[k]:
                A[x][y] = population // len(alliance2loc[k])
print(moving)