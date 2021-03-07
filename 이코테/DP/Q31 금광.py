T = int(input())
answer = []
for _ in range(T):
    n,m = map(int, input().split())
    array = list(map(int, input().split()))
    cave = []
    for i in range(0,len(array),m):
        cave.append(array[i:i+m])

    # dp = [[0]*m for _ in range(n)]
    # for i in range(n):
    #     dp[i][0] = cave[i][0]
    dp = []
    for i in range(0, len(array), m):
        dp.append(array[i:i + m])


    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    answer.append(result)

print(answer)




"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""