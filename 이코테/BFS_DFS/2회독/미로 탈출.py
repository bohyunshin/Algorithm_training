from collections import deque

n,m = map(int, input().split())
array = []

for _ in range(n):
    array.append( [int(i) for i in input()] )
visited = [[0]*(m) for _ in range(n)]
distance = [[-100]*(m) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

distance[0][0] = 1
q = deque()
q.append((0,0))

while q:
    x,y = q.popleft()
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if array[nx][ny] == 0:
            continue
        if distance[nx][ny] == -100 or distance[nx][ny] > distance[x][y] + 1:
            distance[nx][ny] = distance[x][y] + 1
            q.append((nx,ny))
print(distance[n-1][m-1])