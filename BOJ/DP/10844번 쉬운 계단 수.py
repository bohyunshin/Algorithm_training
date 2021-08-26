# dp[i][j] -> 길이가 i인 계단 수 중에서 j로 끝나는 애들의 개수.
dp = [[0]*10 for _ in range(101)]
# 자리수가 1인 애들 초기값 설정 해줌.
for i in range(1,10):
    dp[1][i] += 1
# dp 값 채우기.
for i in range(2,101):
    for j in range(10):
        if j == 0:
            dp[i][j] += dp[i-1][1]
        elif j == 9:
            dp[i][j] += dp[i-1][8]
        else:
            dp[i][j] += dp[i-1][j-1] + dp[i-1][j+1]
        dp[i][j] %= 1000000000
n = int(input())
print(sum(dp[n]) % 1000000000)
