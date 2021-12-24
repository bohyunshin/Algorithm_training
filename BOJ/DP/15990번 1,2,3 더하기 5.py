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

# m = 100000
# numbers = [1,2,3]
# dp = [[0]*4 for _ in range(m+1)]
# for j in numbers:
#     dp[j][j] = 1
# for i in range(1,m+1):
#     for j in range(1,4):
#         if i-j >= 0:
#             if j == 1:
#                 dp[i][j] += dp[i-j][2] + dp[i-j][3]
#             if j == 2:
#                 dp[i][j] += dp[i-j][1] + dp[i-j][3]
#             if j == 3:
#                 dp[i][j] += dp[i-j][1] + dp[i-j][2]
#         dp[i][j] %= 1000000009
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     print(sum(dp[n]) % 1000000009)
