from collections import deque
n,m = map(int, input().split())
array= []
for _ in range(n):
    array.append( list(map(int, input())) )

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph, x, y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        # array[x][y] += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if array[nx][ny] == 0:
                continue
            if array[nx][ny] == 1:
                q.append((nx, ny))
                array[nx][ny] = array[x][y] + 1
    print(array[n-1][m-1])
bfs(array,0,0)