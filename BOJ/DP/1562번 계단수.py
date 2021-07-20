import sys

mod = 1000000000

# 자릿수 입력
n = int(sys.stdin.readline())

# dp : 비트 정보, 자릿수, 끝나는 수에 대해 가능한 경우의 수를 담는 3차원 배열
dp = [[[-1] * 11 for _ in range(101)] for _ in range(1 << 11)]

# go : d[f][b][x]를 리턴하는 함수
def go(f, b, x):
    # 끝나는 수가 범위가 넘어가는 경우는 없으므로 0 리턴
    if x < 0 or x > 9:
        return 0
    # 다 뽑았으면
    if b == n:
        # 모든 수를 다 뽑으면 유효한 경우이므로 1 리턴
        if f == (1 << 10) - 1:
            return 1
        # 모든 수를 다 뽑지 않으면 유효하지 않은 경우이므로 0 리턴
        else:
            return 0
    # Memoization
    if dp[f][b][x] != -1:
        return dp[f][b][x]
    dp[f][b][x] = 0
    # 끝나는 수가 0이면 그 뒤에 1만 올 수 있으므로
    if x == 0:
        dp[f][b][x] += go(f | (1 << (x + 1)), b + 1, (x + 1))
        dp[f][b][x] %= mod
    # 끝나는 수가 9면 그 뒤에 8만 올 수 있으므로
    elif x == 9:
        dp[f][b][x] += go(f | (1 << (x - 1)), b + 1, (x - 1))
        dp[f][b][x] %= mod
    # 둘다 아니면 +1, -1만 올 수 있으므로
    else:
        dp[f][b][x] += go(f | (1 << (x + 1)), b + 1, (x + 1))
        dp[f][b][x] %= mod
        dp[f][b][x] += go(f | (1 << (x - 1)), b + 1, (x - 1))
        dp[f][b][x] %= mod

    return dp[f][b][x]

ans = 0

# 각 숫자로 끝나는 모든 경우를 조사해야하므로 각 자리마다 go함수 호출
for i in range(1, 10):
    ans += go(1 << i, 1, i)
    ans %= mod

# 정답 출력
print(ans)