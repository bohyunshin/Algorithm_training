a = input()
b = input()
n,m = len(a),len(b)
a = ' ' + a
b = ' ' + b
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = 0
ans = -1
for i in range(1,n+1):
    for j in range(1,m+1):
        ans = max(ans,dp[i][j])
print(ans)