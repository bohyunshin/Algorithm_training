from collections import deque
n,m = map(int,input().split())
a = [[0]*(m+1)]
for _ in range(n):
    a.append([0] + list(map(int,input().split())))
s = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j]

def get_sum(a,b,x,y):
    return s[x][y] - s[x][b-1] - s[a-1][y] + s[a-1][b-1]

h,w,s_r,s_c,f_r,f_c = map(int,input().split())
# s_r -= 1
# s_c -= 1
# f_r -= 1
# f_c -= 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[-1]*(m+1) for _ in range(n+1)]
q = deque()
visited[s_r][s_c] = 0
q.append((s_r,s_c))
while q:
    x,y = q.popleft()
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 1 <= nx < n+1 and 1 <= ny < m+1 and \
                visited[nx][ny] == -1 and 1 <= nx+h-1 < n+1 and 1 <= ny+w-1 < m+1 and \
                get_sum(nx,ny,nx+h-1,ny+w-1) == 0:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny))

print(visited[f_r][f_c])



# while q:
#     x,y = q.popleft()
#     for i in range(4):
#         nx,ny = x+dx[i],y+dy[i]
#         if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
#             FLAG = False
#             for j in range(h):
#                 y_ = y
#                 for k in range(w):
#                     if 0 <= nx+j < n and 0 <= ny+k < m and a[nx+j][ny+k] != 1:
#                         pass
#                     else:
#                         FLAG = True
#                         break
#                 if FLAG:
#                     break
#                 y = y_
#             if FLAG == False:
#                 visited[nx][ny] = visited[x][y] + 1
#                 q.append((nx,ny))
# print(visited[f_r][f_c])