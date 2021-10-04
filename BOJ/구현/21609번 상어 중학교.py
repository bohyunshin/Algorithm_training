from collections import defaultdict
from copy import deepcopy
n,m = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
ans = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y,color):
    global cnt
    if visited[x][y]:
        return
    visited[x][y] = True
    loc[cnt].append((x,y))
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and \
            A[nx][ny] not in [-1,-2] and A[nx][ny] in [color,0]:
            dfs(nx,ny,color)

def reverse_rainbow(r):
    global visited
    for x,y in r:
        visited[x][y] = False

while True:
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    loc = defaultdict(list)
    r = []
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:
                r.append((i, j))
    # 가장 큰 블록 찾기.
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and A[i][j] not in [-1,-2] and A[i][j] != 0:
                dfs(i,j,A[i][j])
                cnt += 1
                reverse_rainbow(r)
    criteria_block = {}
    for k in loc.keys():
        if len(loc[k]) >= 2:
            tmp = [(x,y) for x,y in loc[k] if A[x][y] != 0]
            tmp.sort(key=lambda x: (x[0],x[1]))
            criteria = tmp[0]
            criteria_block[criteria] = loc[k]
    if len(criteria_block.keys()) == 0:
        break
    # Step 1
    tmp = []
    for c in criteria_block.keys():
        block = criteria_block[c]
        rainbow = 0
        for x,y in block:
            if A[x][y] == 0:
                rainbow += 1
        a = []
        a.append(len(block))
        a.append(rainbow)
        a += list(c)
        tmp.append(a)
    # print(criteria_block)
    tmp.sort(key=lambda x: (-x[0],-x[1],-x[2],-x[3]))
    # print(tmp)
    block_sel = criteria_block[tmp[0][2],tmp[0][3]]
    # print(block_sel)
    # Step 2
    for x,y in block_sel:
        A[x][y] = -2
    ans += len(block_sel)**2
    # Step 3
    for _ in range(n):
        for i in range(n-1):
            for j in range(n):
                if A[i][j] not in [-1,-2]:
                    if A[i+1][j] == -2:
                        A[i+1][j] = A[i][j]
                        A[i][j] = -2
    # Step 4
    A_rotate = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n-1,-1,-1):
            A_rotate[n-j-1].append(A[i][j])
    A = deepcopy(A_rotate)
    # Step 5
    for _ in range(n):
        for i in range(n-1):
            for j in range(n):
                if A[i][j] not in [-1,-2]:
                    if A[i+1][j] == -2:
                        A[i+1][j] = A[i][j]
                        A[i][j] = -2
    # for i in A:
    #     print(i)
    # print()
print(ans)