n = int(input())
A = list(map(int, input().split()))
A = [0] + A
dp = [0]*(n+1)
dp[1] = A[1]
dp[2] = min(A[1]*2, A[2])
for i in range(3,n+1):
    tmp = []
    for j in range(i):
        tmp.append(dp[j]+A[i-j])
    dp[i] = min(tmp)
print(dp[n])