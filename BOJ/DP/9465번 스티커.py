t = int(input())
for _ in range(t):
    n = int(input())
    a = []
    for _ in range(2):
        a.append([0,0] + list(map(int,input().split())))
    dp = [[0]*(n+2) for _ in range(2)]
    dx, dy = [1,1], [-1,-2]
    for y in range(2,n+2):
        for x in range(2):
            if x == 0:
                p = 1
            else:
                p = -1
            for k in range(2):
                nx,ny = x+dx[k]*p, y+dy[k]
                dp[x][y] = max(dp[x][y], dp[nx][ny] + a[x][y])
    print(max(dp[0][n+1],dp[1][n+1]))