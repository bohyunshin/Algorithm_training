from collections import deque
n,m = map(int,input().split())
a = [input() for _ in range(n)]
c = []
for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
            x,y = i,j
        if a[i][j] == 'C':
            c.append((i,j))
visited = [[[[-1]*4 for _ in range(4)] for _ in range(m)] for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
q = deque()
for i in range(4):
    visited[x][y][i][2] = 0
    q.append((x,y,i,2))
ans = -1
while q:
    x,y,d,state = q.popleft()
    if state == 3:
        ans = visited[x][y][d][state]
        break
    for i in range(4):
        if i == d:
            continue
        nx,ny = x+dx[i],y+dy[i]
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] != '#':
            # 방문할 곳에 선물이 있다면,
            if a[nx][ny] == 'C':
                index = c.index((nx, ny))
                # 선물을 하나도 배달하지 않았고 처음 방문한다면, state를 index로 업데이트.
                # 선물 배달 -> index 선물 배달이므로.
                if state == 2 and visited[nx][ny][i][index] == -1:
                    visited[nx][ny][i][index] = visited[x][y][d][state] + 1
                    q.append((nx,ny,i,index))
                # 선물을 하나 배달했고 (state in [0,1])
                # 배달한 선물이 현재 방문한 곳의 선물과 다르다면 (state != index)
                # 선물을 모두 배달한 것이니까 state를 3으로 업데이트 함.
                elif state in [0,1] and state != index and visited[nx][ny][i][3] == -1:
                    visited[nx][ny][i][3] = visited[x][y][d][state] + 1
                    q.append((nx, ny, i, 3))
            else:
                # 방문한 곳이 선물이 아니라면 현재 state를 그대로 업데이트 해줌.
                if visited[nx][ny][i][state] == -1:
                    visited[nx][ny][i][state] = visited[x][y][d][state] + 1
                    q.append((nx,ny,i,state))
print(ans)