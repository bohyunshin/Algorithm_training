m = 100000
numbers = [1,2,3]
dp = [[0]*4 for _ in range(m+1)]
for j in numbers:
    dp[j][j] = 1
for i in range(1,m+1):
    for j in range(1,4):
        if i-j >= 0:
            if j == 1:
                dp[i][j] += dp[i-j][2] + dp[i-j][3]
            if j == 2:
                dp[i][j] += dp[i-j][1] + dp[i-j][3]
            if j == 3:
                dp[i][j] += dp[i-j][1] + dp[i-j][2]
        dp[i][j] %= 1000000009

t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % 1000000009)
