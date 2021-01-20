n,m = map(int, input().split())
x,y,current_direction = map(int, input().split())

# (direction, x, y): 바라보고 있는 방향, 그 방향으로 갈 때 더해줘야하는 x, y 값
# 각각 북 동 남 서
steps = [(0,-1,0), (1,0,1), (2,1,0), (3,0,-1)]
steps_order = [(0,-1,0), (3,0,-1), (2,1,0), (1,0,1)]
steps_backward = [(0,1,0), (1,0,-1), (2,-1,0), (3,0,1)]

game_map = []
for i in range(m):
    row = list(map(int, input().split()))
    game_map.append(row)

# 바라봐야하는 순서는 북 -> 서 -> 남 -> 동 -> 북
order = [0,3,2,1]

hitting_point = 1

curr2next = {0:3, 3:1, 2:1, 1:0}

while True:

    next_direction = curr2next[current_direction]
    visit_order = steps_order[next_direction:] + steps_order[:next_direction]

    ISMOVE = False
    for step in visit_order:

        nx = x + step[1]
        ny = y + step[2]
        next_direction = step[0]
        # 만약 바다이거나 이미 가본 곳이라면 (가본 곳은 2로 표시할 것임)
        # 방향만 바꾸고 다시 다음 방향을 바라봄
        if game_map[nx][ny] == 1 or game_map[nx][ny] == 2:
            continue
        else:
            # 가본 곳을 2로 업데이트 함
            temp = game_map[nx]
            temp[ny] = 2
            game_map[nx] = temp
            # 바라보는 방향을 바꿈
            current_direction = next_direction
            # 방문했으므로 1 값을 더해줌
            hitting_point += 1
            # for loop을 탈출함
            ISMOVE = True
            x,y = nx,ny
            break

    if ISMOVE:
        continue
    # 네 방향 모두 가본 곳이거나 바다라면
    # 바라보는 방향 유지한 채로 한칸 뒤로 간다
    else:
        step = steps_backward[current_direction]
        nx = x + step[1]
        ny = y + step[2]
        if game_map[nx][ny] == 1 or game_map[nx][ny] == 2:
            break
        else:
            x,y = nx,ny
            hitting_point += 1

print(game_map)
print(hitting_point)