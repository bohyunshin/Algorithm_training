t = int(input())

def go(i,j):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    answer = dp[i][j]
    cost = sum(A[i:j+1])
    for k in range(i,j):
        temp = go(i,k) + go(k+1,j) + cost
        if answer == -1 or answer > temp:
            answer = temp
    dp[i][j] = answer
    return answer

for _ in range(t):
    k = int(input())
    A = list(map(int, input().split()))

    dp = [[-1]*k for _ in range(k)]

    print(go(0,k-1))