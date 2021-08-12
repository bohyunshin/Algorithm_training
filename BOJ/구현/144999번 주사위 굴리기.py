n,m,x,y,k = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
moves = list(map(int, input().split()))

cube = {}
for i in range(1,7):
    cube[i] = 0
state = (6, cube[6])

dx = [0,0,-1,1]
dy = [1,-1,0,0]
# 전개도 표현.
east_west = [4,1,3,6]
south_north = [2,1,5,6]

for move in moves:
    nx = x + dx[move-1]
    ny = y + dy[move-1]
    if 0 <= nx < n and 0 <= ny < m:
        if move == 1:
            east_west = east_west[-1:] + east_west[:-1]
            south_north[1] = east_west[1]
            south_north[3] = east_west[3]
        if move == 2:
            east_west = east_west[1:] + east_west[:1]
            south_north[1] = east_west[1]
            south_north[3] = east_west[3]
        if move == 3:
            south_north = south_north[1:] + south_north[:1]
            east_west[1] = south_north[1]
            east_west[3] = south_north[3]
        if move == 4:
            south_north = south_north[-1:] + south_north[:-1]
            east_west[1] = south_north[1]
            east_west[3] = south_north[3]

        top_loc, down_loc = south_north[1], south_north[3]
        if A[nx][ny] == 0:
            A[nx][ny] = cube[down_loc]
        else:
            cube[down_loc] = A[nx][ny]
            A[nx][ny] = 0
        x = nx
        y = ny
        print(cube[top_loc])