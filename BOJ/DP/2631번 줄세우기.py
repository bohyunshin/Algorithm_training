n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))
dp = [1]*n

# n에서 LIS 빼면 됨.
for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))