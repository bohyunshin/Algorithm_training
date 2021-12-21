from collections import deque
r,c = map(int,input().split())
A = []
for _ in range(r):
    A.append(list(map(int,input().split())))

x,y = 0,0
# corners = [(0,c-1),(r-1,0)]
# if r == 2 or c == 2:
#     ans = A[x][y]
#     d = 1
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     direction = ['U','R','D','L']
#     way1 = ''
#     while (x,y) != (r-1,c-1):
#         x += dx[d]
#         y += dy[d]
#         ans += A[x][y]
#         way1 += direction[d]
#         if (x,y) in corners:
#             d = (d+1)%4
#     # ans += A[x][y]
#
#     x,y = (0,0)
#     tmp = A[x][y]
#     d = 2
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
#     direction = ['U','L','D','R']
#     way2 = ''
#     while (x,y) != (r-1,c-1):
#         x += dx[d]
#         y += dy[d]
#         tmp += A[x][y]
#         way2 += direction[d]
#         if (x,y) in corners:
#             d = (d+1)%4
#     # tmp += A[x][y]
#
#     if ans > tmp:
#         print(way1)
#     else:
#         print(way2)
# else:
#     x,y = 0,0
#     d = 1
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#     direction = ['U','R','D','L']
#     way = ''
#     # while (x,y) != (r-1,c-1):
#     #     x += dx[d]
#     #     y += dy[d]
#     #     way += direction[d]
#     #
#     for i in range(r):
#         if i%2 == 0:
#             way += 'R'*(c-1)
#         else:
#             way += 'L'*(c-1)
#         way += 'D'
#     print(way[:-1])



def direction(d):
    if d == 0:
        return 'U'
    elif d == 1:
        return 'D'
    elif d == 2:
        return 'L'
    else:
        return 'R'

q = deque()
visited = [[-1]*c for _ in range(r)]
way = [['']*c for _ in range(r)]
history = [ [ [] for _ in range(c)] for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q.append((x,y))
visited[x][y] = A[x][y]
history[x][y].append((x,y))
while q:
    x,y = q.popleft()
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < r and 0 <= ny < c:
            if visited[nx][ny] == -1:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + A[nx][ny]
                way[nx][ny] = way[x][y] + direction(i)
                history[nx][ny] = history[x][y] + [(nx,ny)]
            else:
                if visited[nx][ny] < visited[x][y] + A[nx][ny] and \
                        (nx,ny) not in history[x][y]:
                    q.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y] + A[nx][ny]
                    way[nx][ny] = way[x][y] + direction(i)
                    history[nx][ny] = history[x][y] + [(nx, ny)]
print(way[r-1][c-1])