from collections import defaultdict
n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    if visited[x][y]:
        return
    visited[x][y] = True
    slices[cnt].append((x,y))
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 1 <= nx < n-1 and 1 <= ny < m-1 and a[nx][ny] == 0:
            dfs(nx,ny)
def is_hole_in_cheese(locs):
    for x,y in locs:
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if (nx,ny) not in locs and a[nx][ny] == 0:
                return False
    return True
def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                return True
    return False
while check():
    visited = [[False] * m for _ in range(n)]
    slices = defaultdict(list)
    cheese = []
    cnt = 0
    for x in range(1,n-1):
        for y in range(1,m-1):
            if visited[x][y] == False and a[x][y] == 0:
                dfs(x, y)
                cnt += 1
            if a[x][y] == 1:
                cheese.append((x,y))
    hole_in_cheese = []
    for i in slices.keys():
        locs = slices[i]
        if is_hole_in_cheese(locs):
            hole_in_cheese += locs
    cheese_disappear = []
    for x,y in cheese:
        flag = False
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if a[nx][ny] == 0 and (nx,ny) not in hole_in_cheese:
                flag = True
        if flag:
            cheese_disappear.append((x,y))
            print(x,y)

    break