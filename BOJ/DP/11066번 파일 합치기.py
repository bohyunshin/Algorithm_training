t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    dp = [[0]*n for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = a[i] + a[i+1]
        for j in range(i+2,n):
            dp[i][j] = dp[i][j-1] + a[j]
    for d in range(2,n):
        for i in range(n-d):
            j = i+d
            tmp = 1e100
            for k in range(i,j):
                tmp = min(dp[i][k] + dp[k+1][j], tmp)
            dp[i][j] += tmp
    print(dp[0][n-1])