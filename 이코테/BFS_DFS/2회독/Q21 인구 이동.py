from collections import deque

n,l,r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append( list(map(int, input().split())) )

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def process(x,y,index):
    global union
    united = []
    count = 1
    union[x][y] = index
    united.append((x,y))
    summary = graph[x][y]

    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1 and \
                    l <= abs(graph[nx][ny]-graph[x][y]) <= r and union[nx][ny] == -1:
                union[nx][ny] = index
                united.append((nx,ny))
                count += 1
                summary += graph[nx][ny]
                q.append((nx,ny))
    for i,j in united:
        graph[i][j] = summary // count

total_count = 0
while True:
    index = 0
    union = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index += 1
    if index == n*n:
        break
    total_count += 1
print(total_count)