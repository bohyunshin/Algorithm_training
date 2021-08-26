n = int(input())
A = list( map(int, input().split()) )
dp = [1]*(n)
v = [-1]*n

for i in range(n):
    for j in range(i):
        if A[j] < A[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
            v[i] = j
index = dp.index(max(dp))
ans = []
while index != -1:
    ans.append(A[index])
    index = v[index]
print(max(dp))
print(' '.join(list(map(str, ans[::-1]))))
