n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

x,y = (n//2,n//2)
dx_ = [0,1,0,-1]
dy_ = [-1,0,1,0]
k = 0
LEN = 1
ans = 0
def distribute(x,y,nx,ny,sand):
    global ans,rest
    A[x][y] -= sand
    rest += sand
    if 0 <= nx < n and 0 <= ny < n:
        A[nx][ny] += sand
    else:
        ans += sand

while True:
    FLAG = False
    for _ in range(2):
        for _ in range(LEN):
            x += dx_[k]
            y += dy_[k]
            # print(x,y,k)
            # 왼쪽 이동시,
            if k == 0:
                rest = 0
                tot_sand = A[x][y]

                dx,dy = [2,-2],[0,0]
                for i in range(2):
                    nx,ny = x+dx[i],y+dy[i]
                    distribute(x,y,nx,ny,int(tot_sand*0.02))

                dx,dy = [-1,-1,-1,1,1,1,],[-1,0,1,-1,0,1]
                ratio = [0.1,0.07,0.01]*2
                for i in range(6):
                    nx,ny,r = x+dx[i],y+dy[i],ratio[i]
                    distribute(x,y,nx,ny,int(tot_sand*r))

                nx,ny = x,y-2
                distribute(x,y,nx,ny,int(tot_sand*0.05))

                alpha = tot_sand-rest
                nx,ny = x,y-1
                distribute(x,y,nx,ny,alpha)
            # 아래 이동시,
            elif k == 1:
                rest = 0
                tot_sand = A[x][y]

                dx, dy = [0,0], [2,-2]
                for i in range(2):
                    nx, ny = x + dx[i], y + dy[i]
                    distribute(x, y, nx, ny, int(tot_sand * 0.02))

                dx, dy = [1,0,-1,1,0,-1], [-1,-1,-1,1,1,1]
                ratio = [0.1, 0.07, 0.01] * 2
                for i in range(6):
                    nx, ny, r = x + dx[i], y + dy[i], ratio[i]
                    distribute(x, y, nx, ny, int(tot_sand * r))

                nx, ny = x+2, y
                distribute(x, y, nx, ny, int(tot_sand * 0.05))

                alpha = tot_sand - rest
                nx, ny = x+1, y
                distribute(x, y, nx, ny, alpha)
            # 오른쪽 이동시,
            elif k == 2:
                rest = 0
                tot_sand = A[x][y]

                dx, dy = [2, -2], [0, 0]
                for i in range(2):
                    nx, ny = x + dx[i], y + dy[i]
                    distribute(x, y, nx, ny, int(tot_sand * 0.02))

                dx, dy = [-1, -1, -1, 1, 1, 1, ], [-1, 0, 1, -1, 0, 1]
                ratio = [0.01, 0.07, 0.1] * 2
                for i in range(6):
                    nx, ny, r = x + dx[i], y + dy[i], ratio[i]
                    distribute(x, y, nx, ny, int(tot_sand * r))

                nx, ny = x, y + 2
                distribute(x, y, nx, ny, int(tot_sand * 0.05))

                alpha = tot_sand - rest
                nx, ny = x, y + 1
                distribute(x, y, nx, ny, alpha)
            # 위로 이동시,
            elif k == 3:
                rest = 0
                tot_sand = A[x][y]

                dx, dy = [0, 0], [2, -2]
                for i in range(2):
                    nx, ny = x + dx[i], y + dy[i]
                    distribute(x, y, nx, ny, int(tot_sand * 0.02))

                dx, dy = [1, 0, -1, 1, 0, -1], [-1, -1, -1, 1, 1, 1]
                ratio = [0.01, 0.07, 0.1] * 2
                for i in range(6):
                    nx, ny, r = x + dx[i], y + dy[i], ratio[i]
                    distribute(x, y, nx, ny, int(tot_sand * r))

                nx, ny = x - 2, y
                distribute(x, y, nx, ny, int(tot_sand * 0.05))

                alpha = tot_sand - rest
                nx, ny = x - 1, y
                distribute(x, y, nx, ny, alpha)

            # print(x,y)
            A[x][y] = 0

            if (x,y) == (0,0):
                FLAG = True
                break
        k = (k+1) % 4
        if FLAG:
            break
    if FLAG:
        break
    LEN += 1
print(ans)