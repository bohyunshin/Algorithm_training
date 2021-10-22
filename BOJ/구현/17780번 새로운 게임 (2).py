n,k = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
horse = {}
dx = [0,0,-1,1]
dy = [1,-1,0,0]
where = [ [ [] for _ in range(n) ] for _ in range(n)]
for i in range(k):
    horse[i] = {}
    x,y,d = map(int,input().split())
    x -= 1
    y -= 1
    d -= 1
    # horse[i]['loc'] = (x,y)
    # horse[i]['d'] = d
    horse[i] = d
    where[x][y].append(i)

def change_d(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    elif d == 3:
        return 2

def check(where):
    for i in range(n):
        for j in range(n):
            if len(where[i][j]) >= 4:
                return True
    return False

for turn in range(1,1001):
    for i in range(k):
        FLAG = False
        for x in range(n):
            for y in range(n):
                if len(where[x][y]) >= 1 and where[x][y][0] == i:
                    FLAG = True
                    d = horse[i]
                    nx,ny = x+dx[d],y+dy[d]
                    if (0 <= nx < n and 0 <= ny < n) and A[nx][ny] in [0,1]:
                        if A[nx][ny] == 0:
                            where[nx][ny] += where[x][y]
                            where[x][y].clear()
                        elif A[nx][ny] == 1:
                            where[nx][ny] += where[x][y][::-1]
                            where[x][y].clear()
                    if (0 <= nx < n and 0 <= ny < n and A[nx][ny] == 2) or \
                            (nx < 0 or nx >= n or ny < 0 or ny >= n):
                        horse[i] = change_d(d)
                        d = horse[i]
                        nnx,nny = x+dx[d],y+dy[d]

                        if 0 <= nnx < n and 0 <= nny < n:
                            if A[nnx][nny] == 0:
                                where[nnx][nny] += where[x][y]
                                where[x][y].clear()
                            elif A[nnx][nny] == 1:
                                where[nnx][nny] += where[x][y][::-1]
                                where[x][y].clear()
                            elif A[nnx][nny] == 2:
                                pass
                        # 방향을 바꿨을 때, 벗어나는 경우는 방향만 바꿔줌.
                        else:
                            pass
                    break
            if FLAG:
                break
    if check(where):
        print(turn)
        exit()
        break
print(-1)
