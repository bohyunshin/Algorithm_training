n,m = map(int, input().split())
x, y, direction = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]

# 가본 곳을 표시해주는 맵 생성
d = [ [0]*m for _ in range(n) ]

# 처음 시작점을 가봤다고 표시해줌
d[x][y] = 1

# 북,동,남,서로 움직일때 dx, dy 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 방향을 회전하는 함수 정의
def turn_left():
    # 전역적으로 정의
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
# turn_time이 4라면 문제에서 3번을 수행
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()

    nx = x + dx[direction]
    ny = y + dy[direction]

    # 아직 가보지 않은 칸이 존재하고 그곳이 바다가 아니라면
    # 그곳으로 전진
    if d[nx][ny] == 0 and game_map[nx][ny] == 0:
        x = nx
        y = ny
        # 가봤다고 표시해줌
        d[nx][ny] = 1
        # turn_time을 초기화해줌
        turn_time = 0

        count += 1
        continue
    # 아니라면 다시 회전해줌 (while loop 처음으로 되돌아감)
    else:
        turn_time += 1

    # 3번에 대한 수행 코드임
    # 만약 네 방향 모두 이미 가본칸이거나 바다로 되어있는 칸인 경우
    # 어떤 경우에서든지 turn_time == 4인 경우임
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        turn_time = 0

        # 뒤로간 칸이 바다라면 while loop을 탈출함
        if game_map[nx][ny] == 1:
            break
        # 뒤로간 칸이 바다가 아니라면 그곳으로 이동하고 다시 while loop으로 돌아감
        else:
            x = nx
            y = ny

print(count)