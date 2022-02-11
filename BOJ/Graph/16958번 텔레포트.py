n,t = map(int,input().split())
dist = [[1e100]*(n+1) for _ in range(n+1)]
info = [()]
for _ in range(n):
    s,x,y = map(int,input().split())
    info.append((s,x,y))
# 거리 업데이트.
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            continue
        sa,xa,ya = info[i]
        sb,xb,yb = info[j]
        if sa == 1 and sb == 1:
            if dist[i][j] == -1 or dist[i][j] > t:
                dist[i][j] = t
                dist[j][i] = t
        else:
            if dist[i][j] == -1 or dist[i][j] > abs(xa-xb) + abs(ya+yb):
                dist[i][j] = abs(xa-xb) + abs(ya-yb)
                dist[j][i] = abs(xa-xb) + abs(ya-yb)
# 플로이드 와샬 쓰기.
# ans = [[1e100]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dist[i][i] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            # min_dist = dist[i][j]
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            # ans[i][j] = min_dist
m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    print(dist[x][y])