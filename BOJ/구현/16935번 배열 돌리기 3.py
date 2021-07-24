n,m,r = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
C = list(map(int, input().split()))

def up_down(A):
    result = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[(n-1) - i][j] = A[i][j]
    return result

def left_right(A):
    result = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[i][(m-1)-j] = A[i][j]
    return result

def right_rotate(A):
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][(n-1)-i] = A[i][j]
    return result

def left_rotate(A):
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[(m-1)-j][i] = A[i][j]
    return result

def bbeul_zit(A,num):
    k = n // 2
    l = m // 2

    one = [i[:l] for i in A[:k]]
    two = [i[l:] for i in A[:k]]
    three = [i[l:] for i in A[k:]]
    four = [i[:l] for i in A[k:]]

    result = []

    if num == 5:
        for x,y in zip(four,one):
            result.append(x+y)

        for x,y in zip(three,two):
            result.append(x+y)

    if num == 6:
        for x,y in zip(two,three):
            result.append(x+y)

        for x,y in zip(one,four):
            result.append(x+y)
    return result

for c in C:
    if c == 1:
        A = up_down(A)
    if c == 2:
        A = left_right(A)
    if c == 3:
        A = right_rotate(A)
    if c == 4:
        A = left_rotate(A)
    if c == 5:
        A = bbeul_zit(A,c)
    if c == 6:
        A = bbeul_zit(A,c)

    n = len(A)
    m = len(A[0])
for l in A:
    print(' '.join(map(str, l)))