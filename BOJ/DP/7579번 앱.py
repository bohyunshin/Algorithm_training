n,m = map(int,input().split())
a = [0] + list(map(int,input().split()))
c = [0] + list(map(int,input().split()))
cost_total = sum(c)
dp = [[0]*(cost_total+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,cost_total+1):
        dp[i][j] = dp[i-1][j]
        if j-c[i] >= 0:
            dp[i][j] = max(dp[i-1][j-c[i]] + a[i], dp[i][j])
for j in range(1,cost_total+1):
    for i in range(1,n+1):
        if dp[i][j] >= m:
            print(j)
            exit()