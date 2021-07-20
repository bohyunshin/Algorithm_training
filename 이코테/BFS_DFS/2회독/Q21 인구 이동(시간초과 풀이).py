n,l,r = map(int,input().split())
import sys
sys.setrecursionlimit(100000)
array = []
for _ in range(n):
    array.append( list(map(int,input().split())) )


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,v,cnt,first=False):
    global union
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if union[x][y] == 0:
        if l <= abs(v-array[x][y]) <= r or first:
            union[x][y] = cnt
        else:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny,array[x][y],cnt)
    return True
moving = 0
while True:
    cnt = 1
    union = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result = dfs(i,j,array[1][0],cnt,first=True)
            if result:
                cnt += 1
    d_union = {}
    d_loc = {}

    for i in range(n):
        for j in range(n):
            u = union[i][j]
            try:
                d_union[u].append(array[i][j])
                d_loc[u].append((i,j))
            except:
                d_union[u] = []
                d_union[u].append(array[i][j])

                d_loc[u] = []
                d_loc[u].append((i, j))
    if len(d_union.keys()) == n*n:
        break

    for key in d_union.keys():
        if len(d_union[key]) == 1:
            continue
        else:
            mean_ = sum(d_union[key]) // len(d_union[key])
        for x,y in d_loc[key]:
            array[x][y] = mean_

    moving += 1
print(moving)

