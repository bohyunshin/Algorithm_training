n = 1000
dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[0][0] = 1
number = [1,2,3]
for i in range(1,n+1):
    for j in range(len(number)):
        if i-number[j] >= 0:
            for k in range(n):
                dp[i][k+1] += dp[i-number[j]][k]
                dp[i][k + 1] %= 1000000009
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    print(dp[n][m] % 1000000009)