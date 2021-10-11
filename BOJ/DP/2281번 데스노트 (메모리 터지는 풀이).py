n,m = map(int,input().split())
people = []
for _ in range(n):
    people.append(int(input()))
dp = [[[1e100]*(m+1) for _ in range(n+1)] for _ in range(n+1)]
# dp[i][j][k]: i번째 줄에 j번째 사람까지 썼고 i번째 줄에서 현재 위치가 k일때, 그 이전까지 사용한 마지막 총 칸 수.
dp[0][0][people[0]] = (m-people[0])**2
for i in range(n):
    for j in range(n-1):
        for k in range(m+1):
            # if i == 1:
            #     print(i)
            # if i == 0 and j == 2:
            #     print(i,j)
            if dp[i][j][k] != 1e100:
                # i번째 줄에 j번째 사람을 이미 적은 경우,
                # j+1번째 사람을 쓰고자 할 때, 다음 사람을 쓰기 위해 한 칸을 띄고,
                # j+1번째 사람까지 쓰고 난 뒤에 칸 수가 m보다 작다면,
                if k + 1 + people[j+1] <= m:
                    # i번째 줄에 j+1번째 사람을 쓰거나,
                    if dp[i][j+1][k+1+people[j+1]] > dp[i][j][k] - (m-k)**2 + (m - (k+1+people[j+1]))**2:
                        dp[i][j+1][k+1+people[j+1]] = dp[i][j][k] - (m-k)**2 + (m - (k+1+people[j+1]))**2
                    # i번째 줄에 j+1번째 사람을 쓰지 않고 i+1번째 줄에 쓰거나,
                    if dp[i+1][j+1][people[j+1]] > dp[i][j][k] + (m - people[j+1])**2:
                        dp[i+1][j+1][people[j+1]] = dp[i][j][k] + (m - people[j+1])**2
                # 크다면, 무조건 다음 줄에 써야 함.
                else:
                    # i번째 줄에 j+1번째 사람을 쓰지 않고 i+1번째 줄에 써야함.
                    if dp[i+1][j+1][people[j+1]] > dp[i][j][k] + (m - people[j+1])**2:
                        dp[i+1][j+1][people[j+1]] = dp[i][j][k] + (m - people[j+1])**2
ans = 1e100
where = 0
for i in range(n):
    for k in range(m+1):
        tmp = dp[i][n-1][k] - (m-k)**2
        if tmp < ans:
            ans = tmp
print(ans)

"""
3 10
5
4
1
"""