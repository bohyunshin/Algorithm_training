n = 5
m = 7
a = []
for _ in range(n):
    a.append(input())
def check(num):
    global available
    r = num // 5
    c = num % 5
    for d in range(4):
        nr = r + dx[d]
        nc = c + dy[d]
        if not (0 <= nr < 5 and 0 <= nc < 5) or visited[nr][nc]:
            continue
        nextNum = nr*5+nc   # 다음 숫자
        if nextNum in chosen:    # p에 있다면 방문표시, 재귀로 다음 숫자 넘겨 재검사
            visited[nr][nc] = True
            available += 1
            check(nextNum)
def go(i,index,ycnt):
    global available, visited, ans
    # if ycnt >= 4 or i >= n**2하면,
    # index == m이면서 i == n**2인 경우가 빠져서, 틀린답이 나온다.
    if ycnt >= 4:
        return
    if index == m:
        available = 1
        visited = [[False]*n for _ in range(n)]
        sx,sy = chosen[0] // n, chosen[0] % n
        visited[sx][sy] = True
        check(chosen[0])
        if available == m:
            ans += 1
        return
    if i >= n**2:
        return
    x, y = i // n, i % n
    # i 선택하는 경우.
    chosen[index] = i
    if a[x][y] == 'S':
        go(i + 1, index + 1, ycnt)
    else:
        go(i + 1, index + 1, ycnt + 1)
    # i 선택하지 않는 경우.
    chosen[index] = -1
    go(i + 1, index, ycnt)
chosen = [-1]*m
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
go(0,0,0)
print(ans)

"""
YYYYY
SSSSY
YYYYY
YYYYY
YYYYY

YYYYY
SYYYY
YYYYY
YYYYY
YYYYY
"""