n = int(input())
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 1
number = []
k = 0
while 2**k <= n:
    number.append(2**k)
    k += 1
for j in range(len(number)):
    for i in range(2,n+1):
        if i-number[j] >= 0:
            dp[i] += dp[i-number[j]]
            dp[i] %= 1000000000
print(dp[n])