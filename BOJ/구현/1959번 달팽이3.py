n,m = map(int, input().split())
visited = [[0]*m for _ in range(n)]
# 차례대로 오른쪽, 아래, 왼쪽, 위.
dx = [0,1,0,-1]
dy = [1,0,-1,0]
ans = 0
# 초기 시작점은 (0,0)
x,y = (0,0)
# 초기 방향은 오른쪽.
d = 0
def turn(d):
    if d in [0,1,2]:
        return d+1
    else:
        return 0
while visited[x][y] == 0:
    visited[x][y] = 1
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            x = nx
            y = ny
        else:
            ans += 1
            d = turn(d)
            break
    # print(x, y, d)
    x = x + dx[d]
    y = y + dy[d]

# for i in visited:
#     print(i)
print(ans-1)
print(x-dx[d]+1,y-dy[d]+1)