n = int(input())
A = [0] + list(map(int,input().split()))
m = int(input())
dp = [[0]*(3+1) for _ in range(n+1)]
for j in range(1,4):
    for i in range(1,n+1):
        dp[i][j] = dp[i-1][j]
        if i-m < 0:
            continue
        dp[i][j] = max(dp[i][j], dp[i-m][j-1] + sum(A[i-m+1:i+1]))
print(dp[n][3])
