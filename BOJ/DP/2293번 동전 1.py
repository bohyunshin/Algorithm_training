n,k = map(int,input().split())
number = []
for _ in range(n):
    a = int(input())
    number.append(a)
dp = [0]*(k+1)
dp[0] = 1
for j in range(len(number)):
    for i in range(1,k+1):
        if i-number[j] >= 0:
            dp[i] += dp[i-number[j]]
print(dp[k])