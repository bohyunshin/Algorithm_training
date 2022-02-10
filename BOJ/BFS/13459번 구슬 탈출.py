from collections import deque
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(input())
for i in range(n):
    for j in range(m):
        if a[i][j] == 'O':
            hole = i,j
        if a[i][j] == 'R':
            r = i,j
        if a[i][j] == 'B':
            b = i,j
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def move(x,y,sx,sy,d):
    while ( a[x][y] not in ['#','O'] and (x,y) != (sx,sy)):
        x += dx[d]
        y += dy[d]
    if a[x][y] == 'O':
        return x,y
    else:
        return x-dx[d], y-dy[d]
def go(rx,ry,bx,by,d):
    reds = []
    blues = []
    # 위 또는 아래로 움직이는 경우.
    if d in [0,2]:
        # 같은 열에 있는 경우.
        if ry == by:
            # 빨간 구슬이 더 아래에 있는 경우
            # 위로 움직이는 경우라면 파란구슬부터, 아래로 움직이는 경우라면 빨간구슬부터 움직인다.
            if rx >= bx:
                if d == 0:
                    nbx,nby = move(bx,by,rx,ry,d)
                    nrx,nry = move(rx,ry,nbx,nby,d)
                else:
                    nrx, nry = move(rx, ry, bx,by, d)
                    nbx, nby = move(bx, by, nrx, nry, d)
            # 파란 구슬이 더 아래에 있는 경우
            # 위로 움직이는 경우라면 빨간구슬부터, 아래로 움직이는 경우라면 파란구슬부터 움직인다.
            else:
                if d == 0:
                    nrx,nry = move(rx,ry,bx,by,d)
                    nbx,nby = move(bx,by,nrx,nry,d)
                else:
                    nbx, nby = move(bx, by, rx, ry, d)
                    nrx, nry = move(rx, ry, nbx, nby, d)
                # print(nbx, nby)
                # print(nrx, nry)
        # 다른 열에 있는 경우.
        else:
            nbx,nby = move(bx,by,rx,ry,d)
            nrx,nry = move(rx,ry,bx,by,d)
    elif d in [1,3]:
        # 같은 행에 있는 경우.
        if rx == bx:
            # 빨간 구슬이 더 오른쪽에 있는 경우
            # 왼쪽으로 움직이는 경우라면 파란구슬부터, 오른쪽으로 움직이는 경우라면 빨간구슬부터 움직인다.
            if ry >= by:
                if d == 3:
                    nbx, nby = move(bx, by, rx, ry, d)
                    nrx, nry = move(rx, ry, nbx, nby, d)
                    # print(nrx,nry)
                else:
                    nrx, nry = move(rx, ry, bx, by, d)
                    nbx, nby = move(bx, by, nrx, nry, d)
            # 파란 구슬이 더 오른쪽에 있는 경우
            # 왼쪽으로 움직이는 경우라면 빨간구슬부터, 오른쪽으로 움직이는 경우라면 파란구슬부터 움직인다.
            else:
                if d == 3:
                    nrx, nry = move(rx, ry, bx, by, d)
                    nbx, nby = move(bx, by, nrx, nry, d)
                else:
                    nbx, nby = move(bx, by, rx, ry, d)
                    nrx, nry = move(rx, ry, nbx, nby, d)
                # print(nbx, nby)
                # print(nrx, nry)
        # 다른 행에 있는 경우.
        else:
            nbx, nby = move(bx, by, rx, ry, d)
            nrx, nry = move(rx, ry, bx, by, d)
    return (nrx,nry),(nbx,nby)
q = deque()
visited = {}
q.append((r,b))
visited[(r,b)] = 0
ans = 0
while q:
    r,b = q.popleft()
    rx,ry = r
    bx,by = b
    if (rx,ry) == hole:
        if visited[(r,b)] <= 10:
            ans = visited[(r,b)]
        break
    for d in range(4):
        (nrx,nry),(nbx,nby) = go(rx,ry,bx,by,d)
        if (nbx,nby) == hole:
            continue
        if ((nrx,nry),(nbx,nby)) not in visited.keys():
            visited[(nrx,nry),(nbx,nby)] = visited[(r,b)] + 1
            q.append(((nrx,nry),(nbx,nby)))
print(1 if ans >= 1 else 0)

# print(go(1,3,1,5,3))
# print(go(3,1,2,1,0))
"""
5 5
#####
#O###
#R###
#B###
#####

5 5
#####
#O###
#B###
#R###
#####

5 5
#####
#O#.#
#R#.#
#.#B#
#####

3 5
#####
#OBR#
#####

3 5
#####
#ORB#
#####

3 5
#..R#
#O###
#..B#

5 5
#####
#R#.#
#.O.#
#.#B#
#####
"""