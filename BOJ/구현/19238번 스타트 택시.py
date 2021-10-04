from collections import deque
n,m,k = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
x,y = map(int,input().split())
x -= 1
y -= 1
son = []
for _ in range(m):
    a,b,c,d = map(int,input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    son.append([a,b,c,d])

def bfs(start,end=None):
    x,y = start
    if end is not None:
        w,z = end
    visited = [[1e100]*n for _ in range(n)]
    q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited[x][y] = 0
    q.append((x,y))
    while q:
        x,y = q.popleft()
        if end is not None and (x,y) == (w,z):
            return visited
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 1e100 and A[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    return visited

def make_candidate(visited,son):
    criteria = []
    for a,b,c,d in son:
        tmp = []
        tmp.append(visited[a][b])
        tmp.append(a)
        tmp.append(b)
        tmp.append(c)
        tmp.append(d)
        criteria.append(tmp)
    criteria.sort(key=lambda x: (x[0],x[1],x[2]))
    return criteria

while True:
    visited = bfs((x,y))
    candidate = make_candidate(visited,son)
    sel_son = candidate[0]
    fuel_to_start_point = sel_son[0]
    a,b,c,d = sel_son[1:]
    visited = bfs((a,b),(c,d))
    fuel_to_end_point = visited[c][d]
    if k - (fuel_to_start_point + fuel_to_end_point) < 0:
        print(-1)
        exit()
    else:
        k -= fuel_to_start_point + fuel_to_end_point
        k += 2*fuel_to_end_point
    x,y = c,d
    son = [[a,b,c,d] for z,a,b,c,d in candidate[1:]]
    if len(son) == 0:
        print(k)
        exit()