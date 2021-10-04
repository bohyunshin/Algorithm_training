from collections import defaultdict
n = int(input())
pop = []
for _ in range(n):
    pop.append(list(map(int,input().split())))
def mendering(x,y,d1,d2,n):
    A = [[0]*n for _ in range(n)]
    nx,ny = x,y
    for i in range(d1+1):
        A[nx][ny] = 5
        nx += 1
        ny -= 1
    nx,ny = x,y
    for i in range(d2+1):
        A[nx][ny] = 5
        nx += 1
        ny += 1
    nx,ny = x+d1,y-d1
    for i in range(d2+1):
        A[nx][ny] = 5
        nx += 1
        ny += 1
    nx,ny = x+d2,y+d2
    for i in range(d1+1):
        A[nx][ny] = 5
        nx += 1
        ny -= 1
    # 안쪽 채워두기.
    for i in range(n):
        index = []
        for j in range(n):
            if A[i][j] == 5:
                index.append(j)
        if len(index) == 0:
            continue
        start = min(index)
        end = max(index)
        for j in range(start,end+1):
            A[i][j] = 5

    for i in range(n):
        for j in range(n):
            if A[i][j] == 5:
                continue
            if 0 <= i < x+d1 and 0 <= j <= y:
                A[i][j] = 1
            elif 0 <= i <= x+d2 and y < j <= n-1:
                A[i][j] = 2
            elif x+d1 <= i <= n-1 and 0 <= j < y-d1+d2:
                A[i][j] = 3
            elif x+d2 < i <= n-1 and y-d1+d2 <= j <= n-1:
                A[i][j] = 4
    # for i in A:
    #     print(i)
    return A
# mendering(1,4,3,2,7)
ans = 1e100
for x in range(n):
    for y in range(n):
        for d1 in range(1,n+1):
            for d2 in range(1,n+1):
                # print(x,y,d1,d2,0 <= x < x+d1+d2 <= n-1,0 <= y-d1 < y < y+d2 <= n-1)
                if 0 <= x < x+d1+d2 <= n-1 and 0 <= y-d1 < y < y+d2 <= n-1:
                    # print(x,y,d1,d2)
                    A = mendering(x,y,d1,d2,n)
                    dct = defaultdict(int)
                    for i in range(n):
                        for j in range(n):
                            dct[A[i][j]] += pop[i][j]
                    MAX = max(dct.values())
                    MIN = min(dct.values())
                    if ans > MAX-MIN:
                        ans = MAX-MIN
                    # for i in A:
                    #     print(i)
                    # print()
print(ans)