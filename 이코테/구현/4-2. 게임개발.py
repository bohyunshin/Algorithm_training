n,m = map(int, input().split())

d = [[0]*m for _ in range(n)]

x,y,direction = map(int, input().split())
# 현재 좌표 방문 처리
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction  == -1:
        direction = 3

count = 1
# turn_time이 4가 되면 네 방향을 모두 바라본 것임
turn_time = 0
while True:
    # 반시계 90도 만큼
    turn_left()
    # 그때의 좌표는?
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 그 좌표가 가보지 않은 곳인지, 바다인지 체크해봄
    # 만약 둘다 아니라면 그곳으로 이동함
    if d[nx][ny] != 1 and array[nx][ny] != 1:
        x = nx
        y = ny
        count += 1
        turn_time = 0
        # 방문했다고 처리해줌
        d[nx][ny] = 1
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        turn_time = 0
        # 뒤로 갈 수 있다면
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 바다로 막혀있다면
        else:
            break

print(count)