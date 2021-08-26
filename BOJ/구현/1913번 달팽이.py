n = int(input())
A = [[0]*n for _ in range(n)]
k = 0
current = n*n
while True:
    for i in range(k,n-1-k):
        A[i][k] = current
        current -= 1
    # for i in A:
        # print(i)
    for j in range(k,n-1-k):
        A[n-1-k][j] = current
        current -= 1
    # for i in A:
    #     print(i)
    for i in range(n-1-k,k,-1):
        A[i][n-1-k] = current
        current -= 1
    # for i in A:
    #     print(i)
    for j in range(n-1-k,k,-1):
        A[k][j] = current
        current -= 1
    # for i in A:
    #     print(i)
    k += 1
    if n // 2 == k:
        A[k][k] = current
        break

for i in A:
    print(' '.join(list(map(str,i))))

m = int(input())
for i in range(n):
    for j in range(n):
        if A[i][j] == m:
            print(i+1,j+1,end=' ')
            break