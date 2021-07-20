n = int(input())
A = list(map(int, input().split()))
dp =[[1e100]*n for _ in range(n)]
if n == 1:
    print(0)
    exit()
# dp 초기값 채워넣기
for i in range(1,A[0]+1):
    dp[0][i] = 1
# 시간 복잡도는 O(10^5)
for i in range(1,n): # O(10^3)
    m = 1e100
    for j in range(n):
        if m > dp[j][i]:
            m = dp[j][i]

    for k in range(1,A[i]+1): # O(10^2)
        if i + k < n:
            dp[i][i+k] = min(dp[i][i+k], m + 1)
result = []
for i in range(n):
    result.append(dp[i][n-1])
print(-1 if min(result) == 1e100 else min(result))
