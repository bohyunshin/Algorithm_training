m = 1000000
# dp[i][j] -> i번째 수를 구성하는 애들 중에서
# j로 끝나는 애들의 개수.
dp = [[0]*4 for _ in range(m+1)]
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1
# 1000000009
for i in range(4,m+1):
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % 1000000009
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % 1000000009
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % 1000000009

n = int(input())
for _ in range(n):
    a = int(input())
    print(sum(dp[a]) % 1000000009)