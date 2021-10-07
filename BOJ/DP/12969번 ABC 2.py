n,k = map(int,input().split())
MAX_k = int(n*(n-1)/2)
dp = [ [ [ [0]*(MAX_k+1) for _ in range(n+1) ] for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0][0] = 1
for i in range(n):
    for a in range(n):
        for b in range(n):
            for p in range(MAX_k+1):
                if dp[i][a][b][p] == 1:
                    # 'A' 추가한 경우.
                    dp[i+1][a+1][b][p] = 1
                    # 'B' 추가한 경우.
                    dp[i+1][a][b+1][p+a] = 1
                    # 'C' 추가한 경우.
                    dp[i+1][a][b][p+a+b] = 1
FLAG = False
for a in range(n+1):
    for b in range(n+1):
        if dp[n][a][b][k] == 1:
            FLAG = True
            break
    if FLAG:
        break
c = n-a-b
if FLAG == False:
    print(-1)
else:
    print('A'*a + 'B'*b + 'C'*c)