n = int(input())
A = list(map(int, input().split()))
dp =[[1e100]*n for _ in range(n)]

# 미로의 크기가 1*1이라면 그냥 그 위치가 도착점임
if n == 1:
    print(0)
    exit()

# dp[i][j]: i -> j로 가는 최소 점프 수
# 따라서 최종 구해야하는 답은 min(dp[i][n-1])임
# 0 ~ n-2 출발점 -> n-1 도착점의 최소 점프의 수

# dp 초기값 채워넣기
for i in range(1,A[0]+1):
    dp[0][i] = 1

# 시간 복잡도는 O(10^5)
for i in range(1,n): # O(10^3)
    m = 1e100
    # dp[i][j]의 의미는 -> j로 가는 최소 점프 수
    # 결국 j까지 가는 최소 점프 수를 구하는 것인데 이를 고려하기 위해
    # 우선 i번째까지 가는 최소 점프 수를 구하고 거기서 j로의 최소 점프 수를 고려

    # 모든 점을 돌면서 i까지 갈 수 있는 최소 점프 수를 구함
    for j in range(n):
        if m > dp[j][i]:
            m = dp[j][i]

    # 현재 i번째 점에 있을 때 뛸수 있는 점프 수는 A[i]임
    # 따라서 for 문을 돌면서 기존의 값 (dp[i][i+k])와
    # 점프를 했을 때의 값 (m+1)을 비교해주면서 업데이트
    for k in range(1,A[i]+1): # O(10^2)
        if i + k < n:
            dp[i][i+k] = min(dp[i][i+k], m + 1)
result = []
for i in range(n):
    result.append(dp[i][n-1])
# min 값이 1e100이면 업데이트가 안됐다는 뜻이고 못간다는 뜻임.
print(-1 if min(result) == 1e100 else min(result))
