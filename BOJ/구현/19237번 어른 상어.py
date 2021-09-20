from collections import defaultdict
n,m,k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

shark = [0]*(m+1)
direction = list(map(int, input().split()))
for i in range(m):
    shark[i+1] = direction[i]

priority = defaultdict(list)
for i in range(1,m+1):
    for _ in range(4):
        priority[i].append(list(map(int, input().split())))

smell_time = [[0]*n for _ in range(n)]
smell_number = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            smell_time[i][j] = k
            smell_number[i][j] = board[i][j]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(board):
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2:
                return False
    return True

time = 0
while not check(board):
    smell_to_add = []
    for s in range(1,m+1):
        for x in range(n):
            for y in range(n):
                FLAG = False
                if board[x][y] == s:
                    d = shark[s]
                    # 인접한 칸 중, 아무 냄새가 없는 칸을 찾음.
                    for i in priority[s][d-1]:
                        nx,ny = x+dx[i-1],y+dy[i-1]
                        if 0 <= nx < n and 0 <= ny < n and smell_time[nx][ny] == 0:
                            # 이동할 곳에, 더 작은 번호의 상어가 있따면,
                            # 걔는 격자 밖으로 퇴출임.
                            if board[nx][ny] >= 1 and board[nx][ny] < board[x][y]:
                                board[x][y] = 0
                                FLAG = True
                                break
                            # 상어 이동시키기. 번호가 작은 애들부터 이동시키는 것임.
                            board[x][y] = 0
                            board[nx][ny] = s
                            # 나중에 냄새 추가할 위치.
                            # 여기는 k로 추가하는 것임.
                            smell_to_add.append((nx,ny))
                            # 상어의 방향을 바꿔줘야 함.
                            shark[s] = i
                            # 이동할 시에, 냄새를 남겨야 함.
                            smell_number[nx][ny] = s
                            FLAG = True
                            break
                    # 인접한 칸 중, 아무 냄새가 없는 곳이 없다면,
                    # 자신의 냄새가 있는 칸의 방향으로 잡아야 함.
                    if FLAG == False:
                        for i in priority[s][d-1]:
                            nx,ny = x+dx[i-1],y+dy[i-1]
                            # if s == 2 and (x,y) == (1,3):
                            #     print(nx,ny)
                            if 0 <= nx < n and 0 <= ny < n and smell_number[nx][ny] == s:
                                # 이동할 곳에, 더 작은 번호의 상어가 있따면,
                                # 걔는 격자 밖으로 퇴출임.
                                if board[nx][ny] >= 1 and board[nx][ny] < board[x][y]:
                                    board[x][y] = 0
                                    FLAG = True
                                    break
                                board[x][y] = 0
                                board[nx][ny] = s
                                # 나중에 냄새 추가할 위치.
                                # 여기는 k로 추가하는 것임.
                                smell_to_add.append((nx,ny))
                                # 상어의 방향울 바꿔줘야 함.
                                shark[s] = i
                                # 이동할 시에, 냄새를 남겨야 함.
                                smell_number[nx][ny] = s
                                FLAG = True
                                break
                if FLAG:
                    break
            if FLAG:
                break

    for x,y in smell_to_add:
        smell_time[x][y] = k

    for x in range(n):
        for y in range(n):
            if (x,y) in smell_to_add:
                continue
            if smell_time[x][y] >= 1:
                smell_time[x][y] -= 1
            # time == 0이면 냄새를 없애야 함.
            if smell_time[x][y] == 0:
                smell_number[x][y] = 0
    time += 1

    if time > 1000:
        print(-1)
        exit()
print(time)