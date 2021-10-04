a = input()
b = input()
n,m = len(a), len(b)
a = ' ' + a
b = ' ' + b
dp = [ [[] for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + [a[i]]
        else:
            if len(dp[i][j-1]) > len(dp[i-1][j]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
print(len(dp[n][m]))
print(''.join(dp[n][m]))
