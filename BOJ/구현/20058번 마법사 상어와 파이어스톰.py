import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)
n,q = map(int, input().split())
A = []
for _ in range(2**n):
    A.append(list(map(int, input().split())))
L = map(int, input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def concat_rowwise(matrices):
    ans = []
    for matrix in matrices:
        for row in matrix:
            ans.append(row)
    return ans

def concat_colwise(matrices):
    n = len(matrices[0])
    ans = [[] for _ in range(n)]
    for matrix in matrices:
        for i in range(n):
            ans[i] += matrix[i]
    return ans

def rotate(A):
    n = len(A)
    ans = [[] for _ in range(n)]
    for j in range(n):
        for i in range(n):
            ans[j].append(A[i][j])
    return [k[::-1] for k in ans]

# print(rotate([[1,2,3],[4,5,6],[7,8,9]]))

def firestorm_OneStep(A,l):
    m = 2**l
    if l == 0:
        return A
    n = len(A)
    ans = []
    for i in range(0,n,m):
        mat_list = []
        for j in range(0,n,m):
            tmp = [k[j:j+m] for k in A[i:i+m]]
            tmp = rotate(tmp)
            mat_list.append(tmp)
        ans.append(concat_colwise(mat_list))
    return concat_rowwise(ans)

def firestorm_TwoStep(A):
    n = len(A)
    ans = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            cnt = 0
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if A[x][y] >= 1 and 0 <= nx < n and 0 <= ny < n and A[nx][ny] >= 1:
                    cnt += 1
            if cnt <= 2 and A[x][y] >= 1:
                ans[x][y] = A[x][y]-1
            else:
                ans[x][y] = A[x][y]
    return ans

visited = [[False]*(2**n) for _ in range(2**n)]
def dfs(x,y,A):
    global cnt,ice
    if visited[x][y]:
        return
    visited[x][y] = True
    ice[cnt].append((x,y))
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < 2**n and 0 <= ny < 2**n and A[nx][ny] >= 1:
            dfs(nx,ny,A)
    return

for l in L:
    rotated = firestorm_OneStep(A,l)
    A = firestorm_TwoStep(rotated)
ans = 0
ice = defaultdict(list)
cnt = 0
for i in range(2**n):
    for j in range(2**n):
        ans += A[i][j]
        if visited[i][j] == False and A[i][j] != 0:
            dfs(i,j,A)
            cnt += 1
print(ans)
MAX_ICE = -1
for i in ice.keys():
    MAX_ICE = max(MAX_ICE,len(ice[i]))
print(0 if MAX_ICE == -1 else MAX_ICE)