from collections import deque

n = int(input())
r1,c1,r2,c2 = map(int, input().split())

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
dp = {}
for i in range(n):
    for j in range(n):
       dp[(i,j)] = {(k,l):1e100 for k in range(n) for l in range(n)}
# dp 초기값 설정
for i in range(len(dx)):
    nx = 0 + dx[i]
    ny = 0 + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
        dp[(0,0)][(nx,ny)] = 1
print(dp)

# q = deque()
# visited = [[-1]*n for _ in range(n)]
# q.append((r1,c1))
# visited[r1][c1] = 0
#
# while q:
#     x,y = q.popleft()
#
#     if x == r2 and y == c2:
#         break
#
#     for i in range(len(dx)):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if visited[nx][ny] == -1 or visited[nx][ny] > visited[x][y] + 1:
#                 visited[nx][ny] = visited[x][y] + 1
#                 q.append((nx,ny))
# print(visited[r2][c2])