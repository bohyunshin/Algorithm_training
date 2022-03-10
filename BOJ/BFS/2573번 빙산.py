import sys
from collections import deque
sys.setrecursionlimit(10**4)

n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                elif a[nx][ny] == 0:
                    melt[x][y] += 1
    return 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
t = 0
check = False

while True:
    visited = [[False]*m for _ in range(n)]
    melt = [[0]*m for _ in range(n)]
    result = 0
    # 덩어리 파악.
    for x in range(n):
        for y in range(m):
            if a[x][y] != 0 and visited[x][y] == False:
                result += bfs(x,y)
    # 빙산 녹이기.
    for x in range(n):
        for y in range(m):
            a[x][y] = max(a[x][y] - melt[x][y], 0)

    if result == 0:
        break
    if result >= 2:
        check = True
        break
    t += 1
if check:
    print(t)
else:
    print(0)

# # 빙산이 모두 녹지 않았을 때,
# while check():
#     # 빙산이 얼마나 녹아야하는지, 그 높이를 담은 배열.
#     melt = [[0]*m for _ in range(n)]
#     for x in range(n):
#         for y in range(m):
#             cnt = 0
#             for i in range(4):
#                 nx,ny = x+dx[i],y+dy[i]
#                 if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
#                     cnt += 1
#             melt[x][y] = cnt
#     # melt 배열을 이용해서 빙산 녹히기.
#     for x in range(n):
#         for y in range(m):
#             a[x][y] = max(a[x][y]-melt[x][y], 0)
#     visited = [[-1]*m for _ in range(n)]
#     num = 0
#     # 빙산을 녹혔으니 dfs 함수를 통해 빙산 조각 수 알아보기.
#     for x in range(n):
#         for y in range(m):
#             if a[x][y] >= 1 and visited[x][y] == -1:
#                 dfs(x,y,num)
#                 num += 1
#     t += 1
#     # 만약 빙산 조각의 개수가 2개 였다면, num은 2에서 끝났으니
#     # 아래와 같은 조건으로 프로그램을 종료.
#     if num >= 2:
#         print(t)
#         exit()
# print(0)
#
# """
# 3 3
# 0 0 0
# 0 0 0
# 0 0 0
# """