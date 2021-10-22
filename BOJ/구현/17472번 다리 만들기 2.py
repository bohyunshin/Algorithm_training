from collections import deque,defaultdict
n,m = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    visited[x][y] = True
    q.append((x,y))
    result = [(x,y)]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and A[nx][ny] == 1:
                q.append((nx,ny))
                result.append((nx,ny))
                visited[nx][ny] = True
    return result

cnt = 1
visited = [[False]*m for _ in range(n)]
islands = [[0]*m for _ in range(n)]
islands_loc = []
# bfs를 통해서 섬을 알아내자.
for x in range(n):
    for y in range(m):
        if visited[x][y] or A[x][y] == 0:
            continue
        result = bfs(x,y)
        for i,j in result:
            visited[i][j] = True
            islands[i][j] = cnt
            islands_loc.append((i,j))
        cnt += 1

def make_bridge(x,y,islands):
    global possible_bridge
    f = islands[x][y]
    for d in range(4):
        # print(d)
        result = []
        nx,ny = x,y
        nx += dx[d]
        ny += dy[d]
        while 0 <= nx < n and 0 <= ny < m and islands[nx][ny] == 0:
            result.append((nx,ny))
            nx += dx[d]
            ny += dy[d]
        if len(result) <= 1:
            continue
        if 0 <= nx < n and 0 <= ny < m and islands[nx][ny] != 0:
            result.sort(key=lambda x: (x[0],x[1]))
            t = islands[nx][ny]
            key = tuple(sorted([f,t]))
            if result not in possible_bridge[key]:
                possible_bridge[key].append(result)
possible_bridge = defaultdict(list)
# make_bridge(6,5,islands)
# for i in islands:
#     print(i)
# print(possible_bridge)

# 각 섬의 가장자리를 돌면서, 다른 섬까지 놓을 수 있는 다리의 모든 수를 기록 함.
dx = [0,1,0,-1]
dy = [1,0,-1,0]
edges = []
for c in range(1,cnt):
    island = []
    for i in range(n):
        for j in range(m):
            if islands[i][j] == c:
                island.append((i,j))
    d = 0
    min_x,min_y,max_x,max_y = 1e100,1e100,-1e100,-1e100
    for x,y in island:
        min_x = min(min_x,x)
        min_y = min(min_y,y)
        max_x = max(max_x,x)
        max_y = max(max_y,y)
    point = [(min_x,min_y),(min_x,max_y),(max_x,max_y),(max_x,min_y)]
    edge = []
    # 섬이 가로 모양인 경우,
    if min_x == max_x:
        for y in range(min_y,max_y+1):
            edge.append((min_x,y))
        edges.append(edge)
        continue
    # 섬이 세로 모양인 경우,
    if min_y == max_y:
        for x in range(min_x,max_x+1):
            edge.append((x,min_y))
        edges.append(edge)
        continue
    x,y = min_x,min_y
    if A[x][y] == 1:
        edge = [(x,y)]
    else:
        edge = []
    while True:
        # print(x,y)
        x += dx[d]
        y += dy[d]
        if (x,y) == (min_x,min_y):
            break
        if A[x][y] == 1:
            edge.append((x,y))
        if (x,y) in point:
            d = (d+1)%4
    edges.append(edge)
# edges을 돌며 가능한 다리를 세워본다.
for edge in edges:
    for x,y in edge:
        if A[x][y] == 1:
            make_bridge(x,y,islands)
final_bridge = {}
for loc in possible_bridge.keys():
    LEN = 1e100
    for br in possible_bridge[loc]:
        if LEN > len(br):
            LEN = len(br)
            final_bridge[loc] = br
f_t_info = list(final_bridge.keys())
c = [False]*len(f_t_info)
ans = 1e100
# 섬의 개수 구하기.
cnt = -1
for i in range(n):
    for j in range(m):
        if islands[i][j] >= 1:
            cnt = max(cnt,islands[i][j])

def check(x,graph,cnt):
    visited = [False]*(cnt+1)
    q = deque()
    visited[x] = True
    q.append(x)
    result = [x]
    while q:
        x = q.popleft()
        for v in graph[x]:
            if visited[v] == False:
                q.append(v)
                visited[v] = True
                result.append(v)
    return len(result) == cnt

def recursive(index,start,l):
    global ans
    if index >= l:
        br = []
        graph = [[] for _ in range(cnt+1)]
        for j in range(len(f_t_info)):
            if c[j]:
                a,b = f_t_info[j]
                graph[a].append(b)
                graph[b].append(a)
                br += final_bridge[f_t_info[j]]
        # 다리를 놓아보기.
        for x,y in br:
            A[x][y] = 1

        # 섬들을 모두 방문했따면,
        tmp = 0
        if check(1,graph,cnt):
            tmp += len(br)
            ans = min(ans, tmp)

        # 다리를 부셔야함.
        for x, y in br:
            A[x][y] = 0
        # print(br,check(1,graph,cnt))
        return
    for i in range(start,len(f_t_info)):
        c[i] = True
        recursive(index+1,i+1,l)
        c[i] = False
        recursive(index+1,i+1,l)
recursive(0,0,len(f_t_info))
print(-1 if ans == 1e100 else ans)

"""
8 8
0 0 0 1 1 1 1 0
0 1 1 1 1 0 1 0
0 1 0 1 1 1 0 0
0 1 0 0 0 1 0 0
0 0 0 1 0 0 1 0
0 0 0 0 0 1 0 0
0 1 1 1 0 0 0 0
0 1 0 0 0 1 0 0
"""

"""
9 6
0 0 0 0 1 0
0 0 0 0 0 0
0 1 0 0 0 1
0 0 0 0 0 0
0 0 0 0 0 0
0 1 0 0 1 1
0 0 0 0 0 0
0 0 0 0 0 0
0 1 0 0 0 0

9 6
0 0 0 0 1 0 
0 0 0 0 0 0 
0 1 0 0 0 1 
0 0 0 0 0 0 
0 0 0 0 0 0 
0 1 0 0 1 1 
0 0 0 0 0 0 
0 0 0 0 0 0 
0 1 0 0 0 0

5 6
1 1 0 0 0 1
1 1 0 0 0 1
0 0 0 0 0 1
0 0 0 0 0 1
1 1 1 1 1 1

6 5
1 1 0 0 1
1 1 0 0 1
0 0 0 0 1
0 0 0 0 1
0 0 0 0 1
1 1 1 1 1
"""