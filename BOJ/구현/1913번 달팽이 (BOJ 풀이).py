dx = [0,1,0,-1]
dy = [1,0,-1,0]
n = int(input())
m = int(input())
a = [[0]*n for _ in range(n)]
x = y = 0
a[x][y] = n*n
k = 0
for i in range(n*n-1,0,-1):
    nx,ny = x+dx[k],y+dy[k]
    if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 0:
        pass
    else:
        k = (k+1)%4
        nx,ny = x+dx[k],y+dy[k]
    a[nx][ny] = i
    x,y = nx,ny
for i in a:
    print(' '.join(list(map(str,i))))
for i in range(n):
    for j in range(n):
        if a[i][j] == m:
            print(i,j,end=' ')
            break
