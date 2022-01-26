import sys
sys.setrecursionlimit(10**5)
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
# 빙산 모두 녹았는지 확인하는 함수.
def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] >= 1:
                return True
    return False
# 빙산 조각 수를 구하기 위한 dfs 함수.
def dfs(x,y,num):
    # -1이 아니라면 방문한 것이므로 return
    if visited[x][y] != -1:
        return
    visited[x][y] = num
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] >= 1:
            dfs(nx,ny,num)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
t = 0
# 빙산이 모두 녹지 않았을 때,
while check():
    # 빙산이 얼마나 녹아야하는지, 그 높이를 담은 배열.
    melt = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            cnt = 0
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                    cnt += 1
            melt[x][y] = cnt
    # melt 배열을 이용해서 빙산 녹히기.
    for x in range(n):
        for y in range(m):
            a[x][y] = max(a[x][y]-melt[x][y], 0)
    visited = [[-1]*m for _ in range(n)]
    num = 0
    # 빙산을 녹혔으니 dfs 함수를 통해 빙산 조각 수 알아보기.
    for x in range(n):
        for y in range(m):
            if a[x][y] >= 1 and visited[x][y] == -1:
                dfs(x,y,num)
                num += 1
    t += 1
    # 만약 빙산 조각의 개수가 2개 였다면, num은 2에서 끝났으니
    # 아래와 같은 조건으로 프로그램을 종료.
    if num >= 2:
        print(t)
        exit()
print(0)

"""
3 3
0 0 0
0 0 0
0 0 0
"""