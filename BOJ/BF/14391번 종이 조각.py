n,m = map(int,input().split())
A = []
for _ in range(n):
    A.append([int(i) for i in input()])
k = n*m
answer = -1
for s in range(1<<(n*m)):
    sum = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i*m+j
            if s & (1 << k) == 0:
                cur = cur * 10 + A[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i*m+j
            if s & (1 << k) != 0:
                cur = cur * 10 + A[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    answer = max(answer,sum)
print(answer)