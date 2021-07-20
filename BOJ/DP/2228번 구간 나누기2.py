n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(input()))
A = [1e100] + A

# dp[n][m]: n번째까지의 수를 이용해 m개의 구간을 만들 때 그 합의 최대값
dp = [[-1]*(m+1) for _ in range(n+1)]

def solve(n,m):
    # print(n,m)
    if m == 0:
        return 0
    if n < 0:
        return -1e100
    if dp[n][m] != -1:
        return dp[n][m]

    # n번째 수를 포함하지 않을 때, dp[n-1][m]와 같음.
    dp[n][m] = solve(n-1,m)

    for i in range(n,0,-1):
        temp = solve(i-2,m-1) + sum(A[1:n+1]) - sum(A[1:i])
        if temp > dp[n][m]:
            dp[n][m] = temp
    return dp[n][m]

print(solve(n,m))