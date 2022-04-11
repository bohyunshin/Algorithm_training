from copy import deepcopy
m,s = map(int,input().split())
class fish:
    def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.d = d
a = [[[] for _ in range(4)] for _ in range(4)]
smell = [[[] for _ in range(4)] for _ in range(4)]
fish_list = []
for _ in range(m):
    x,y,d = map(int,input().split())
    f = fish(x-1,y-1,d-1)
    a[x-1][y-1].append(f)
    fish_list.append(f)
sx,sy = map(int,input().split())
sx,sy = sx-1,sy-1
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
sdx = [-1,0,1,0]
sdy = [0,-1,0,1]

def move_shark(x,y,cnt,d,fish_set):
    if cnt == 3:
        shark_candidate.append((len(fish_set),d))
        return
    for i in range(4):
        d += str(i+1)
        nx,ny = x+sdx[i],y+sdy[i]
        tmp = set()
        if 0 <= nx < 4 and 0 <= ny < 4:
            for f in b[nx][ny]:
                tmp.add(f)
            move_shark(nx,ny,cnt+1,d,fish_set.union(tmp))
        d = d[:-1]


for k in range(s):
    b = [[[] for _ in range(4)] for _ in range(4)]
    # 물고기 이동
    # fish_list_cp = []
    for f in fish_list:
        f = deepcopy(f)
        x,y,d = f.x, f.y, f.d
        cnt = 0
        nx,ny = x+dx[d],y+dy[d]
        while not (0 <= nx < 4 and 0 <= ny < 4 and \
                (nx,ny) != (sx,sy) and len(smell[nx][ny]) == 0):
            d = (d-1)%8
            nx,ny = x+dx[d],y+dy[d]
            cnt += 1
            if cnt == 8:
                break
        # 움직일 수 있다면,
        if cnt != 8:
            f.x,f.y,f.d = nx,ny,d
        b[f.x][f.y].append(f)

    # if k == 1:
    #     for i in range(4):
    #         for j in range(4):
    #             print([f.d for f in b[i][j]], end=' ')
    #         print('\n')
    # 상어 이동.
    shark_candidate = []
    move_shark(sx,sy,0,'',set())
    shark_candidate.sort(key=lambda x: (-x[0],x[1]))
    # print(shark_candidate)
    # 상어 먹방.
    for i in shark_candidate[0][1]:
        i = int(i)-1
        sx,sy = sx+sdx[i],sy+sdy[i]
        if len(b[sx][sy]) >= 1:
            b[sx][sy].clear()
            smell[sx][sy].append(k)
    # 냄새 사라지기.
    for i in range(4):
        for j in range(4):
            tmp = []
            for l in smell[i][j]:
                if k-l < 2:
                    tmp.append(l)
            smell[i][j] = tmp
    # 물고기 복제.
    fish_list = []
    for i in range(4):
        for j in range(4):
            for f in a[i][j]:
                f = deepcopy(f)
                b[i][j].append(f)
            fish_list += b[i][j]
    a = deepcopy(b)
    # break
ans = 0
for i in range(4):
    for j in range(4):
        ans += len(a[i][j])
print(ans)