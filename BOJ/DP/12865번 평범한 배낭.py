n,k = map(int,input().split())
A = []
W = [0]
V = [0]
for _ in range(n):
    w,v = map(int,input().split())
    A.append((w,v))
    W.append(w)
    V.append(v)
dp = [[0]*(k+1) for _ in range(n+1)]
# w,v = A[0]
# dp[0][w] = v
for i in range(1,n+1):
    for j in range(1,k+1):
        dp[i][j] = dp[i-1][j]
        if j-W[i] >= 0:
            dp[i][j] = max(dp[i-1][j-W[i]] + V[i], dp[i][j])
        # else:
        #     dp[i][j] = dp[i-1][j]
print(dp[n][k])
for i in dp:
    print(i)

"""
2 1
2 2 
2 2
"""