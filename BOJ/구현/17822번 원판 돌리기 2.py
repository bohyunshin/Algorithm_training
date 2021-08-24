from collections import defaultdict
n,m,t = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(t):
    x,d,k = map(int, input().split())

    for i in range(n):
        if (i+1) % x == 0:
            row = A[i]
            if d == 0:
                A[i] = row[-k:] + row[:-k]
            if d == 1:
                A[i] = row[k:] + row[:k]
    # for i in A:
    #     print(i)
    # print()

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    FLAG = False
    dct = defaultdict(list)
    d = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                continue
            if A[i][j] == A[i][(j + 1) % m]:
                d[i][j] = d[i][(j + 1) % m] = True
            if i + 1 <= n-1 and A[i][j] == A[i + 1][j]:
                d[i][j] = d[i + 1][j] = True
    for i in range(n):
        for j in range(m):
            if d[i][j]:
                FLAG = True
                A[i][j] = 0

    if FLAG is False:
        total = 0
        cnt = 0
        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    total += A[i][j]
                    cnt += 1

        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    if A[i][j] < total/cnt:
                        A[i][j] += 1
                    elif A[i][j] > total/cnt:
                        A[i][j] -= 1

ans = 0
for i in range(n):
    for j in range(m):
        ans += A[i][j]
print(ans)