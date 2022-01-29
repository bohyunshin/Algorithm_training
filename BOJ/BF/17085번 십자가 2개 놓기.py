from itertools import combinations
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cross = []
x,y = 0,0
LEN = 0
while 0 <= x < n and 0 <= y < m:
    for i in range(x,n):
        for j in range(y,m):
            if a[i][j] != '#':
                continue
            tmp = [(i,j)]
            flag = False
            for k in range(4):
                nx,ny = i,j
                for _ in range(LEN):
                    nx += dx[k]
                    ny += dy[k]
                    if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == '#':
                        tmp.append((nx,ny))
                    else:
                        flag = True
                        break
                if flag:
                    break
            if flag == False:
                cross.append(tmp)
    x += 1
    y += 1
    LEN += 1
ans = -1
for c in combinations(cross,2):
    a,b = c[0],c[1]
    if len(set(a) & set(b)) >= 1:
        continue
    ans = max(ans,len(a)*len(b))
print(ans)
# print(cross)
"""
2 2
# #
# #
"""