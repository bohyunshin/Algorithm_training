r, c, t = map(int, input().split())
array = []
for _ in range(r):
    array.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 공기청정기 위치 파악
air = []
for i in range(r):
    for j in range(c):
        if array[i][j] == -1:
            air.append((i,j))

def gen_dxdy():
    a = []
    for _ in range(r):
        a.append([0]*c)
    return a

current = 0


while True:
    # 먼지 퍼뜨리기
    dxdy = gen_dxdy()
    for x in range(r):
        for y in range(c):
            if array[x][y] not in [0, -1]:
                # 퍼질 수 있는 양
                dust = int(array[x][y] / 5)
                # 얼마나 퍼졌는지 방향 체크
                direction = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and (nx,ny) not in air:
                        dxdy[nx][ny] += dust
                        direction += 1
                # 한 곳의 미세먼지 감소
                dxdy[x][y] -= dust*direction
    for i in range(r):
        array[i] = [j+k for j,k in zip(array[i], dxdy[i])]

    array_copy = []
    for a in array:
        array_copy.append(a.copy())

    # 공기청정기 작동시키기
    # 위쪽부터 작동시킴
    # 왼쪽에서 오른쪽
    x = air[0][0]
    y = air[0][1]
    array_copy[x][y+1:] = [0] + array[x][y+1:c-1]
    # 오른쪽에서 아래에서 위
    rows = x
    while True:
        a = array[rows][c-1]
        rows -= 1
        if rows == -1:
            a = array[rows][c - 1]
            break
        array_copy[rows][c-1] = a
    # 오른쪽에서 왼
    array_copy[0][:c-1] = array[0][1:c]
    # 왼쪽에서 위에서 아래
    rows = 0
    while True:
        a = array[rows][0]
        rows += 1
        if rows == x:
            a = array[rows][c - 1]
            break
        array_copy[rows][0] = a


    # 아래쪽 작동시킴
    # 왼쪽에서 오른쪽
    x = air[1][0]
    y = air[1][1]
    array_copy[x][y+1:] = [0] + array[x][y+1:c-1]
    # 오른쪽에서 위에서 아래
    rows = x
    while True:
        a = array[rows][c-1]
        rows += 1
        if rows == r:
            break
        array_copy[rows][c-1] = a
    # 오른쪽에서 왼쪽
    array_copy[r-1][:c-1] = array[r-1][1:c]
    # 왼쪽에서 아래에서 위
    rows = r-1
    while True:
        a = array[rows][0]
        rows -= 1
        if rows == x:
            break
        array_copy[rows][0] = a

    # 미세먼지 양 출력
    total = 0
    for i in range(r):
        for j in range(c):
            if array_copy[i][j] != -1:
                total += array_copy[i][j]

    current += 1

    array = []
    for a in array_copy:
        array.append(a.copy())

    if current == t:
        break

print(total)





