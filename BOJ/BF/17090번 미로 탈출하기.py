import sys
sys.setrecursionlimit(10**5)
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(input())
way = [[-1]*m for _ in range(n)]
d = {'U':(-1,0),'R':(0,1),'D':(1,0),'L':(0,-1)}
# def go(x,y,path):
#     if not (0 <= x < n and 0 <= y < m):
#         for sx,sy in path:
#             way[sx][sy] = 1
#         # ans += 1
#         return
#     if way[x][y] != -1:
#         for sx,sy in path:
#             way[sx][sy] = way[x][y]
#         return
#     if visited[x][y]:
#         for sx,sy in path:
#             if way[x][y] == -1:
#                 way[sx][sy] = 0
#             else:
#                 way[sx][sy] = way[x][y]
#         return
#     visited[x][y] = True
#     path.append((x,y))
#     dx,dy = d[a[x][y]]
#     nx,ny = x+dx,y+dy
#     go(nx,ny,path.copy())

def go2(x,y,path):
    if not (0 <= x < n and 0 <= y < m):
        way[x][y] = 1
        return
    if way[x][y] != -1:
        return
    way[x][y] = 0
    dx,dy = d[a[x][y]]
    nx,ny = x+dx,y+dy
    go2(nx,ny,path.copy())



for i in range(n):
    for j in range(m):
        if way[i][j] == -1:
            go2(i,j,[])
ans = 0
for i in range(n):
    for j in range(m):
        if way[i][j] >= 1:
            ans += way[i][j]
print(ans)

# for i in way:
#     print(i)

# n, m = map(int, input().split())
# s = [input() for _ in range(n)]
# d = [[-1] * m for _ in range(n)]
#
#
# def go(x, y):
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return 1
#     if d[x][y] != -1:
#         return d[x][y]
#     d[x][y] = 0
#     if s[x][y] == 'R':
#         d[x][y] = go(x, y + 1)
#     elif s[x][y] == 'L':
#         d[x][y] = go(x, y - 1)
#     elif s[x][y] == 'U':
#         d[x][y] = go(x - 1, y)
#     else:
#         d[x][y] = go(x + 1, y)
#
#     return d[x][y]
#
#
# for i in range(n):
#     for j in range(m):
#         if d[i][j] == -1:
#             go(i, j)
#
# ans = 0
# for i in range(n):
#     for j in range(m):
#         if d[i][j] == 1:
#             ans += 1
#
# print(ans)