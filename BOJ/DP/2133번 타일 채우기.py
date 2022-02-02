n = int(input())
if n == 1:
    print(0)
    exit()
dp = [0]*(n+1)
dp[0] = 1
dp[2] = 3
for i in range(3,n+1):
    dp[i] = dp[i-2]*3
    k = 4
    while i-k >= 0:
        dp[i] += dp[i-k]*2
        k += 2
print(dp[n])