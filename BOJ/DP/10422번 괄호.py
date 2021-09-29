L = 5000
dp = [-1]*(L+1)
def go(n):
    if n == 0:
        return 1
    if dp[n] >= 0:
        return dp[n]
    dp[n] = 0
    for i in range(2,n+1,2):
        dp[n] += go(i-2) * go(n-i)
        dp[n] %= 1000000007
    return dp[n]
T = int(input())
for _ in range(T):
    n = int(input())
    if n % 2 == 0:
        print(go(n))
    else:
        print(0)
