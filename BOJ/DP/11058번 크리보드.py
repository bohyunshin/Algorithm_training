n = int(input())
dp = [0]*(n+1)
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    j = 3
    while i-j >= 1:
        dp[i] = max(dp[i],dp[i-j]*(j-1))
        j += 1
print(dp[n])