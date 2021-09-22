from copy import deepcopy
n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
move = []
for _ in range(m):
    a,b = map(int,input().split())
    move.append((a-1,b))
cloud = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
dx_diag = [-1,-1,1,1]
dy_diag = [-1,1,1,-1]
for d,s in move:
    moved_cloud = []
    A_cp = deepcopy(A)
    for x,y in cloud:
        nx = x+s*dx[d]
        ny = y+s*dy[d]
        nx = (nx % n + n) % n
        ny = (ny % n + n) % n
        # 비내리기.
        A[nx][ny] += 1
        A_cp[nx][ny] += 1
        moved_cloud.append((nx,ny))
    for x,y in moved_cloud:
        cnt = 0
        for i in range(4):
            nx,ny = x+dx_diag[i],y+dy_diag[i]
            if 0 <= nx < n and 0 <= ny < n and A[nx][ny] >= 1:
                cnt += 1
        # 대각선에 물이 있는 개수만큼 물의 양이 증가.
        A_cp[x][y] += cnt
    A = deepcopy(A_cp)
    # 새로운 구름 만들기.
    cloud = []
    for i in range(n):
        for j in range(n):
            if (i,j) not in moved_cloud and A[i][j] >= 2:
                cloud.append((i,j))
                A[i][j] -= 2
    # print(cloud)
    # break
ans = 0
for i in range(n):
    for j in range(n):
        ans += A[i][j]
print(ans)