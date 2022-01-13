from collections import deque
n,k = map(int,input().split())
a = []
for _ in range(2):
    a.append([int(i) for i in input()])
visited = [[-1]*n for _ in range(2)]
q = deque()
visited[0][0] = 0
q.append((0,0,0))
dx = [-1,1,k]
ans = 0
while q:
    x,y,t = q.popleft()
    for i in dx:
        if i == k:
            nx,ny = 1-x,y+k
        else:
            nx,ny = x,y+i
        if 0 <= nx < 2 and 0 <= ny < n and a[nx][ny] == 1 and\
                visited[nx][ny] == -1 and ny > t:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny,t+1))
        # 상근이가 맵을 넘어서면 게임이 끝난다.
        elif 0 <= nx < 2 and ny >= n:
            ans = 1
print(ans)

"""
6 1
100010
001000

6 2
100010
001000

1 100
1
1
"""