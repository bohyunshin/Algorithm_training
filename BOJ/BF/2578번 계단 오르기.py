n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
if n == 1:
    print(a[0])
    exit()
dp = [[-1]*4 for _ in range(n)]
# dp 테이블 초기값 설정.
dp[0][1] = a[0]
dp[1][1] = a[1]
for i in range(n):
    for j in [1,2]:
        if dp[i][j] == -1:
            continue
        if j == 1:
            # 한칸 이동하기.
            if i+1 < n:
                dp[i+1][2] = max(dp[i+1][2], dp[i][j] + a[i+1])
            # 두칸 이동하기.
            if i+2 < n:
                dp[i+2][1] = max(dp[i+2][1], dp[i][j] + a[i+2])
        elif j == 2:
            # 두칸 이동하기.
            if i+2 < n:
                dp[i+2][1] = max(dp[i+2][1], dp[i][j] + a[i+2])
print(max(dp[n-1]))

"""
5
1
2
3
4
5
"""