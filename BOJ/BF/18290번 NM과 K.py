n,m,k = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
b = [[False]*m for _ in range(n)]
a = [0]*k

ans = -1e100

def check(x,y):
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if b[nx][ny]:
                return False
    return True

def go(index,k,px,py):
    global ans
    if index == k:
        if ans < sum(a):
            ans = sum(a)
        return
    for r in range(px,n):
        if r == px:
            pass
        else:
            py = 0
        for c in range(py,m):
            if b[r][c]:
                continue
            if check(r,c) == False:
                continue
            b[r][c] = True
            a[index] = A[r][c]
            go(index+1,k,r,c)
            b[r][c] = False

go(0,k,0,0)
print(ans)

"""
2 3 3
5 4 100
1 1 1000

2 3 3
5 4 1000
1 1 1000
"""
