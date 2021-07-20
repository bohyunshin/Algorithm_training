n = int(input())
m = int(input())
vip = []
for _ in range(m):
    vip.append(int(input()))
# dp[i]: i번째 원소까지 고려했을 때 경우의 수
dp = [0]*(n+1)

if n == 1:
    print(1)
    exit(0)

# 첫 번째 원소는 무조건 1
dp[1] = 1
# 첫 번째 원소가 vip이거나 두 번째 원소가 vip라면 1, 아니면 2
dp[2] = 1 if 2 in vip or 1 in vip else 2

for i in range(3,n+1):
    if i in vip or i-1 in vip:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n])