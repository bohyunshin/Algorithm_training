S,A,B,C = map(int,input().split())
dp = [ [ [ [0]*(C+1) for _ in range(B+1)] for _ in range(A+1)] for _ in range(S+1)]
# def go(index,a,b,c):
#     if index == S:
#         return 0
#     if dp[index][a][b][c] != -1:
#         return dp[index][a][b][c]
# dp[i][a][b][b]: 곡의 수 i개, 세 사람이 부른 곡의 수가 a,b,c개일 때, 경우의 수.
for i in range(2):
    for j in range(2):
        for k in range(2):
            if i+j+k == 0:
                continue
            dp[1][i][j][k] += 1
for i in range(S):
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                # print(dp[i][a][b][c])
                if dp[i][a][b][c] == 0:
                    continue
                for j in range(2):
                    for k in range(2):
                        for l in range(2):
                            if j+k+l == 0:
                                continue
                            if a+j <= A and b+k <= B and c+l <= C:
                                dp[i+1][a+j][b+k][c+l] += dp[i][a][b][c]
                                dp[i+1][a+j][b+k][c+l] %= 1000000007
print(dp[S][A][B][C])
