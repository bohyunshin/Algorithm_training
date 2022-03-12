n,m = map(int,input().split())
hight = list(map(int,input().split()))
a = [[0]*m for _ in range(n)]
for j,h in enumerate(hight):
    for k in range(h):
        i = n-1-k
        a[i][j] = 1
for i in range(n):
    rain = []
    for j in range(m):
        if a[i][j] == 0:
            rain.append((i,j))
        else:
            if len(rain) >= 1:
                x1,y1 = rain[0]
                x2,y2 = rain[-1]
                y1 -= 1
                y2 += 1
                if 0 <= x1 < n and 0 <= y1 < m and \
                    0 <= x2 < n and 0 <= y2 < m and \
                    a[x1][y1] == 1 and a[x2][y2] == 1:
                    for x,y in rain:
                        a[x][y] = 2
            rain = []
ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            ans += 1
print(ans)