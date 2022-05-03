n = int(input())
a = [0] + list(map(int,input().split()))
b = [0] + list(map(int,input().split()))
dp = [[0]*101 for _ in range(n+1)]
ans = -1
for i in range(1,n+1):
    for j in range(100,0,-1):
        if j <= a[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-a[i]] + b[i], dp[i-1][j])
        ans = max(ans,dp[i][j])
print(ans)