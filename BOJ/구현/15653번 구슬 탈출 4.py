from collections import deque
n,m = map(int,input().split())
A = []
for _ in range(n):
    A.append([i for i in input()])
for i in range(n):
    for j in range(m):
        if A[i][j] == 'B':
            blue = (i,j)
        if A[i][j] == 'R':
            red = (i,j)
        if A[i][j] == 'O':
            hole = (i,j)
visited = {}
q = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited[(red,blue)] = 0
q.append((red,blue))
while q:
    (red,blue) = q.popleft()
    if red == hole:
        print(visited[(red,blue)])
        exit()
        break
    x_r,y_r = red
    x_b,y_b = blue
    for i in range(4):
        nx_r, ny_r = x_r + dx[i], y_r + dy[i]
        nx_b, ny_b = x_b + dx[i], y_b + dy[i]
        # red부터 움직임.
        if (x_r == x_b and y_r < y_b and i == 2) or \
                (x_r == x_b and y_r > y_b and i == 3) or \
                (y_r == y_b and x_r < x_b and i == 0) or \
                (y_r == y_b and x_r > x_b and i == 1):
            while True:
                if (nx_r,ny_r) == hole:
                    break
                if A[nx_r][ny_r] == '#':
                    nx_r -= dx[i]
                    ny_r -= dy[i]
                    break
                nx_r += dx[i]
                ny_r += dy[i]
            while True:
                if (nx_b,ny_b) == hole:
                    break
                if A[nx_b][ny_b] == '#' or (nx_b,ny_b) == (nx_r,ny_r):
                    nx_b -= dx[i]
                    ny_b -= dy[i]
                    break
                nx_b += dx[i]
                ny_b += dy[i]
            if (nx_b,ny_b) == hole:
                continue
            if ((nx_r,ny_r),(nx_b,ny_b)) not in visited.keys():
                visited[(nx_r,ny_r),(nx_b,ny_b)] = visited[(red,blue)] + 1
                q.append(((nx_r,ny_r),(nx_b,ny_b)))
                continue
        if (x_r == x_b and y_r < y_b and i == 3) or \
                (x_r == x_b and y_r > y_b and i == 2) or \
                (y_r == y_b and x_r < x_b and i == 1) or \
                (y_r == y_b and x_r > x_b and i == 0):
            # blue부터 움직임.
            while True:
                if (nx_b,ny_b) == hole:
                    break
                if A[nx_b][ny_b] == '#':
                    nx_b -= dx[i]
                    ny_b -= dy[i]
                    break
                nx_b += dx[i]
                ny_b += dy[i]
            while True:
                if (nx_r,ny_r) == hole:
                    break
                if A[nx_r][ny_r] == '#' or (nx_b,ny_b) == (nx_r,ny_r):
                    nx_r -= dx[i]
                    ny_r -= dy[i]
                    break
                nx_r += dx[i]
                ny_r += dy[i]
            if (nx_b,ny_b) == hole:
                continue
            if ((nx_r,ny_r),(nx_b,ny_b)) not in visited.keys():
                visited[(nx_r,ny_r),(nx_b,ny_b)] = visited[(red,blue)] + 1
                q.append(((nx_r,ny_r),(nx_b,ny_b)))
                continue

        while True:
            if (nx_r, ny_r) == hole:
                break
            if A[nx_r][ny_r] == '#':
                nx_r -= dx[i]
                ny_r -= dy[i]
                break
            nx_r += dx[i]
            ny_r += dy[i]
        while True:
            if (nx_b, ny_b) == hole:
                break
            if A[nx_b][ny_b] == '#':
                nx_b -= dx[i]
                ny_b -= dy[i]
                break
            nx_b += dx[i]
            ny_b += dy[i]
        if (nx_b, ny_b) == hole:
            continue
        if ((nx_r, ny_r), (nx_b, ny_b)) not in visited.keys():
            visited[(nx_r, ny_r), (nx_b, ny_b)] = visited[(red, blue)] + 1
            q.append(((nx_r, ny_r), (nx_b, ny_b)))
            continue
print(-1)

"""
5 4
#######
#..R..#
#..B..#
#..O..#
#######
"""