n = 100000
dp = [[[0]*4 for _ in range(2)] for _ in range(n+1)]
number = [1,2,3]
# 0: 짝수, 1: 홀수.
dp[0][0][0] = 1
dp[1][1][1] = 1
for i in range(2,n+1):
    for j in range(len(number)):
        if i-number[j] >= 0:
            for k in range(len(number)):
                if number[k] == number[j]:
                    # 홀수에서 짝수로 넘어가는 경우,
                    dp[i][0][0] += dp[i-number[j]][1][number[k]]
                    dp[i][0][0] %= 1000000009
                    # 짝수에서 홀수로 넘어가는 경우,
                    dp[i][1][number[k]] += dp[i - number[j]][0][0]
                    dp[i][1][number[k]] %= 1000000009
t = int(input())
for _ in range(t):
    m = int(input())
    ans = 0
    for i in range(2):
        for j in range(4):
            ans += dp[m][i][j]
    print(ans % 1000000009)