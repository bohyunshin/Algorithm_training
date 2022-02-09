import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
s = [input() for _ in range(n)]
d = [[-1] * m for _ in range(n)]
def go(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return 1
    if d[x][y] != -1:
        return d[x][y]
    d[x][y] = 0
    if s[x][y] == 'R':
        d[x][y] = go(x, y + 1)
    elif s[x][y] == 'L':
        d[x][y] = go(x, y - 1)
    elif s[x][y] == 'U':
        d[x][y] = go(x - 1, y)
    else:
        d[x][y] = go(x + 1, y)

    return d[x][y]


for i in range(n):
    for j in range(m):
        if d[i][j] == -1:
            go(i, j)

ans = 0
for i in range(n):
    for j in range(m):
        if d[i][j] == 1:
            ans += 1

print(ans)