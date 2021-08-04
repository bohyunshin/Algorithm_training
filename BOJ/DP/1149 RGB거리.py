n = int(input())
rgb = []
for _ in range(n):
    rgb.append(list(map(int,input().split())))
dp = [[1e100]*3 for _ in range(n)]
dp[0] = rgb[0]
for i in range(1,n):
    color = [0,1,2]
    for j in [0,1,2]:
        color.pop(j)
        for k in color:
            dp[i][j] = min(dp[i][j], rgb[i][j] + dp[i-1][k])
        color.append(j)
        color.sort()
print(min(dp[n-1]))
