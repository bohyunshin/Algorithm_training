from collections import defaultdict
R,C,m = map(int, input().split())

def move_shark(x,y,d,s):
    while s > 0:
        # 위
        if d == 1:
            if x == 1:
                d = 2
            elif x-1 >= s:
                x -= s
                s = 0
            elif x-1 < s:
                s -= x - 1
                x = 1
                d = 2
        # 아래.
        if d == 2:
            if R == x:
                d = 1
            elif R-x >= s:
                x += s
                s = 0
            elif R-x < s:
                s -= R - x
                x = R
                d = 1
        # 오른쪽.
        if d == 3:
            if C == y:
                d = 4
            elif C-y >= s:
                y += s
                s = 0
            elif C-y < s:
                s -= C-y
                y = C
                d = 4
        # 왼쪽.
        if d == 4:
            if y == 1:
                d = 3
            elif y-1 >= s:
                y -= s
                s = 0
            elif y-1 < s:
                s -= y-1
                y = 1
                d = 3
    return x,y,d
A = [[0]*(C+1) for _ in range(R+1)]
shark = {}
for i in range(m):
    r,c,s,d,z = map(int, input().split())
    shark[i] = {'r':r, 'c':c, 's':s, 'd':d, 'z':z}
    A[r][c] += 1

answer = 0
for i in range(1,C+1):
    # 상어잡기.
    eaten_index = -1
    min_r = 1e100
    for s in shark.keys():
        if shark[s]['c'] == i:
            if min_r > shark[s]['r']:
                eaten_index = s
                min_r = shark[s]['r']
    # print(answer,eaten_index)
    if eaten_index != -1:
        # print(answer,eaten_index)
        answer += shark[eaten_index]['z']
        del shark[eaten_index]

    # 상어 이동시키기.
    for sh in shark.keys():
        r,c,s,d,z = list(shark[sh].values())
        x,y,d = move_shark(r,c,d,s)
        shark[sh]['r'] = x
        shark[sh]['c'] = y
        shark[sh]['d'] = d

    # 상어 잡아먹기
    loc = {}
    del_index = []
    for sh in shark.keys():
        r,c,s,d,z = list(shark[sh].values())

        if (r,c) in loc.keys():
            if shark[loc[(r,c)]]['z'] > z:
                del_index.append(sh)
            else:
                del_index.append(loc[(r,c)])
                loc[(r,c)] = sh
        else:
            loc[(r,c)] = sh
    for index in del_index:
        del shark[index]

print(answer)

