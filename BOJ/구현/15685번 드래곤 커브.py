def rotate(x,y,a,b):
    if x >= a:
        n = y - (x-a)
    else:
        n = y + (a-x)
    if y >= b:
        m = x + (y-b)
    else:
        m = x - (b-y)
    return m,n

n = int(input())
dragon_coord_list = []
for _ in range(n):
    x,y,d,g = map(int,input().split())
    dragon = [(x,y)]
    if d == 0:
        dragon.append((x+1,y))
    if d == 1:
        dragon.append((x,y-1))
    if d == 2:
        dragon.append((x-1,y))
    if d == 3:
        dragon.append((x,y+1))

    # 세대수 늘리기
    for _ in range(g):
        # 기준점
        x, y = dragon[-1]
        temp = []
        for a,b in dragon[:-1][::-1]:
            a,b = rotate(x,y,a,b)
            temp.append((a,b))
        # 회전한 드래곤 커브 합치기
        dragon.extend(temp)
    dragon_coord_list.extend(dragon)
min_x = 1e100
min_y = 1e100
max_x = -1e100
max_y = -1e100
visited = [[0]*200 for _ in range(200)]
for x,y in set(dragon_coord_list):
    if min_x > x:
        min_x = x
    if min_y > y:
        min_y = y
    if max_x < x:
        max_x = x
    if max_y < y:
        max_y = y
    visited[x][y] = 1

x,y = min_x, min_y
dx = [0,1,1,0]
dy = [0,0,1,1]

answer = 0
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= 101 and 0 <= ny <= 101:
                if visited[nx][ny] == 1:
                    cnt += 1
        if cnt == 4:
            answer += 1
print(answer)