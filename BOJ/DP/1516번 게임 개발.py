n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
dp = [-1]*n
def go(idx):
    global visited
    if dp[idx] != -1:
        for k in a[idx][1:]:
            if k == -1:
                break
            visited[k-1] = True
        return dp[idx]
    order = a[idx]
    time = order[0]
    for k in order[1:]:
        if k == -1:
            break
        if visited[k-1] == False:
            time += go(k-1)
    dp[idx] = time
    return dp[idx]
for i in range(n):
    visited = [False]*n
    go(i)
for i in dp:
    print(i)

"""
5
10 -1
10 5 -1
10 -1
10 -1
1000 -1
"""