import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = [[0]*(n+1)]
for _ in range(n):
    a.append([0] + list(map(int,input().split())))
s = [[0]*(n+1) for _ in range(n+1)]
# 가로 누적합.
for i in range(1,n+1):
    for j in range(1,n+1):
        s[i][j] = s[i][j-1] + a[i][j]
# 세로 누적합.
for j in range(1,n+1):
    for i in range(1,n+1):
        s[i][j] = s[i-1][j] + s[i][j]
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    print(s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1])

"""
4 1
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3 3 4 4
"""