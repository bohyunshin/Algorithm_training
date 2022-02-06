from collections import deque
n = 5
m = 7
a = []
for _ in range(n):
    a.append([i for i in input()])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
check = [[False]*n for _ in range(n)]
student = ['']*m
# def bfs(x,y):
#     cnt = 0
#     q = deque()
#     visited = [[[-1]*8 for _ in range(n)] for _ in range(n)]
#     if a[x][y] == 'S':
#         q.append((x,y,1))
#         visited[x][y][1] = 0
#     else:
#         q.append((x,y,0))
#         visited[x][y][0] = 0
#     while q:
#         x,y,S = q.popleft()
#         if visited[x][y][S]+1 == 7:
#             if S >= 4:
#                 print(x,y,S)
#                 cnt += 1
#             continue
#         for i in range(4):
#             nx,ny = x+dx[i],y+dy[i]
#             if 0 <= nx < n and 0 <= ny < n:
#                 if a[nx][ny] == 'S':
#                     nS = S+1
#                 else:
#                     nS = S
#                 if visited[nx][ny][nS] == -1 and check[nx][ny] == False:
#                     q.append((nx,ny,nS))
#                     visited[nx][ny][nS] = visited[x][y][S] + 1
#     return cnt
# print(bfs(1,0))
ans = 0
def go(x,y,index):
    global ans
    if index == m:
        print(student)
        S = 0
        Y = 0
        for k in range(m):
            if student[k] == 'S':
                S += 1
            else:
                Y += 1
        if S >= 4:
            ans += 1
        return
    student[index] = a[x][y]
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and check[nx][ny] == False:
            go(nx,ny,index+1)
student[0] = a[1][0]
go(1,0,1)
print(ans)

# ans = 0
# for i in range(n):
#     for j in range(n):
#         ans += bfs(i,j)
#         check[i][j] = True
# print(ans)