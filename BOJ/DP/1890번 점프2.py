n = int(input())
array = []
for _ in range(n):
    array.append( list(map(int, input().split())) )
# d[i][j]: (i,j)까지 가는 경우의 수
d = [[0]*n for _ in range(n)]
# d[0][0]: (0,0)까지 가는 경우의 수는 1이므로 1로 초기화
d[0][0] = 1

# bottom-up DP 방식
for x in range(n):
    for y in range(n):
        if x == n-1 and y == n-1:
            break
        if d[x][y] >= 1:
            # 아래쪽 좌표
            dx = x + array[x][y]
            # 오른쪽 좌표
            dy = y + array[x][y]
            # 이동 좌표가 범위 내에 있다면
            if 0 <= dy < n:
                d[x][dy] += d[x][y]
            # 이동 좌표가 범위 내에 있다면
            if 0 <= dx < n:
                d[dx][y] += d[x][y]
print(d[n-1][n-1])