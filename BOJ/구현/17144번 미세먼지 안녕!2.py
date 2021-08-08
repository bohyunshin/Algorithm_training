from copy import deepcopy
r,c,t = map(int,input().split())
A = []
for _ in range(r):
    A.append(list(map(int, input().split())))
air = []
for i in range(r):
    for j in range(c):
        if A[i][j] == -1:
            air.append((i,j))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(t):
    B = [[0]*c for _ in range(r)]
    # 먼지 증식하기.
    for i in range(r):
        for j in range(c):
            if (i,j) in air:
                B[i][j] = -1
                continue
            if A[i][j] == 0:
                continue
            dust = A[i][j] // 5
            count = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < r and 0 <= ny < c and (nx,ny) not in air:
                    count += 1
                    B[nx][ny] += dust
            B[i][j] += A[i][j] - dust*count

    ##### 공기청정기 위쪽 순환
    x,y =  air[0]
    y += 1

    C = deepcopy(B)
    # 공기 청소기 바로 옆 없애기
    C[x][y] = 0
    while True:

        if (x,y)  == air[0]:
            break
        # 아래쪽 가로 방향 순환.
        if x == air[0][0] and y < c-1:
            C[x][y+1] = B[x][y]
            y += 1
            continue
        # 오른쪽 세로 방향 순환.
        if 1 <= x <= air[0][0] and y == c-1:
            C[x-1][y] = B[x][y]
            x -= 1
            continue
        # 위쪽 가로 방향 순환.
        if x == 0 and 1 <= y <= c-1:
            C[x][y-1] = B[x][y]
            y -= 1
            continue
        # 왼쪽 세로 방향 순환.
        if 0 <= x < air[0][0] and y == 0:
            C[x+1][y] = B[x][y]
            x += 1
            continue

    ##### 공기청소기 아래쪽 순환
    a, b = air[1]
    b += 1
    # 공기 청소기 바로 옆 없애기
    C[a][b] = 0
    while True:

        if (a, b) == air[1]:
            break

        if a == air[1][0] and b < c - 1:
            C[a][b + 1] = B[a][b]
            b += 1
            continue
        if air[1][0] <= a < r-1 and b == c - 1:
            C[a + 1][b] = B[a][b]
            a += 1
            continue
        if a == r-1 and 1 <= b <= c - 1:
            C[a][b - 1] = B[a][b]
            b -= 1
            continue
        if air[1][0] < a <= r-1 and b == 0:
            C[a - 1][b] = B[a][b]
            a -= 1
            continue

    for x,y in air:
        C[x][y] = -1

    A = deepcopy(C)

answer = 0
for i in range(r):
    for j in range(c):
        if A[i][j] != -1:
            answer += A[i][j]
print(answer)