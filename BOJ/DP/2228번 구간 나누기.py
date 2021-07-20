n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(input()))

dp = [[-1e100]*(n+1) for _ in range(m+1)]

# print(len(dp))
# print(len(dp[0]))

for i in range(1,n+1):
    # print(i)
    dp[1][i] = max(A[:i])
print(dp[1])
print()

if n == 2 and m == 2:
    print(sum(A))
    exit(0)
elif n == 3 and m == 2:
    print(A[0] + A[2])
    exit(0)

for i in range(2,n+1):
    for j in range(2,m+1):
        for k in range(2,n-2 + 1):
            if k == 2:
                dp[j][i] = max(dp[j][i], dp[j-1][1] + sum(A[2:i-1]))
            else:
                dp[j][i] = max(dp[j][i], dp[j-1][k-2] + sum(A[k:i]))
    print(dp[j])
    print()
print(dp[m][n])

"""
3 2
-100
-1
1
"""