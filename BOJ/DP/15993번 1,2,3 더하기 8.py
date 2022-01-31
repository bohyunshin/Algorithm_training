n = 100000
# 0은 홀수, 1은 짝수.
dp = [[0]*2 for _ in range(n+1)]
dp[0][1] = 1
number = [1,2,3]
for i in range(1,n+1):
    for j in range(len(number)):
        if i-number[j] >= 0:
            for k in [0,1]:
                dp[i][1-k] += dp[i-number[j]][k]
                dp[i][1-k] %= 1000000009
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])