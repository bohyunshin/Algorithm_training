from collections import deque, defaultdict
# 배열을 초기화하는 과정에서도 시간초과가 뜰 수 있다는 것을 인지하셈!!!
n,m = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y,visited_total,number_total):
    global number
    visited = defaultdict(int)
    visited[(x,y)] = 1
    visited_total[x][y] = True
    number_total[x][y] = number
    q = deque()
    q.append((x,y))
    result = []
    result.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[(nx,ny)] == 0 and A[nx][ny] == 1:
                result.append((nx,ny))
                visited[(nx,ny)] = visited[(x,y)] + 1
                visited_total[nx][ny] = True
                number_total[nx][ny] = number
                q.append((nx,ny))
    return result
number = 0
ans = -1
visited_total = [[False]*m for _ in range(n)]
# cnt_total = [[0]*m for _ in range(n)]
number_total = [[-1]*m for _ in range(n)]
number2cnt = {}
# 우선 현재 연결되어 있는 array 찾고, 그 중 max을 ans에 담아둔다.
for x in range(n):
    for y in range(m):
        if A[x][y] == 0:
            visited_total[x][y] = True
            continue
        if visited_total[x][y]:
            continue
        block = bfs(x,y,visited_total,number_total)
        # for i,j in block:
        #     cnt_total[i][j] = len(block)
        #     number_total[i][j] = number
        ans = max(ans,len(block))
        number2cnt[number] = len(block)
        number += 1
for x in range(n):
    for y in range(m):
        if A[x][y] == 1:
            continue
        tmp = 1
        A[x][y] = 1
        hist = []
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < m and A[nx][ny] == 1:
                number = number_total[nx][ny]
                cnt = number2cnt[number]
                if number not in hist:
                    hist.append(number)
                    tmp += cnt
                    ans = max(ans,tmp)
        A[x][y] = 0
        ans = max(ans,tmp)
print(ans)
