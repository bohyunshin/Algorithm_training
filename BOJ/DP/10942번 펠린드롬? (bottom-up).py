import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
# dp[i][j]: A[i] ~ A[j]가 펠린드롬이면 1, 아니면 0
dp = [[0]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 1
    if i < n-1:
        if A[i] == A[i+1]:
            dp[i][i+1] = 1
# 점화식은
# dp[i][j] = dp[i+1][j-1] & A[i] == A[j]
# -> A[i]~A[j]가 펠린인지 결정짓기 위해서
# A[i+1]~A[j-1]가 펠린인지 여부와 A[i] == A[j]인지 살펴본다.
# bottom-up 방식.
# 아래처럼 하면 dp 테이블 채워지는 방식이
# (0,2), (1,3), (2,4)...
# (0,3), (1,4), (2,5)...
# (0,4), (1,5), (2,6)...
for k in range(3, n+1):
    for i in range(0, n-k+1):
        j = i+k-1
        if dp[i+1][j-1] == 1 and A[i] == A[j]:
            dp[i][j] = 1
m = int(sys.stdin.readline())
answer = ''
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    answer += str(dp[a-1][b-1]) + '\n'
print(answer)