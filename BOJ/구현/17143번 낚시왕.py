R,C,M = map(int, input().split())
shark = {}
for i in range(M):
    shark[i] = {}
    r,c,s,d,z = map(int, input().split())
    shark[i]['r'] = r
    shark[i]['c'] = c
    shark[i]['s'] = s
    shark[i]['d'] = d
    shark[i]['z'] = z

# 상어 이동시키기
for i in range(M):
    r = shark[i]['r']
    c = shark[i]['c']
    s = shark[i]['s']
    d = shark[i]['d']
    z = shark[i]['z']

    # 초기 방향이 위라면
    count = 0
    while count != s:
        if d == 1:
            if r-1 == 0:
                r += 1
            else:
                r -= 1
