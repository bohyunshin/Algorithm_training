m = 1000000
dp = [0]*(m+1)
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,m+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

n = int(input())
for _ in range(n):
    a = int(input())
    print(dp[a])