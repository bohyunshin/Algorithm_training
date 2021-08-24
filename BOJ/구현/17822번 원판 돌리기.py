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

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    FLAG = False
    dct = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                continue
            temp = [(i,j)]
            for l in range(4):
                ni = i + dx[l]
                nj = j + dy[l]
                if 0 <= ni < n and 0 <= nj < m:
                    if A[i][j] == A[ni][nj]:
                        temp.append((ni,nj))
            if j == 0:
                if A[i][j] == A[i][m-1]:
                    temp.append((i,m-1))
            if j == m-1:
                if A[i][j] == A[i][0]:
                    temp.append((i,0))

            if len(temp) >= 2:
                FLAG = True
                dct[A[i][j]] += temp
    for key in dct.keys():
        for i,j in dct[key]:
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
                    if A[i][j]*cnt < total:
                        A[i][j] += 1
                    elif A[i][j]*cnt > total:
                        A[i][j] -= 1

ans = 0
for i in range(n):
    for j in range(m):
        ans += A[i][j]
print(ans)