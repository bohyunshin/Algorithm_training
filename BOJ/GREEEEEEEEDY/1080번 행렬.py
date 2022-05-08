n,m = map(int,input().split())
a = [list(int(i) for i in input()) for _ in range(n)]
b = [list(int(i) for i in input()) for _ in range(n)]
if n <= 2 or m <= 2:
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                print(-1)
                exit()
    print(0)
else:
    ans = 0
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] == b[i][j]:
                continue
            ans += 1
            for x in range(3):
                for y in range(3):
                    a[i+x][j+y] = abs(a[i+x][j+y]-1)
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                print(-1)
                exit()
    print(ans)

"""
3 3
110
111
111
101
111
111
"""