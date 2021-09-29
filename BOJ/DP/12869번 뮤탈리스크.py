n = int(input())
scv = list(map(int,input().split()))
if n == 1:
    dp = [1e100]*(scv[0]+1)
    dp[scv[0]] = 0
    for i in range(scv[0],-1,-1):
        if dp[i] != 1e100:
            if i-9 > 0:
                dp[i-9] = min(dp[i-9],dp[i]+1)
            else:
                dp[0] = min(dp[0], dp[i]+1)
            if i-3 > 0:
                dp[i-3] = min(dp[i-3],dp[i]+1)
            else:
                dp[0] = min(dp[0], dp[i]+1)
            if i-1 > 0:
                dp[i-1] = min(dp[i-1],dp[i]+1)
            else:
                dp[0] = min(dp[0],dp[i]+1)
    print(dp[0])
elif n == 2:
    dp = [[1e100]*(scv[1]+1) for _ in range(scv[0]+1)]
    dp[scv[0]][scv[1]] = 0
    for i in range(scv[0],-1,-1):
        for j in range(scv[1],-1,-1):
            if dp[i][j] != 1e100:
                # (9,3)
                a = i-9 if i-9 > 0 else 0
                b = j-3 if j-3 > 0 else 0
                dp[a][b] = min(dp[a][b],dp[i][j]+1)

                # (3,9)
                a = i-3 if i-3 > 0 else 0
                b = j-9 if j-9 > 0 else 0
                dp[a][b] = min(dp[a][b],dp[i][j]+1)

    print(dp[0][0])
elif n == 3:
    dp = [[[1e100] * (scv[2]+1) for _ in range(scv[1]+1)] for _ in range(scv[0]+1)]
    dp[scv[0]][scv[1]][scv[2]] = 0
    for i in range(scv[0],-1,-1):
        for j in range(scv[1],-1,-1):
            for k in range(scv[2],-1,-1):
                if dp[i][j][k] != 1e100:
                    # (9,3,1)
                    a = i-9 if i-9 > 0 else 0
                    b = j-3 if j-3 > 0 else 0
                    c = k-1 if k-1 > 0 else 0
                    dp[a][b][c] = min(dp[a][b][c],dp[i][j][k]+1)

                    # (9,1,3)
                    a = i-9 if i-9 > 0 else 0
                    b = j-1 if j-1 > 0 else 0
                    c = k-3 if k-3 > 0 else 0
                    dp[a][b][c] = min(dp[a][b][c],dp[i][j][k]+1)

                    # (3,9,1)
                    a = i-3 if i-3 > 0 else 0
                    b = j-9 if j-9 > 0 else 0
                    c = k-1 if k-1 > 0 else 0
                    dp[a][b][c] = min(dp[a][b][c],dp[i][j][k]+1)

                    # (3,1,9)
                    a = i-3 if i-3 > 0 else 0
                    b = j-1 if j-1 > 0 else 0
                    c = k-9 if k-9 > 0 else 0
                    dp[a][b][c] = min(dp[a][b][c],dp[i][j][k]+1)

                    # (1,9,3)
                    a = i-1 if i-1 > 0 else 0
                    b = j-9 if j-9 > 0 else 0
                    c = k-3 if k-3 > 0 else 0
                    dp[a][b][c] = min(dp[a][b][c],dp[i][j][k]+1)

                    # (1,3,9)
                    a = i-1 if i-1 > 0 else 0
                    b = j-3 if j-3 > 0 else 0
                    c = k-9 if k-9 > 0 else 0
                    dp[a][b][c] = min(dp[a][b][c],dp[i][j][k]+1)
    print(dp[0][0][0])