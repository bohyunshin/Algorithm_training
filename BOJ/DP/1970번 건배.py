import sys
sys.setrecursionlimit(10**6)
n = int(input())
brand = list(map(int,input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]
for step in range(1,n):
    for i in range(n-step):
        cur = dp[i+1][i+step]
        for k in range(i+1,i+step+1):
            tmp = 0
            if brand[i] == brand[k]:
                # print(i + 1, k - 1, k + 1, i + step)
                tmp = dp[i+1][k-1] + dp[k+1][i+step] + 1

            if cur < tmp:
                cur = tmp
        dp[i][i+step] = cur
print(dp[0][n-1])


# def go(i,j):
#     if i >= j:
#         return 0
#     ans = dp[i][j]
#     if ans != -1:
#         return ans
#     ans = go(i+1,j)
#     for k in range(i+1,j+1):
#         cur = 0
#         if brand[i] == brand[k]:
#             cur = go(i+1,k-1) + go(k+1,j) + 1
#         if ans < cur:
#             ans = cur
#     dp[i][j] = ans
#     return ans
# print(go(0,n-1))