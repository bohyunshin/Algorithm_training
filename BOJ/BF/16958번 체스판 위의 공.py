from collections import deque
r,c = map(int,input().split())
a = []
for _ in range(r):
    a.append(list(map(int,input().split())))
dx = [-1,0,1,0,-1,1,1,-1]
dy = [0,1,0,-1,1,1,-1,-1]

ans = [0]*(r*c)
parent = [0]*(r*c)

def go(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = go(parent[x])
        return parent[x]

for i in range(r):
    for j in range(c):
        x,y = i,j
        for k in range(8):
            nx,ny = i+dx[k],j+dy[k]
            if 0 <= nx < r and 0 <= ny < c:
                if a[nx][ny] < a[x][y]:
                    x = nx
                    y = ny
        parent[i*c+j] = x*c+y

for i in range(r):
    for j in range(c):
        ans[go(i*c+j)] += 1

for i in range(r):
    print(*ans[i*c:(i+1)*c])

# def move(x,y):
#     d = 0
#     cnt = 0
#     MIN = -1
#     sx,sy = -1,-1
#     for i in range(8):
#         nx,ny = x+dx[i],y+dy[i]
#         if 0 <= nx < r and 0 <= ny < c:
#             d += 1
#             if a[x][y] < a[nx][ny]:
#                 cnt += 1
#             if MIN == -1 or MIN > a[nx][ny]:
#                 MIN = a[nx][ny]
#                 sx,sy = nx,ny
#     return (cnt == d, (sx,sy))
# q = deque()
# ans = [[0]*c for _ in range(r)]
# way = {}
# for i in range(r):
#     for j in range(c):
#         q.append(((i,j),(i,j)))
# while q:
#     now,from_ = q.popleft()
#     if way.get(now) is not None:
#         fn,fy = way[now]
#         ans[fn][fy] += 1
#         continue
#     x,y = now
#     flag,(sx,sy) = move(x,y)
#     if flag:
#         ans[x][y] += 1
#         way[(from_)] = (x,y)
#     else:
#         q.append(((sx,sy),from_))
# for row in ans:
#     print(' '.join(map(str,row)))