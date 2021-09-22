from collections import deque
n,m = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
def convert(d):
    if d == 1:
        return 1
    if d == 2:
        return 3
    if d == 3:
        return 2
    if d == 4:
        return 0
def append_q(x,y,d,nx,ny,nd):
    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][nd] == -1 and A[nx][ny] == 0:
        if (x,y) == (nx,ny):
            q.append((nx,ny,nd))
            visited[nx][ny][nd] = visited[x][y][d] + 1
        # 중간에 모두 벽이 있는지 검사해야 함.
        else:
            mx,my = x+dx[d],y+dy[d]
            while (mx,my) != (nx,ny):
                if A[mx][my] == 1:
                    return
                mx += dx[d]
                my += dy[d]
            # 위에서 모두 안 걸렸다면, 사이에 모두 벽이 없는 경우임.
            q.append((nx, ny, nd))
            visited[nx][ny][nd] = visited[x][y][d] + 1

x,y,d = map(int,input().split())
d = convert(d)
x -= 1
y -= 1
a,b,c = map(int,input().split())
c = convert(c)
a -= 1
b -= 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[[-1]*4 for _ in range(m)] for _ in range(n)]
visited[x][y][d] = 0
q = deque()
q.append((x,y,d))
while q:
    x,y,d = q.popleft()
    if (x,y,d) == (a,b,c):
        print(visited[x][y][d])
        break
    # 왼쪽,오른쪽으로 90도 회전하기.
    for i in [-1,1]:
        nd = ( (d+i) % 4 + 4 ) % 4
        append_q(x,y,d,x,y,nd)
    # 방향 유지하면서 k칸 이동하기.
    for k in range(1,4):
        nx,ny = x+k*dx[d],y+k*dy[d]
        append_q(x,y,d,nx,ny,d)
        # while 0 <= nx < n and 0 <= ny < n:
        #     append_q(x,y,d,nx,ny,d)
        #     nx += dx[i]
        #     ny += dy[i]
# for i in visited:
#     print(i)

"""
5 6
0 0 0 0 0 0
0 1 1 0 1 0
0 1 0 0 0 0
0 0 1 1 1 0
1 0 0 0 0 0
4 2 3
1 2 1
>> 6

5 6
0 0 0 0 0 0
0 1 1 0 1 0
0 1 0 0 0 0
0 0 1 1 1 0
1 0 0 0 0 0
4 2 3
1 2 2
>> 8

5 6
0 0 0 0 0 0
1 1 1 0 1 0
0 1 0 0 0 0
0 0 1 1 1 0
1 0 0 0 0 0
4 2 3
2 4 4
>> 10
"""