from copy import deepcopy
n,m = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
direction = {
    1:[[0],[1],[2],[3]],
    2:[[0,2],[1,3]],
    3:[[0,1],[1,2],[2,3],[3,0]],
    4:[[3,0,1],[0,1,2],[1,2,3],[2,3,0]],
    5:[[0,1,2,3]]
}
lst = []
cctv = []
for i in range(n):
    for j in range(m):
        if 1 <= A[i][j] <= 5:
            lst.append(direction[A[i][j]])
            cctv.append((i,j))

def recursive(index,m,lst):
    global ans,a,order,c
    if index >= m:
        ans.append(a[:])
        return
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if i != index:
                continue
            if c[i][j] or order[i]:
                continue
            c[i][j] = True
            order[i] = True
            a[index] = lst[i][j]
            recursive(index+1,m,lst)
            c[i][j] = False
            order[i] = False

def main_recursive(lst):
    global ans,a,order,c
    n = len(lst)
    m = len(lst[0])
    ans = []
    a = [0]*n
    order = [False]*n
    c = []
    for i in range(n):
        c.append([False]*len(lst[i]))
    recursive(0,n,lst)
    return ans
if len(lst) == 0:
    ans = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                ans += 1
    print(ans)
    exit()
# for i in lst:
#     print(i)
methods = main_recursive(lst)
answer = 1e100
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for method in methods:
    A_cp = deepcopy(A)
    for i,lst in enumerate(method):
        x,y = cctv[i]
        for d in lst:
            nx,ny = x+dx[d],y+dy[d]
            while 0 <= nx < n and 0 <= ny < m and A_cp[nx][ny] != 6:
                if A_cp[nx][ny] != '#' and 1 <= A_cp[nx][ny] <= 5:
                    nx += dx[d]
                    ny += dy[d]
                    continue
                A_cp[nx][ny] = '#'
                nx += dx[d]
                ny += dy[d]
    tmp = 0
    for i in range(n):
        for j in range(m):
            if A_cp[i][j] == 0:
                tmp += 1
    if answer > tmp:
        answer = tmp
print(answer)

"""
CCTV가 0개인 경우 index error 처리해줘야 함.
3 3
0 0 0
6 6 0
0 0 6
"""