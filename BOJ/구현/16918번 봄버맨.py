r,c,n = map(int,input().split())
A = []
for _ in range(r):
    A.append([i for i in input()])
time = [[-1]*c for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(r):
    for j in range(c):
        if A[i][j] == 'O':
            time[i][j] = 3
for t in range(1,n+1):
    # 시간 줄이기.
    for i in range(r):
        for j in range(c):
            if time[i][j] != -1:
                time[i][j] -= 1
    # 처음 1초 동안에는 움직이지 않음.
    if t == 1:
        continue
    for i in range(r):
        for j in range(c):
            if t % 2 == 0:
                if A[i][j] == '.':
                    A[i][j] = 'O'
                    time[i][j] = 3
            else:
                if time[i][j] == 0:
                    A[i][j] = '.'
                    time[i][j] = -1
                    for k in range(4):
                        nx,ny = i+dx[k],j+dy[k]
                        if 0 <= nx < r and 0 <= ny < c and A[nx][ny] == 'O' and time[nx][ny] != 0:
                            time[nx][ny] = -1
                            A[nx][ny] = '.'
    # if t == 4:
    #     break
for i in A:
    print(''.join(i))

