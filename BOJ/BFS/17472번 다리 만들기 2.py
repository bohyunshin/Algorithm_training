#!/usr/bin/python3
from collections import deque
n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
group = [[0]*m for _ in range(n)]
groups = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
edges = []
ans = -1
a = [[0]*10 for _ in range(10)]
check = []
bridge = [[0]*10 for _ in range(10)]
def bfs(x, y):
    global groups
    groups += 1
    q = deque()
    group[x][y] = groups
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx,ny))
                    group[nx][ny] = groups
def dfs(x):
    for y in range(1, groups+1):
        if a[x][y] > 0 and check[y] == False:
            check[y] = True
            dfs(y)
def go(index, s):
    # edges[index] o/x
    if index == len(edges):
        global check
        check = [False]*(groups+1)
        check[1] = True
        dfs(1)
        for i in range(1, groups+1):
            if check[i] == False:
                return
        global ans
        if ans == -1 or ans > s:
            ans = s
        return
    u, v, cost = edges[index]
    a[u][v] = a[v][u] = cost
    go(index+1, s+cost)
    a[u][v] = a[v][u] = 0
    go(index+1, s)

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and group[i][j] == 0:
            bfs(i, j)

# bridge[i][j] > 0 i -> j length
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            continue
        # (i, j) -> ... -> (x, y)
        for k in range(4):
            length = 0
            x, y = i+dx[k], j+dy[k]
            while 0 <= x < n and 0 <= y < m:
                if board[x][y] == 0:
                    pass
                elif group[x][y] == group[i][j]:
                    break
                else:
                    if length >= 2:
                        g1 = group[i][j]
                        g2 = group[x][y]
                        if bridge[g1][g2] == 0 or bridge[g1][g2] > length:
                            bridge[g1][g2] = length
                            bridge[g2][g1] = length
                    break
                x += dx[k]
                y += dy[k]
                length += 1

for i in range(1, groups+1):
    for j in range(i+1, groups+1):
        if bridge[i][j] > 0:
            edges.append((i,j,bridge[i][j]))

go(0, 0)
print(ans)


# from itertools import combinations
# from collections import defaultdict, deque
# n,m = map(int,input().split())
# a = []
# for _ in range(n):
#     a.append(list(map(int,input().split())))
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# island = defaultdict(list)
# visited = [[-1]*m for _ in range(n)]
# cnt = 0
# def dfs(x,y):
#     if visited[x][y] != -1:
#         return
#     visited[x][y] = cnt
#     island[cnt].append((x,y))
#     for i in range(4):
#         nx,ny = x+dx[i],y+dy[i]
#         if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
#             dfs(nx,ny)
# def bfs(init_x,init_y,number):
#     q = deque()
#     v = [[-1]*m for _ in range(n)]
#     q.append((init_x,init_y,-1))
#     v[init_x][init_y] = 0
#     route = []
#     ways = []
#     while q:
#         x,y,d = q.popleft()
#         if visited[x][y] != -1 and visited[x][y] != number:
#             if v[x][y]-1 <= 1:
#                 continue
#             if (number,visited[x][y]) in ways:
#                 continue
#             ways.append((number,visited[x][y]))
#             route.append((v[x][y]-1,d,(init_x,init_y),(x,y)))
#             continue
#         for i in range(4):
#             nx,ny = x+dx[i],y+dy[i]
#             if d == -1:
#                 pass
#             elif d != i:
#                 continue
#             if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == -1 and \
#                     ( a[nx][ny] == 0 or (a[nx][ny] == 1 and visited[nx][ny] != -1 and visited[nx][ny] != number) ):
#                 q.append((nx,ny,i))
#                 v[nx][ny] = v[x][y] + 1
#     return route
# def check(x,y):
#     if v[x][y]:
#         return
#     v[x][y] = True
#     for i in range(4):
#         nx,ny = x+dx[i],y+dy[i]
#         if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
#             if visited[nx][ny] != -1:
#                 l[visited[nx][ny]] = True
#             dfs(nx,ny)
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 1 and visited[i][j] == -1:
#             dfs(i,j)
#             cnt += 1
# routes = []
# for isl in island.keys():
#     for x,y in island[isl]:
#         routes += bfs(x,y,isl)
# ans = -1
# xx,yy = island[0][0]
# for k in range(1,len(routes)+1):
#     for c in combinations(routes,k):
#         tmp = 0
#         v = [[False]*m for _ in range(n)]
#         l = [False]*len(island.keys())
#         for dist,d,(x,y),(z,w) in c:
#             tmp += dist
#             while not (x == z and y == w):
#                 x += dx[d]
#                 y += dy[d]
#                 a[x][y] = 1
#         for i in a:
#             print(i)
#         print()
#         check(xx,yy)
#         if sum(l) == len(island.keys()):
#             if ans == -1 or ans > tmp:
#                 ans = tmp
#         for dist,d,(x,y),(z,w) in c:
#             while not (x == z and y == w):
#                 x += dx[d]
#                 y += dy[d]
#                 a[x][y] = 0
#
#     #         for i in a:
#     #             print(i)
#     #         break
#     #     break
#     # break
#         # if sum(check) == len(island.keys()):
#         #     if dist == -1 or dist > tmp:
#         #         dist = tmp
#         #         print(c)
# print(ans)