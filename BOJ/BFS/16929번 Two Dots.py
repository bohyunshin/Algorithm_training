n,m = map(int, input().split())
game = [[i for i in input()] for _ in range(n)]

visited = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 평소랑 똑같이 bfs 구현
# 단, 순환하는 조건 추가하기 위해서 아래 조건을 추가함
# 이동할 점 (nx,ny)가 이미 방문 했고 바로 이전에 위치한 점이 아닐때!
# -> (nx != before_x or ny != before_y) & visited[x][y] is True
# * -> * -> *
# *    * <- *
def bfs(x,y,before_x, before_y, color):
    # 이동할 점이 색깔도 같고
    # (nx != before_x or ny != before_y) 조건도 충족하는데
    # 이미 방문까지 했다면 걔는 순환하는게 존재하는 거임
    if visited[x][y] is True:
        return True
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if game[nx][ny] == color and (nx != before_x or ny != before_y):
                if bfs(nx,ny,x,y,color):
                    return True
                # bfs(nx, ny, x, y, color)
    return False

for i in range(n):
    for j in range(m):
        if visited[i][j] is True:
            continue
        if bfs(i,j,-1,-1,game[i][j]):
            print('Yes')
            exit(0)
print('No')