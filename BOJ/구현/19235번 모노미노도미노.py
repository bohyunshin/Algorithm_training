from copy import deepcopy
from collections import defaultdict


def go(t,x,y,col,k):
    n = len(blue) if col == 'blue' else len(green)
    m = len(blue[0]) if col == 'blue' else len(green[0])
    if t == 1:
        nx = x
        ny = y
        FLAG = blue[nx][ny] == 0 if col == 'blue' else green[nx][ny] == 0
        while nx <= n-1 and ny <= m-1 and FLAG:
            if col == 'blue':
                ny += 1
            else:
                nx += 1
            try:
                FLAG = blue[nx][ny] == 0 if col == 'blue' else green[nx][ny] == 0
            except:
                pass
        if col == 'blue':
            ny -= 1
            blue[nx][ny] = k
            blue_cnt[k] += 1
        else:
            nx -= 1
            green[nx][ny] = k
            green_cnt[k] += 1
    if t == 2:
        nx = x
        ny1 = y
        ny2 = y+1
        FLAG = blue[nx][ny1] == 0 and blue[nx][ny2] == 0 if col == 'blue' else green[nx][ny1] == 0 and green[nx][ny2] == 0
        while nx <= n-1 and ny2 <= m-1 and FLAG:
            if col == 'blue':
                ny1 += 1
                ny2 += 1
            else:
                nx += 1
            try:
                FLAG = blue[nx][ny1] == 0 and blue[nx][ny2] == 0 if col == 'blue' else green[nx][ny1] == 0 and green[nx][ny2] == 0
            except:
                pass
        if col == 'blue':
            ny1 -= 1
            ny2 -= 1
            blue[nx][ny1] = k
            blue[nx][ny2] = k
            blue_cnt[k] += 2
        else:
            nx -= 1
            green[nx][ny1] = k
            green[nx][ny2] = k
            green_cnt[k] += 2
    if t == 3:
        nx1 = x
        nx2 = x+1
        ny = y
        FLAG = blue[nx1][ny] == 0 and blue[nx2][ny] == 0 if col == 'blue' else green[nx1][ny] == 0 and green[nx2][ny] == 0
        while nx2 <= n-1 and ny <= m-1 and FLAG:
            if col == 'blue':
                ny += 1
            else:
                nx1 += 1
                nx2 += 1
            try:
                FLAG = blue[nx1][ny] == 0 and blue[nx2][ny] == 0 if col == 'blue' else green[nx1][ny] == 0 and green[nx2][ny] == 0
            except:
                pass
        if col == 'blue':
            ny -= 1
            blue[nx1][ny] = k
            blue[nx2][ny] = k
            blue_cnt[k] += 2
        else:
            nx1 -= 1
            nx2 -= 1
            green[nx1][ny] = k
            green[nx2][ny] = k
            green_cnt[k] += 2

def rotate(B):
    n = len(B)
    m = len(B[0])
    result = [[] for _ in range(m)]
    for j in range(m):
        for i in range(n):
            result[j].append(B[i][j])
    return result

