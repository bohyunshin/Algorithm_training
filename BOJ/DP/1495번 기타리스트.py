n,s,m = map(int,input().split())
A = [0] + list(map(int,input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1
# for i in range(n):
#     for j in range(m+1):
#         if dp[i][j] == 0:
#             continue
#         if j-A[i+1] >= 0:
#             dp[i+1][j-A[i+1]] = 1
#         if j+A[i+1] <= m:
#             dp[i+1][j+A[i+1]] = 1
for i in range(1,n+1):
    for j in range(m+1):
        if j-A[i] >= 0 and dp[i-1][j-A[i]] == 1:
            dp[i][j] = 1
        if j+A[i] <= m and dp[i-1][j+A[i]] == 1:
            dp[i][j] = 1
ans = -1
for j in range(m+1):
    if dp[n][j] == 1:
        ans = j
print(ans)