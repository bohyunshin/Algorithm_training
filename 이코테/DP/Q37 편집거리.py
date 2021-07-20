a = input()
b = input()
dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]

# dp 테이블 첫째행 채우기
dp[0] = [i for i in range(len(a)+1)]
# dp 테이블 첫째열 채우기
for i in range(len(b)+1):
    dp[i][0] = i

for j in range(1,len(a)+1):
    for i in range(1,len(b)+1):
        a_s = a[j-1]
        b_s = b[i-1]
        if a_s == b_s:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1+min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
print(dp)