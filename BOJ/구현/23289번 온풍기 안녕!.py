from copy import deepcopy
def return_machine_direction(d):
    if d == 0:
        return ([-1,-1,-1],[-1,0,1])
    elif d == 1:
        return [-1,0,1],[1,1,1]
    elif d == 2:
        return [1,1,1],[-1,0,1]
    elif d == 3:
        return  [-1,0,1],[-1,-1,-1]
def return_check_walls(x,y,d):
    if d == 0:
        w = [
            [(x-1,y-1,0),(x,y-1,1)],
            [(x-1,y,0)],
            [(x-1,y+1,0),(x,y,1)]
        ]
    elif d == 1:
        w = [
            [(x-1,y,0),(x-1,y,1)],
            [(x,y,1)],
            [(x,y,0),(x+1,y,1)]
        ]
    elif d == 2:
        w = [
            [(x,y-1,1),(x,y-1,0)],
            [(x,y,0)],
            [(x,y+1,0),(x,y,1)]
        ]
    elif d == 3:
        w = [
            [(x-1,y-1,1),(x-1,y,0)],
            [(x,y-1,1)],
            [(x,y,0),(x+1,y-1,1)]
        ]
    return w
r,c,count = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(r)]
temperature = [[0]*c for _ in range(r)]
w = int(input())
walls = {}
for _ in range(w):
    x,y,t = map(int,input().split())
    x -= 1
    y -= 1
    if t == 0:
        walls[(x-1,y,t)] = 1
    else:
        walls[(x,y,t)] = 1
map_direction = {3:0, 1:1, 4:2, 2:3}
mdx = [-1,0,1,0]
mdy = [0,1,0,-1]
ans = 0
machines = []
check_loc = []
for i in range(r):
    for j in range(c):
        if a[i][j] == 5:
            check_loc.append((i,j))
        elif 1 <= a[i][j] <= 4:
            machines.append((i,j))

while True:
    for machine in machines:
        check = [[False]*c for _ in range(r)]
        x,y = machine
        d = map_direction[a[x][y]]
        (dx,dy) = return_machine_direction(d)
        val = 5
        x,y = x+mdx[d],y+mdy[d]
        temperature[x][y] += val
        current = [(x,y)]
        while True:
            val -= 1
            next_loc = []
            for x,y in current:
                for i in range(3):
                    nx,ny = x+dx[i],y+dy[i]
                    if 0 <= nx < r and 0 <= ny < c and check[nx][ny] == False:
                        walls_to_check = return_check_walls(x,y,d)[i]
                        flag = 0
                        for w in walls_to_check:
                            k,l,t = w
                            if walls.get((k,l,t)) != None:
                                flag = 1
                        if flag == 0:
                            temperature[nx][ny] += val
                            next_loc.append((nx, ny))
                            check[nx][ny] = True
            current = next_loc.copy()
            if val == 0:
                break
    temperature_cp = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            s = 0
            for i in range(4):
                nx,ny = x+mdx[i],y+mdy[i]
                if i == 0:
                    w = (nx,ny,0)
                elif i == 1:
                    w = (x,y,1)
                elif i == 2:
                    w = (x,y,0)
                elif i == 3:
                    w = (nx,ny,1)
                if 0 <= nx < r and 0 <= ny < c and \
                    temperature[x][y] > temperature[nx][ny] and \
                    walls.get(w) == None:
                    diff = int((temperature[x][y] - temperature[nx][ny])/4)
                    temperature_cp[nx][ny] += diff
                    s += diff
            temperature_cp[x][y] += temperature[x][y] - s
    temperature = deepcopy(temperature_cp)
    for i in range(r):
        for j in range(c):
            if (j in [0,c-1] or i in [0,r-1]) and temperature[i][j] >= 1:
                temperature[i][j] -= 1
    ans += 1
    flag = 0
    for i,j in check_loc:
        if temperature[i][j] < count:
            flag = 1
    if flag == 0:
        print(ans)
        break
    if ans > 100:
        print(101)
        break

"""
9 6 1
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
1 0 0 0 0 0
1
1 1 1

그림4.
7 7 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
1
3 4 1

그림5.
7 7 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 2
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
2
3 4 1
2 5 0

그림6.
7 7 1
0 0 0 0 0 0 0
0 0 0 0 4 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 3 0 0
3
4 4 0
4 4 1
4 6 0

5 4 1
0 0 0 0
4 4 4 4
0 0 0 0
0 0 0 0
0 0 0 0
1
1 1 0
"""

"""
[94, 100, 107, 110, 113, 109, 103, 98]
[113, 122, 130, 135, 137, 132, 125, 116]
[141, 153, 166, 171, 173, 167, 156, 145]
[172, 187, 198, 198, 213, 197, 187, 175]
[194, 207, 223, 241, 235, 231, 208, 194]
[202, 213, 229, 239, 244, 231, 216, 202]
[201, 210, 223, 234, 236, 225, 210, 199]
"""