S = input()
n = len(S)
A = 0
B = 0
C = 0
for i in S:
    if i == 'A':
        A += 1
    elif i == 'B':
        B += 1
    elif i == 'C':
        C += 1
dp = [ [ [ [ [-1]*3 for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
ans = ''

def go(a,b,c,p1,p2):
    if a+b+c == n:
        dp[a][b][c][p1][p2] = 1
        return dp[a][b][c][p1][p2]
    if dp[a][b][c][p1][p2] != -1:
        return dp[a][b][c][p1][p2]
    global ans
    temp = ans
    # 오늘 일한 사람이 A인 경우.
    ans = temp + 'A'
    if a < A and go(a+1,b,c,0,p1) == 1:
        dp[a][b][c][p1][p2] = 1
        return dp[a][b][c][p1][p2]
    # 오늘 일한 사람이 B인 경우.
    ans = temp + 'B'
    if b < B and p1 != 1 and go(a,b+1,c,1,p1) == 1:
        dp[a][b][c][p1][p2] = 1
        return dp[a][b][c][p1][p2]
    # 오늘 일한 사람이 C인 경우.
    ans = temp + 'C'
    if c < C and p1 != 2 and p2 != 2 and go(a,b,c+1,2,p1) == 1:
        dp[a][b][c][p1][p2] = 1
        return dp[a][b][c][p1][p2]
    dp[a][b][c][p1][p2] = 0
    return dp[a][b][c][p1][p2]
if go(0,0,0,0,0) == 1:
    print(ans)
else:
    print(-1)