R,C,M = map(int, input().split())
# 상어 정보 입력받기
shark = {}
for i in range(M):
    shark[i] = {}
    r,c,s,d,z = map(int, input().split())
    shark[i]['r'] = r
    shark[i]['c'] = c
    shark[i]['s'] = s
    shark[i]['d'] = d
    shark[i]['z'] = z

fisher_loc = 1
total = 0
survived_shark = [i for i in range(M)]

# 낚시 하기
while True:
    min_row = int(1e8)
    fished_shark = -1
    for i in survived_shark:
        r = shark[i]['r']
        c = shark[i]['c']
        s = shark[i]['s']
        d = shark[i]['d']
        z = shark[i]['z']
        if c == fisher_loc:
            if min_row > r:
                fished_shark = i
                shark_size = z
                min_row = r
    if fished_shark != -1:
        total += shark_size
        del shark[fished_shark]
        survived_shark.pop(survived_shark.index(fished_shark))

    # 상어 이동시키기
    for i in survived_shark:
        r = shark[i]['r']
        c = shark[i]['c']
        s = shark[i]['s']
        d = shark[i]['d']
        z = shark[i]['z']

        # 초기 방향이 위라면
        count = 0
        while count != s:
            count += 1
            if d == 1 and r-1 == 0:
                d = 2
                r += 1
            elif d == 1 and r-1 != 0:
                r -= 1

            elif d == 2 and r+1 == R+1:
                d = 1
                r -= 1
            elif d == 2 and r+1 != R+1:
                r += 1

            elif d == 3 and c+1 == C+1:
                d = 4
                c -= 1
            elif d == 3 and c+1 != C+1:
                c += 1

            elif d == 4 and c-1 == 0:
                d = 3
                c += 1
            elif d == 4 and c-1 != 0:
                c -= 1

        shark[i]['r'] = r
        shark[i]['c'] = c
        shark[i]['d'] = d

    # 한칸에 동일한 상어가 있는지 확인하기
    # 있으면 큰애가 잡아먹기
    loc2shark = {}
    for i in survived_shark:
        r = shark[i]['r']
        c = shark[i]['c']

        try:
            loc2shark[(r,c)]
        except:
            loc2shark[(r,c)] = []

        loc2shark[(r,c)].append(i)

    for l in loc2shark.keys():
        if len(loc2shark[l]) == 1:
            continue
        else:
            max_shark = loc2shark[l][0]
            for s in loc2shark[l]:
                if shark[max_shark]['z'] < shark[s]['z']:
                    max_shark = s

            eaten_shark = [i for i in loc2shark[l] if i != max_shark]

            for s in eaten_shark:
                del shark[s]
                survived_shark.pop(survived_shark.index(s))

    fisher_loc += 1
    if fisher_loc == C+1:
        break

print(total)
