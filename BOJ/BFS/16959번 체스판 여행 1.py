from collections import deque
n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
# 나이트, 비숍, 룩 순서로 3차원 dist 테이블 초기화
vist_n = [[[-1]*(n**2+1) for _ in range(n)] for _ in range(n)]
vist_b = [[[-1]*(n**2+1) for _ in range(n)] for _ in range(n)]
vist_l = [[[-1]*(n**2+1) for _ in range(n)] for _ in range(n)]
q = deque()
# 1위치 찾기
for i in range(n):
    for j in range(n):
        if A[i][j] == 1:
            x,y = i,j
        if A[i][j] == n:
            a,b = i,j
# 1위치에 나이트, 비숍, 룩 놓는 것으로 초기화 세팅
vist_n[x][y][1] = 0
vist_b[x][y][1] = 0
vist_l[x][y][1] = 0
for i in [0,1,2]:
    # 순서대로 x,y 좌표, 어떤 말인지 표시하는 indicator, 몇번째 방문하는 중인지 표시하는 것임.
    q.append((x,y,i,1))
while q:
    x,y,horse,num = q.popleft()
    # 나이트라면
    if horse == 0:
        dx = [-2,2,2,-2]
        dy = [1,1,-1,-1]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and vist_n[nx][ny][A[nx][ny]] == -1:
                vist_n[nx][ny][A[nx][ny]] = vist_n[x][y][num]+1
                if A[nx][ny] == A[x][y] + 1:
                    q.append((nx, ny, horse, num+1))
                else:
                    q.append((nx, ny, horse, num))
    # 비숍이라면, 굳이 끝까지 갈 필요는 없음.
    elif horse == 1:
        dx = [-1,1,1,-1]
        dy = [1,1,-1,-1]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            while 0 <= nx < n and 0 <= ny < n:
                if vist_b[nx][ny][A[nx][ny]] == -1:
                    vist_b[nx][ny][A[nx][ny]] = vist_b[x][y][num] + 1
                    if A[nx][ny] == A[x][y] + 1:
                        q.append((nx, ny, horse, num + 1))
                    else:
                        q.append((nx, ny, horse, num))
                nx += dx[i]
                ny += dy[i]
    # 룩이라면, 굳이 끝까지 갈 필요는 없음.
    elif horse == 2:
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while 0 <= nx < n and 0 <= ny < n:
                if vist_l[nx][ny][A[nx][ny]] == -1:
                    vist_l[nx][ny][A[nx][ny]] = vist_l[x][y][num] + 1
                    if A[nx][ny] == A[x][y] + 1:
                        q.append((nx, ny, horse, num + 1))
                    else:
                        q.append((nx, ny, horse, num))
                nx += dx[i]
                ny += dy[i]
    # 단순히 말을 바꾸는 선택지도 존재함.
    for i in [0,1,2]:
        if i == 0:
            if vist_b[x][y][num] == -1:
                vist_b[x][y][num] = vist_n[x][y][num]
                q.append((x,y,1,num))
            if vist_l[x][y][num] == -1:
                vist_l[x][y][num] = vist_n[x][y][num]
                q.append((x,y,2,num))
        if i == 1:
            if vist_n[x][y][num] == -1:
                vist_n[x][y][num] = vist_b[x][y][num]
                q.append((x,y,0,num))
            if vist_l[x][y][num] == -1:
                vist_l[x][y][num] = vist_b[x][y][num]
                q.append((x,y,2,num))
        if i == 2:
            if vist_n[x][y][num] == -1:
                vist_n[x][y][num] = vist_l[x][y][num]
                q.append((x,y,0,num))
            if vist_b[x][y][num] == -1:
                vist_b[x][y][num] = vist_l[x][y][num]
                q.append((x,y,1,num))
print(vist_n[a][b])
print(vist_b[a][b])
print(vist_l[a][b])
