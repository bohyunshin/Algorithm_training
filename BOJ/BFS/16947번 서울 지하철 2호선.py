import sys

sys.setrecursionlimit(1000000)
from collections import deque

n = int(input())
a = [[] for _ in range(n)]
for _ in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)
# 0이면 방문 안함.
# 1이면 방문 했는데 사이클은 아님
# 2이면 방문하고 사이클인 애
check = [0] * n


def go(x, p):
    # -2: 사이클 찾았지만 사이클에 포함은 안되는 애.
    # -1: 사이클 못찾음.
    # 0~n-1: 사이클 찾았고 사이클에 포함되는 애.

    # 만약 이미 방문했는데 또 방문했다면 사이클인 것임.
    # 다만 바로 이전에 방문한 점일 수가 있는데
    # 이는 아래 continue에서 제외됨.
    if check[x] == 1:
        return x
    # 방문 안했다면 방문처리 해주고
    check[x] = 1
    for y in a[x]:
        # 이동할 점이 바로 이전에 이동한 점이라면 패스.
        if y == p:
            continue
        res = go(y, x)
        # 사이클 찾았지만 사이클에 포함은 안되는 경우.
        if res == -2:
            return -2
        # 사이클 찾았고 사이클에 포함되는 경우임.
        if res >= 0:
            check[x] = 2
            # 시작점과 동일하다면 사이클이 끝난 것임.
            if x == res:
                return -2
            # 찾을 때까지 계속함.
            else:
                return res
    return -1


go(0, -1)

q = deque()
dist = [-1] * n

for i in range(n):
    if check[i] == 2:
        dist[i] = 0
        q.append(i)
    else:
        dist[i] = -1

while q:
    x = q.popleft()
    for y in a[x]:
        if dist[y] == -1:
            q.append(y)
            dist[y] = dist[x] + 1

print(*dist, sep=' ')