m = 100000
dp = [0]*(m+1)
# dp[0] 하는 이유는?
# -> 0 + 2 할때 dp[0] 원소를 넣어주므로 1을 미리 넣어줘야함.
dp[0] = 1
dp[1] = 1
number = [1,2,3]
for j in range(len(number)):
    for i in range(2,m+1):
        if i-number[j] >= 0:
            dp[i] += dp[i-number[j]]
n = int(input())
for _ in range(n):
    a = int(input())
    print(dp[a])