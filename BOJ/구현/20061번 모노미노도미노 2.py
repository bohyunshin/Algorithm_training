n = 10
blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]

def go(t,x,y,col):
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
            blue[nx][ny] += 1
        else:
            nx -= 1
            green[nx][ny] += 1
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
            blue[nx][ny1] += 1
            blue[nx][ny2] += 1
        else:
            nx -= 1
            green[nx][ny1] += 1
            green[nx][ny2] += 1
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
            blue[nx1][ny] += 1
            blue[nx2][ny] += 1
        else:
            nx1 -= 1
            nx2 -= 1
            green[nx1][ny] += 1
            green[nx2][ny] += 1

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
    FLAG = False
    full_row = []
    for i in range(n):
        # 연한 부분 제외하고 진한 부분부터 봄.
        if i == 0 or i == 1:
            continue
        row = B[i]
        if sum(row) == m:
            FLAG = True
            full_row.append(i)
    if FLAG == False:
        if col == 'blue':
            return rotate(B)
        else:
            return B
    else:
        result = [[0] * m for _ in range(len(full_row))]
        for i in range(n):
            if i in full_row:
                score += 1
                continue
            result.append(B[i])
        if col == 'blue':
            return rotate(result)
        else:
            return result

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
            if sum(row) >= 1:
                cnt += 1
    if cnt == 0:
        if col == 'blue':
            return rotate(B)
        else:
            return B
    else:
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
            if A[i][j] == 1:
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
for _ in range(n):
    t,x,y = map(int, input().split())
    go(t,x,0,'blue')
    go(t,0,y,'green')

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
