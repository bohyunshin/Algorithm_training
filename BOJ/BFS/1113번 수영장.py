from collections import deque

n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append([int(i) for i in input()])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def start(h):
    ans = 0
    for x in range(n):
        for y in range(m):
            if a[x][y] < h and visited[x][y] == False:
                ans += bfs(x,y,h)
    return ans
def bfs(x,y,h):
    q = deque()
    pos = [(x,y)]
    q.append((x,y))
    visited[x][y] = True
    flag = False
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and a[nx][ny] < h:
                    visited[nx][ny] = True
                    pos.append((nx,ny))
                    q.append((nx,ny))
            # 맵을 벗어난다면, 무조건 그 곳에 고이지 않고 밖으로 빠져나감.
            # -> 맵 밖은 높이가 0이기 때문에 무조건 여기로 감.
            # 따라서 이 경우를 따로 표시해줌.
            else:
                flag = True
    if flag:
        return 0
    else:
        water = 0
        for x,y in pos:
            a[x][y] += 1
            water += 1
        return water
result = 0
for h in range(1,10):
    visited = [[False]*m for _ in range(n)]
    # print(h,start(h))
    result += start(h)
print(result)

"""
3 5
111116
111165
111116
"""