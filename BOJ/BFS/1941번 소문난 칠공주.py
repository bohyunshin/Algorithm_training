from collections import deque
n = 5
m = 7
a = []
for _ in range(n):
    a.append([i for i in input()])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
check = [[False]*n for _ in range(n)]
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
ans = set()
def go(x,y,index,coord,here=False):
    global ans
    if index == m:
        # print(student)
        S = 0
        Y = 0
        for k in range(m):
            if student[k] == 'S':
                S += 1
            else:
                Y += 1
        if S >= 4:
            coord.sort()
            ans.add(tuple(coord))
        return
    if (x,y) in coord:
        return
    # if (x,y) == (2,1):
    #     print(coord)
    tmp = coord.copy()
    if here == False:
        student[index] = a[x][y]
    tmp.append((x,y))
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            go(nx,ny,index+1,tmp)

            # if (nx,ny) in coord:
            #     # go(x,y,index+1,tmp)
            #     pass
            # else:
            #     go(nx,ny,index+1,tmp)
    go(x,y,index+1,tmp,True)
student = ['']*m
go(1,0,0,[])
# for i in range(n):
#     for j in range(n):
#         student = ['']*m
#         go(i,j,0,[])
for i in ans:
    print(i)

# ans = 0
# for i in range(n):
#     for j in range(n):
#         ans += bfs(i,j)
#         check[i][j] = True
# print(ans)