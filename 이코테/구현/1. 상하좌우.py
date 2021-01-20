# 내 풀이
n = int(input())
paths = input().split()

start = [1,1]
for p in paths:
    if p == 'R':
        start[1] = start[1] + 1
    elif p == 'L':
        start[1] = start[1] - 1
    elif p == 'U':
        start[0] = start[0] - 1
    else:
        start[0] = start[0] + 1

    if start[0] <= 0 or start[0] > n:
        start[0] = start[0] + 1
    elif start[1] <= 0 or start[0] > n:
        start[1] = start[1] + 1

    print(start)

# 책 풀이
n = int(input())
paths = input().split()

x,y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

for p in paths:
    for i, move in enumerate(move_types):
        if p == move:
            nx = x + dx[i]
            ny = y + dy[i]
            break

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    else:
        x,y = nx,ny
print(x,y)
