from collections import deque
n = int(input())
A = []
for _ in range(n):
    A.append([i for i in input()])
tong = []
dest = []
for i in range(n):
    for j in range(n):
        if A[i][j] == 'B':
            tong.append((i,j))
        if A[i][j] == 'E':
            dest.append((i,j))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q = deque()
visited = {}
visited[tuple(tong)] = 0
q.append(tuple(tong))
while q:
    tong = q.popleft()
    if tong == tuple(dest):
        print(visited[tong])
        exit()
    # 이동.
    for i in range(4):
        tmp = []
        for x,y in tong:
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and A[nx][ny] != '1':
                tmp.append((nx,ny))
        if len(tmp) == 3:
            tmp.sort()
            tmp = tuple(tmp)
            if tmp not in visited.keys():
                visited[tmp] = visited[tong] + 1
                q.append(tmp)
    # 회전.
    # True면 가로 모양, False면 세로 모양.
    garo = (tong[0][0] == tong[1][0] == tong[2][0])
    if garo:
        if 1 <= tong[0][0] <= n-2:
            tmp = ( (tong[1][0]-1,tong[1][1]), (tong[1][0],tong[1][1]), (tong[1][0]+1,tong[1][1]) )
            if tmp not in visited.keys():
                FLAG = False
                for i in [tong[1][0]-1,tong[1][0]+1]:
                    for j in range(tong[0][1],tong[2][1]+1):
                        if A[i][j] == '1':
                            FLAG = True
                            break
                    if FLAG:
                        break
                if FLAG == False:
                    visited[tmp] = visited[tong] + 1
                    q.append(tmp)
    else:
        if 1 <= tong[0][1] <= n-2:
            tmp = ((tong[1][0], tong[1][1]-1), (tong[1][0], tong[1][1]), (tong[1][0], tong[1][1]+1))
            if tmp not in visited.keys():
                FLAG = False
                for j in [tong[1][1] - 1, tong[1][1] + 1]:
                    for i in range(tong[0][0], tong[2][0] + 1):
                        if A[i][j] == '1':
                            FLAG = True
                            break
                    if FLAG:
                        break
                if FLAG == False:
                    visited[tmp] = visited[tong] + 1
                    q.append(tmp)
print(0)