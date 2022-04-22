t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    coin = int(input())
    dp = [0]*(coin+1)
    dp[0] = 1
    if 1 in a:
        dp[1] = 1
    for j in range(len(a)):
        for i in range(2,coin+1):
            if i-a[j] >= 0:
                dp[i] += dp[i-a[j]]
    print(dp[coin])