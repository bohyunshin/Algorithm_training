from collections import deque
class fish:
    def __init__(self,num,d,loc):
        self.num = num
        self.d = d
        self.loc = loc
        # self.shark = shark
space = [[0]*4 for _ in range(4)]
number = [0]*(17)
for i in range(4):
    row = list(map(int, input().split()))
    for j in range(0,7,2):
        num,d = row[j:j+2]
        f = fish(num,d-1,(i,j//2))
        space[i][j//2] = f
        number[num] = f
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
def move_fish(number,space,shark):
    for i in range(1,17):
        # 빈칸이면 패쓰.
        if number[i] == 0:
            continue
        f = number[i]
        fish_num,d,(x,y) = f.num, f.d, f.loc

        for k in range(d,d+8+1):
            k = k % 8
            nx,ny = x+dx[k],y+dy[k]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx,ny) != shark.loc:
                space[x][y].d = k
                number[i].d = k
                if space[nx][ny] != 0:
                    space[nx][ny].loc = (x,y)
                    number[space[nx][ny].num].loc = (x,y)
                if space[x][y] != 0:
                    space[x][y].loc = (nx,ny)
                    number[space[x][y].num].loc = (nx,ny)
                space[nx][ny], space[x][y] = space[x][y], space[nx][ny]
                break
    return number,space
        # print(f'### when i=={i}')
        # for j in range(4):
        #     print([f.num for f in space[j]])
        # print()
        # for j in range(4):
        #     print([f.d for f in space[j]])
        # print()
        # print(number[3].loc)
        # print()
def move_shark(space,shark):
    (x,y),d = shark.loc, shark.d
    result = []
    while True:
        x += dx[d]
        y += dy[d]
        if 0 <= x < 4 and 0 <= y < 4:
            pass
        else:
            x -= dx[d]
            y -= dy[d]
            break
        if space[x][y] != 0:
            result.append((x,y))
    return result
q = deque()
shark = space[0][0]
space[0][0] = 0
number[shark.num] = 0
eaten = shark.num
number,space = move_fish(number,space,shark)
shark_move_candidates = move_shark(space,shark)
for x,y in shark_move_candidates:






for j in range(4):
    print([f.num if f != 0 else f for f in space[j]])
print()
for j in range(4):
    print([f.d if f != 0 else f for f in space[j]])
