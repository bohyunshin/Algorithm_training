n = int(input())
nums = list(map(int,input().split()))
a,nums =  nums[-1],nums[:-1]
n = len(nums)
dp = [[0]*(20+1) for _ in range(n+1)]
dp[1][nums[0]] = 1
for i in range(1,n+1):
    b = nums[i-1]
    for j in range(20+1):
        if j-b >= 0:
            dp[i][j] += dp[i-1][j-b]
        if j+b <= 20:
            dp[i][j] += dp[i-1][j+b]
print(dp[n][a])
# for i in dp:
#     print(i)