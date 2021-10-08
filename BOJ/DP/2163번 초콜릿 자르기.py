n,m = map(int,input().split())
dp = [[1e100]*(m+1) for _ in range(n+1)]
# dp[i][j]: 크기가 i*j인 초콜릿을 1*1로 쪼개기 위한 최소 쪼개기 횟수.
# 가로를 쪼개는 경우와 세로를 쪼개는 경우로 나눔.
def go(i,j):
    if i == 1 and j == 1:
        return 0
    if dp[i][j] != 1e100:
        return dp[i][j]
    # dp[i][j] = cnt
    if j >= 2:
        for k in range(1,j):
            dp[i][j] = min(dp[i][j],go(i,k) + go(i,j-k) + 1)
    if i >= 2:
        for k in range(1,i):
            dp[i][j] = min(dp[i][j],go(k,j) + go(i-k,j) + 1)
    return dp[i][j]
go(n,m)
print(dp[n][m])