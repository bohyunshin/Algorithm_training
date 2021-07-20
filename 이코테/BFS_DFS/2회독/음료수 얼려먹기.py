n,m = map(int, input().split())
array = []

for _ in range(n):
    array.append( [int(i) for i in input()] )
visited = [[0]*(m) for _ in range(n)]

# 상,하,좌,우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if array[x][y] == 1:
        return
    # 방문 처리
    array[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx,ny)
    return True
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) is True:
            result += 1
print(result)