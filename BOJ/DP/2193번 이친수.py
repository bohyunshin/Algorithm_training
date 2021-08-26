# 10844번 쉬운 계단 수와 유사하게 풀어보자.
# dp[i][j] -> i자리 이친수 중에서 j로 끝나는 애들의 개수.
dp = [[0]*2 for _ in range(91)]
# dp 초기값 설정해주기.
dp[1][1] = 1
dp[2][0] = 1
for i in range(3,91):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
n = int(input())
print(sum(dp[n]))