n = int(input())
a, b = map(int, input().split())
m = int(input())
order = []
for _ in range(m):
    order.append(int(input()))
order = [0] + order
# dp[i][j][k]: i번째 order에서 열려있는 문의 위치가 (j,k)일 때 움직인 문의 수
dp = [[[-1]*(n+1) for _ in range(n+1)] for _ in range(m+1)]
dp[0][a][b] = 0


for orderIdx in range(1,m+1):
    for open1 in range(1,n+1):
        for open2 in range(1,n+1):
            # 이전 order가 방문이 되었다면
            if dp[ orderIdx-1 ][open1][open2] != -1:
                # 첫 번째 문(open1)을 order[orderIdx]으로 움직이고자 하는데,
                # 움직였을 때 처음 방문된 곳이라면 비교 안하고 바로 업데이트 함
                if dp[ orderIdx ][ order[orderIdx] ][open2] == -1:
                    dp[orderIdx][order[orderIdx]][open2] = dp[orderIdx - 1][open1][open2] + abs(order[orderIdx] - open1)
                # 방문한 적이 있다면 이전의 값과 비교해서 min인 애를 때려 넣음
                else:
                    dp[orderIdx][order[orderIdx]][open2] = min(dp[orderIdx][order[orderIdx]][open2], dp[orderIdx - 1][open1][open2] + abs(order[orderIdx] - open1))
                if dp[ orderIdx ][open1][ order[orderIdx] ] == -1:
                    dp[orderIdx][open1][order[orderIdx]] = dp[orderIdx - 1][open1][open2] + abs(order[orderIdx] - open2)
                else:
                    dp[orderIdx][open1][order[orderIdx]] = min(dp[orderIdx][open1][order[orderIdx]], dp[orderIdx - 1][open1][open2] + abs(order[orderIdx] - open2))

answer = 999999
for open1 in range(1,n+1):
    for open2 in range(1,n+1):
        if dp[m][open1][open2] != -1 and answer > dp[m][open1][open2]:
            answer = dp[m][open1][open2]
print(answer)