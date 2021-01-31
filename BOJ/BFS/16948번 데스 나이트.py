from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

array = []
for _ in range(n):
    array.append([0]*n)

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

def bfs(array, x, y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if array[nx][ny] == 0 or array[nx][ny] > array[x][y]+1:
                array[nx][ny] = array[x][y]+1
                q.append((nx,ny))
    return -1 if array[r2][c2] == 0 else array[r2][c2]
print(bfs(array, r1, c1))