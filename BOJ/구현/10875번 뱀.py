from collections import defaultdict
L = int(input())
m = 2*L+1
n = int(input())
info = []
for _ in range(n):
    time,d = input().split()
    time = int(time)
    info.append((time,d))
dx = [-1,0,1,0]
dy = [0,1,0,-1]
x,y = L,L
direction = 1
visited = defaultdict(dict)
# visited[x]: x번째 행에서 뱀이 있는 위
visited[x][y] = 1
ans = 0
for time,d in info:
    FLAG = False
    for _ in range(time):
        nx,ny = x+dx[direction],y+dy[direction]
        if 0 <= nx < m and 0 <= ny < m:
            try:
                visited[nx][ny]
                ans += 1
                FLAG = True
                break
            except:
                visited[nx][ny] = 1
                ans += 1
                x,y = nx,ny
        else:
            ans += 1
            FLAG = True
            break
    if FLAG:
        break
    if d == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
# for i in visited.keys():
#     print(visited[i],i)
print(ans)

"""
3
2
100 L
100 L
"""