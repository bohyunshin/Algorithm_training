dx = [-1,0,1,0]
dy = [0,1,0,-1]
direction = {'U':0,'R':1,'D':2,'L':3}

def check(A,end):
    cnt = 0
    for x,y in end:
        if A[x][y] == 'b':
            cnt += 1
            # return False
    return cnt == len(end)

def result(A,end):
    cnt = 0
    for x,y in end:
        if A[x][y] == 'B':
            cnt += 1
            # return 'incomplete'
    return 'complete' if cnt == len(end) else 'incomplete'

t = 1
while True:
    r,c = map(int,input().split())
    if r == 0 and c == 0:
        break
    A = []
    for _ in range(r):
        A.append([i for i in input()])
    orders = input()
    end = []
    for i in range(r):
        for j in range(c):
            if A[i][j] in ['w','W']:
                x,y = i,j
            if A[i][j] in ['+','B','W']:
                end.append((i,j))
                A[i][j] = A[i][j].lower()
                if A[i][j] == '+':
                    A[i][j] = '.'
    # print(end)
    # for i in A:
    #     print(i)
    # print()
    for order in orders:
        if check(A,end):
            break
        d = direction[order]
        nx,ny = x+dx[d],y+dy[d]
        if 0 <= nx < r and 0 <= ny < c and A[nx][ny] != '#':
            # 0 <= nx < r and 0 <= ny < c and
            # 이동하려는 칸이 빈칸이면 이동함.
            if A[nx][ny] == '.':
                A[nx][ny] = 'w'
                A[x][y] = '.'
                x,y = nx,ny
            # 지시한 방향에 박스가 있으면,
            elif A[nx][ny] == 'b':
                nnx,nny = nx+dx[d],ny+dy[d]
                # 박스가 이동할 칸이 벽이 아니어야 하고 박스도 없어야하고,
                # 이동할 칸이 비어있어야 함.
                if 0 <= nnx < r and 0 <= nny < c and A[nnx][nny] == '.':
                    # 0 <= nnx < r and 0 <= nny < c and
                    A[nnx][nny] = 'b'
                    A[nx][ny] = 'w'
                    A[x][y] = '.'
                    x,y = nx,ny
    for i in range(r):
        for j in range(c):
            if (i,j) in end:
                if A[i][j] == '.':
                    A[i][j] = '+'
                else:
                    A[i][j] = A[i][j].upper()
    RESULT = result(A,end)
    print(f'Game {t}: {RESULT}')
    for row in A:
        print(''.join(row))
    t += 1

"""
8 9
#########
#...#...#
#..bb.b.#
#...#w#.#
#...#b#.#
#...++++#
#...#..##
#########
ULRURDDDUULLDDD

6 6
######
#....#
#+...#
#b...#
#w...#
######
UUU
0 0

6 6
######
#....#
#....#
#+BW.#
#....#
######
LL
0 0
"""