n = int(input())
game_map = [[0]*(n+1) for _ in range(n+1)]
snake_map = [[0]*(n+1) for _ in range(n+1)]
k = int(input())
for _ in range(k):
    x,y = map(int,input().split())
    game_map[x][y] += 1
l = int(input())
direction = {}
for _ in range(l):
    time, d = input().split()
    direction[int(time)] = d

snake = [(1,1)]

dir_ = ['U','R','D','L']

d = 'R'
time = 0
snake_map[1][1] = 1
while True:
    x,y = snake[0]
    # print(x,y)
    x_t, y_t = snake[-1]
    # print(x_t,y_t)
    time += 1
    if d == 'R':
        y += 1
    elif d == 'L':
        y -= 1
    elif d == 'U':
        x -= 1
    else:
        x += 1
    # 머리가 밖으로 가거나 꼬리랑 닿으면 게임 종료
    if x >= n+1 or y >= n+1 or x <= 0 or y <= 0 or (snake_map[x][y] == 1):
        break

    # 머리 이동
    snake = [(x,y)] + snake
    snake_map[x][y] = 1
    # 사과가 있다면 꼬리 안 자름. 없다면 꼬리 자름
    if game_map[x][y] == 1:
        game_map[x][y] -= 1
    else:
        snake.pop()
        snake_map[x_t][y_t] -= 1

    # 방향 이동
    if time in direction.keys():
        v = direction[time]
        index = dir_.index(d)
        # 오른쪽으로 회전이라면
        if v == 'D':
            if index == len(dir_)-1:
                d = 'U'
            else:
                d = dir_[index+1]
        # 왼쪽으로 회전이라면
        else:
            if index == 0:
                d = dir_[-1]
            else:
                d = dir_[index-1]

print(time)
