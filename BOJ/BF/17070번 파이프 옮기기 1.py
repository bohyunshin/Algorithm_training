n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
ans = 0
dx = [0,1,1]
dy = [1,0,1]
def go(p1,p2,d):
    global ans
    if p2 == (n-1,n-1):
        ans += 1
        return
    x1, y1 = p1
    x2, y2 = p2
    # 가로로 놓여있다면.
    if d == 0:
        nx1,ny1 = x1,y1+1
        nx2,ny2 = x2,y2+1
        if 0 <= nx2 < n and 0 <= ny2 < n and a[nx2][ny2] == 0:
            go((nx1,ny1),(nx2,ny2),0)
        nx1,ny1 = x1,y1+1
        nx2,ny2 = x2+1,y2+1
        cnt = 0
        if 0 <= nx2 < n and 0 <= ny2 < n:
            for i in range(3):
                nnx2,nny2 = x2+dx[i],y2+dy[i]
                if a[nnx2][nny2] == 0:
                    cnt += 1
            if cnt == 3:
                go((nx1,ny1),(nx2,ny2),2)
    # 세로로 놓여있다면.
    if d == 1:
        nx1, ny1 = x1+1, y1
        nx2, ny2 = x2+1, y2
        if 0 <= nx2 < n and 0 <= ny2 < n and a[nx2][ny2] == 0:
            go((nx1, ny1), (nx2, ny2), 1)
        nx1, ny1 = x1+1, y1
        nx2, ny2 = x2+1, y2+1
        cnt = 0
        if 0 <= nx2 < n and 0 <= ny2 < n:
            for i in range(3):
                nnx2, nny2 = x2 + dx[i], y2 + dy[i]
                if a[nnx2][nny2] == 0:
                    cnt += 1
            if cnt == 3:
                go((nx1, ny1), (nx2, ny2), 2)
    # 대각선으로 놓여있다면.
    if d == 2:
        nx1, ny1 = x1+1, y1+1
        nx2, ny2 = x2, y2+1
        if 0 <= nx2 < n and 0 <= ny2 < n and a[nx2][ny2] == 0:
            go((nx1, ny1), (nx2, ny2), 0)

        nx1, ny1 = x1+1, y1+1
        nx2, ny2 = x2+1, y2
        if 0 <= nx2 < n and 0 <= ny2 < n and a[nx2][ny2] == 0:
            go((nx1, ny1), (nx2, ny2), 1)

        nx1, ny1 = x1+1, y1+1
        nx2, ny2 = x2+1, y2+1
        cnt = 0
        if 0 <= nx2 < n and 0 <= ny2 < n:
            for i in range(3):
                nnx2, nny2 = x2 + dx[i], y2 + dy[i]
                if a[nnx2][nny2] == 0:
                    cnt += 1
            if cnt == 3:
                go((nx1, ny1), (nx2, ny2), 2)
if a[n-1][n-1]:
    print(0)
else:
    go((0,0),(0,1),0)
    print(ans)