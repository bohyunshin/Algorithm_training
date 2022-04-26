def go(start,end):
    if dp[start][end] != -1:
        return dp[start][end]
    if start == end:
        return 0
    ans = 1e100
    s = partial_s[end+1] - partial_s[start]
    for i in range(start,end):
        tmp = go(start,i) + go(i+1,end) + s
        if ans > tmp:
            ans = tmp
        dp[start][end] = ans
    return ans

t = int(input())
for _ in range(t):
    k = int(input())
    a = list(map(int, input().split()))
    dp = [[-1] * k for _ in range(k)]
    partial_s = [0]*(k+1)
    for i in range(k):
        partial_s[i+1] = partial_s[i] + a[i]
    print(go(0,k-1))