from bisect import bisect_left
n = int(input())
A = list( map(int, input().split()) )
dp = []

for i in A:
	index = bisect_left(dp, i)
	if len(dp) == index:
		dp.append(i)
	else:
		dp[index] = i
print(len(dp))