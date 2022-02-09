from itertools import permutations
from copy import deepcopy
n,m,k = map(int,input().split())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
combis = []
for _ in range(k):
    r,c,s = map(int,input().split())
    r -= 1
    c -= 1
    combis.append((r,c,s))
def rotate(r,c,s,a):
    l = s*2
    d = 0
    cnt = 0
    x,y = r-s,c-s
    visited = [[False]*m for _ in range(n)]
    before = a[x][y]
    while not (x == r and y == c):
        # print(x,y)
        if cnt == l:
            d = (d+1)%4
            cnt = 0
            continue
        if visited[x][y]:
            x += 1
            y += 1
            if x == r and y == c:
                break
            d = 0
            after = a[x][y]
            a[x][y] = before
            before = after
            l -= 2
            cnt = 0
            continue
        visited[x][y] = True
        cnt += 1
        x += dx[d]
        y += dy[d]
        after = a[x][y]
        a[x][y] = before
        before = after
    return a
def value(a):
    ans = -1
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[i][j]
        if ans == -1 or ans > tmp:
            ans = tmp
    return ans
ans = -1
for p in permutations(range(k)):
    a_copy = deepcopy(a)
    for index in p:
        r,c,s = combis[index]
        a_copy = rotate(r,c,s,a_copy)
    tmp = value(a_copy)
    if ans == -1 or ans > tmp:
        ans = tmp
print(ans)