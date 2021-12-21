from copy import deepcopy
fish = []
direction = []
for _ in range(4):
    tmp = list(map(int,input().split()))
    row1,row2 = [],[]
    for i in range(4):
        a,b = tmp[i*2:(i+1)*2]
        b -= 1
        row1.append(a)
        row2.append(b)
    fish.append(row1)
    direction.append(row2)
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
# (0,0)에 있는 물고기 먹기.
ans = fish[0][0]
# 상어가 있는 곳은 값을 100으로 표시해줌.
# 빈 공간은 -1로 표시해주자.
fish[0][0] = 100
# 물고기가 순서대로 이동하기.
def go(fish,direction):
    for f in range(1,17):
        FLAG = False
        for x in range(4):
            for y in range(4):
                if fish[x][y] == f:
                    d = direction[x][y]
                    nx,ny = x+dx[d],y+dy[d]
                    cnt = 0
                    while True:
                        # 이동할 곳이 없다면 이동하지 않음.
                        if cnt == 8:
                            break
                        if 0 <= nx < 4 and 0 <= ny < 4 and \
                            (1 <= fish[nx][ny] <= 16 or fish[nx][ny] == -1):
                            break
                        # 방향을 45도 틀어본다.
                        cnt += 1
                        d = (d+1)%8
                        nx,ny = x+dx[d],y+dy[d]
                    direction[x][y] = d
                    # 이동할 곳이 있다면 그곳의 물고기와 방향을 바꿈.
                    if cnt != 8:
                        fish[x][y],fish[nx][ny] = fish[nx][ny],fish[x][y]
                        direction[x][y],direction[nx][ny] = direction[nx][ny],direction[x][y]
                    FLAG = True
                    break
            if FLAG:
                break
    # 상어 이동하기.
    ans = 0
    for x in range(4):
        for y in range(4):
            if fish[x][y] == 100:
                d = direction[x][y]
                nx,ny = x+dx[d],y+dy[d]
                sx,sy = x,y
                # print(nx,ny)
                while True:
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if 1 <= fish[nx][ny] <= 16:
                            temp = fish[nx][ny]
                            fish[x][y] = -1
                            fish[nx][ny] = 100
                            cur = temp + go(deepcopy(fish),deepcopy(direction))
                            if ans < cur:
                                ans = cur
                            fish[sx][sy] = 100
                            fish[nx][ny] = temp
                        nx += dx[d]
                        ny += dy[d]
                    else:
                        break
    return ans

ans += go(fish,direction)
print(ans)