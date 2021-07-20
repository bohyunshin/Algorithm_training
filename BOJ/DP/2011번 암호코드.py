s = [int(i) for i in input()]
n = len(s)
dp = [0]*(n+1)
if s[0] == 0:
    print(0)
else:
    s = [0] + s
    # dp[0]도 1로 초기화해주는 이유?
    # -> 10 <= s[1:2] <= 26일때 dp[0]의 원소를 더해줘야해서 1로 초기화해야함
    dp[0] = dp[1] = 1
    for i in range(2,n+1):
        # 현재 원소가 0이라면 대응되는 알파벳이 없음
        if s[i] > 0:
            dp[i] += dp[i-1]
        # 1에서 9까지는 이미 위에서 더했기 때문에 범위를 10이상 26이하로 잡아야 함
        if 10 <= s[i-1]*10 + s[i] <= 26:
            dp[i] += dp[i-2]
    print(dp[n] % 1000000)
