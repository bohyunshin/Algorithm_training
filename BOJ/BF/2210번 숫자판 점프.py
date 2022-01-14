n = 5
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
ans = set()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def go(index,n,x,y,start):
    if index == n:
        ans.add(str(start) + ''.join(map(str,num)))
        return
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            num[index] = a[nx][ny]
            go(index+1,n,nx,ny,start)
for x in range(n):
    for y in range(n):
        num = [0] * n
        go(0,n,x,y,a[x][y])
print(len(ans))