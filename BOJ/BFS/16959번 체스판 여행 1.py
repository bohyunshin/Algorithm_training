from collections import deque
n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
# 나이트, 비숍, 룩 순서로 3차원 dist 테이블 초기화
visited = [[[[-1]*3 for _ in range(n*n)] for _ in range(n)] for _ in range(n)]
q = deque()
# 1위치 찾기
for i in range(n):
    for j in range(n):
        A[i][j] -= 1
        if A[i][j] == 0:
            for k in range(3):
                visited[i][j][0][k] = 0
                q.append((i,j,0,k))
ans = -1
while q:
    x,y,num,horse = q.popleft()
    # 끝까지 간 경우
    if num == n*n-1:
        if ans == -1 or ans > visited[x][y][num][horse]:
            ans = visited[x][y][num][horse]
    # 말 바꾸는 경우
    for i in range(3):
        # 말이 동일한 경우는 바꾸지 않음.
        if horse == i:
            continue
        if visited[x][y][num][i] == -1:
            visited[x][y][num][i] = visited[x][y][num][horse] + 1
            q.append((x,y,num,i))
    # 나이트라면
    if horse == 0:
        dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        for i in range(8):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                next_num = num
                if A[nx][ny] == num+1:
                    next_num = num+1
                if visited[nx][ny][next_num][horse] == -1:
                    visited[nx][ny][next_num][horse] = visited[x][y][num][horse]+1
                    q.append((nx,ny,next_num,horse))
    # 비숍이라면, 굳이 끝까지 갈 필요는 없음.
    elif horse == 1:
        dx = [-1,1,1,-1]
        dy = [1,1,-1,-1]
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            while 0 <= nx < n and 0 <= ny < n:
                next_num = num
                if A[nx][ny] == num+1:
                    next_num = num+1
                if visited[nx][ny][next_num][horse] == -1:
                    visited[nx][ny][next_num][horse] = visited[x][y][num][horse]+1
                    q.append((nx,ny,next_num,horse))
                nx += dx[i]
                ny += dy[i]
    # 룩이라면, 굳이 끝까지 갈 필요는 없음.
    elif horse == 2:
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while 0 <= nx < n and 0 <= ny < n:
                next_num = num
                if A[nx][ny] == num + 1:
                    next_num = num + 1
                if visited[nx][ny][next_num][horse] == -1:
                    visited[nx][ny][next_num][horse] = visited[x][y][num][horse] + 1
                    q.append((nx, ny, next_num, horse))
                nx += dx[i]
                ny += dy[i]
print(ans)