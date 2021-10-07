import sys
sys.setrecursionlimit(1000000)
n = int(input())
a = list(map(int,input().split()))
d = [[-1]*n for _ in range(n)]
def go(i, j):
    if i >= j:
        return 0
    if d[i][j] != -1:
        return d[i][j]
    if a[i] == a[j]:
        d[i][j] = go(i+1, j-1)
    else:
        d[i][j] = min(go(i+1, j), go(i, j-1)) + 1
    return d[i][j]
print(go(0, n-1))