def check1(B,col):
    global score
    # 진한부분 확인하는 함수.
    if col == 'blue':
        B = rotate(B)
    n = len(B)
    m = len(B[0])
    while True:
        full_row = []
        for i in range(n):
            # 연한 부분 제외하고 진한 부분부터 봄.
            if i == 0 or i == 1:
                continue
            row = B[i]
            if sum([l>=1 for l in row]) == m:
                full_row.append(i)
                # break
        if len(full_row) == 0:
            break
        result = [[0] * m for _ in range(len(full_row))]
        for i in range(n):
            if i in full_row:
                for l in B[i]:
                    if col == 'blue':
                        blue_cnt[l] -= 1
                    else:
                        green_cnt[l] -= 1
                score += 1
                continue
            result.append(B[i])

        B = deepcopy(result)

        for i in range(n-1):
            for j in range(m):
                if B[i][j] == 0:
                    continue
                t = domino[B[i][j]]
                if t == 1:
                    continue

                # 세로칸 내리기.
                # if t == 3 and B[i+1][j] == 0:
                #     B[i+1][j] = B[i][j]
                #     B[i][j] = 0

                if col == 'blue':
                    if blue_cnt[B[i][j]] == 1 and B[i+1][j] == 0:
                        B[i+1][j] = B[i][j]
                        B[i][j] = 0
                else:
                    if green_cnt[B[i][j]] == 1 and B[i+1][j] == 0:
                        B[i+1][j] = B[i][j]
                        B[i][j] = 0

        # 세로칸 캐리기.
        for _ in range(2):
            for i in range(n - 1):
                for j in range(m):
                    if B[i][j] == 0:
                        continue
                    t = domino[B[i][j]]
                    if t == 3 and B[i + 1][j] == 0:
                        B[i + 1][j] = B[i][j]
                        B[i][j] = 0



    if col == 'blue':
        return rotate(B)
    else:
        return B


def check2(B,col):
    # 연한부분 확인하는 함수.
    if col == 'blue':
        B = rotate(B)
    n = len(B)
    m = len(B[0])
    cnt = 0
    for i in range(n):
        if i == 0 or i == 1:
            row = B[i]
            if sum([l>=1 for l in row]) >= 1:
                cnt += 1
    if cnt == 0:
        if col == 'blue':
            return rotate(B)
        else:
            return B
    else:
        for i in range(1,cnt+1):
            for l in B[-i]:
                if col == 'blue':
                    blue_cnt[l] -= 1
                else:
                    green_cnt[l] -= 1
        result = [[0]*m for _ in range(cnt)] + B[:-cnt]
        if col == 'blue':
            return rotate(result)
        else:
            return result

def count(A):
    cnt = 0
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            if A[i][j] >= 1:
                cnt += 1
    return cnt

# A = [[1,0,1,0,0,0], [1,0,1,0,0,0], [1,0,1,0,0,0], [1,0,1,0,1,1], [1,0,1,0,1,1]]
# for i in A:
#     print(i)
# print()
# A = check2(A,'blue')
# for i in A:
#     print(i)

score = 0
tile = 0

n = int(input())

blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]
domino = [0]*(n+1)
blue_cnt = defaultdict(int)
green_cnt = defaultdict(int)


for i in range(n):
    t,x,y = map(int, input().split())
    domino[i+1] = t
    go(t,x,0,'blue',i+1)
    go(t,0,y,'green',i+1)

    # for i in blue:
    #     print(i)
    # print()
    # for i in green:
    #     print(i)

    blue = check1(blue,'blue')
    green = check1(green,'green')

    blue = check2(blue, 'blue')
    green = check2(green, 'green')

    # for i in blue:
    #     print(i)
    # print()
    # for i in green:
    #     print(i)

# for i in blue:
#     print(i)
# print()
# for i in green:
#     print(i)
#
# print(domino)
# print(blue_cnt)
# print(green_cnt)

tile += count(blue) + count(green)

print(score)
print(tile)

"""
8
2 1 0
2 1 0
2 1 0
2 1 0
2 1 0
3 0 2
3 0 2
3 0 3
"""

"""
9
2 1 0
2 1 0
2 1 0
2 1 0
2 1 0
3 0 2
3 0 2
3 0 3
3 0 3
"""

"""
7
2 1 0
2 1 0
2 1 0
2 1 0
2 1 0
3 0 2
3 0 2
"""

"""
4
3 0 0
2 0 2
2 0 2
2 0 0
"""

"""
8
3 0 0
2 0 2
2 0 2
2 0 0
1 0 3
1 0 0
2 0 1
3 0 3
"""

"""
18
1 2 2
1 2 3
2 0 0
1 2 0
1 1 2
1 1 0
2 3 0
3 0 1
3 1 3
2 1 0
1 2 0
2 3 0
2 2 1
1 2 2
3 0 3
1 2 0
2 2 0
3 2 3
"""