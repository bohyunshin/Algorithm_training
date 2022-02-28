from collections import defaultdict
a = [list(i for i in input()) for _ in range(12)]

def dfs(x,y,color):
    if visited[x][y]:
        return
    visited[x][y] = True
    puyo[cnt].append((x,y))
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < 12 and 0 <= ny < 6 and \
                visited[nx][ny] == False and a[nx][ny] == color:
            dfs(nx,ny,color)
def bumb():
    is_boom = False
    for col in puyo.keys():
        if len(puyo[col]) >= 4:
            is_boom = True
            for x,y in puyo[col]:
                a[x][y] = -1
    return is_boom
def move():
    for _ in range(12):
        for x in range(11):
            for y in range(6):
                nx = x+1
                while a[nx][y] == -1 or a[nx][y] == '.':
                    a[nx][y] = a[x][y]
                    a[x][y] = '.'
                    nx += 1
                    if not 0 <= nx < 12:
                        break

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0
while True:
    visited = [[False] * 6 for _ in range(12)]
    cnt = 0
    puyo = defaultdict(list)
    for x in range(12):
        for y in range(6):
            if a[x][y] != '.' and visited[x][y] == False:
                dfs(x,y,a[x][y])
                cnt += 1
    boom = bumb()
    move()
    if boom:
        ans += 1
    else:
        break

    # for i in a:
    #     print(i)
    # print()
    # if ans == 3:
    #     break
print(ans)

"""
......
......
......
......
......
......
......
.G....
.R....
.R....
.RR...
GRGGG.

......
......
......
......
......
......
......
.G....
.R....
.R....
GRRG..
GRGG..

......
......
......
......
......
......
......
......
......
.YYY..
RRGG..
RRGGY.
"""