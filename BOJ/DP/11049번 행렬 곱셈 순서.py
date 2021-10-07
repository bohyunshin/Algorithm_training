n = int(input())
A = []
for _ in range(n):
    a,b = map(int,input().split())
    A.append((a,b))
dp = [[1e100]*n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0
for i in range(n-1):
    a,b = A[i]
    b,c = A[i+1]
    dp[i][i+1] = a*b*c
for j in range(2,n+1):
    for i in range(n):
        if i+j >= n:
            continue
        for k in range(i,i+j):
            dp[i][i+j] = min(dp[i][i+j], dp[i][k] + dp[k+1][i+j] + A[i][0]*A[k][1]*A[i+j][1])
print(dp[0][n-1])
# for i in dp:
#     print(i)

"""
3
5 3
3 2
2 6

4
5 3
3 2
2 6
6 7
"""