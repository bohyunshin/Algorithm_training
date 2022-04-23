n = int(input())
A = list( map(int, input().split()) )
dp = [1]*n
s = A.copy()

for i in range(n):
	for j in range(i):
		if A[i] > A[j]:
			dp[i] = max( dp[i], dp[j]+1 )
			s[i] = max( s[i], s[j]+A[i])
print(max(s))