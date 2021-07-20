n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
dp = [[-1]*m for _ in range(n)]
dp[0][0] = A[0][0]
# dp[i][j]: (1,1)에서 출발해서 dp[i][j]까지 갔을 때 가질 수 있는 사탕의 최대 개수
for i in range(n):
    for j in range(m):
        # 초기값은 이미 설정해줬으니 ㅌㅌ
        if i == 0 and j == 0:
            continue
        # index error 고려
        if i == 0:
            dp[i][j] = dp[i][j-1] + A[i][j]
            continue
        # index error 고려
        if j == 0:
            dp[i][j] = dp[i-1][j] + A[i][j]
            continue
        dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + A[i][j]
print(dp[n-1][m-1])
