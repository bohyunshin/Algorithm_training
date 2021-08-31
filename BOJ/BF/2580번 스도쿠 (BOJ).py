def go(z,c1,c2,c3,A):
    if z >= 81:
        for row in A:
            print(' '.join(list(map(str,row))))
        return True
    n = len(A)
    x,y = z // n, z % n
    if A[x][y] != 0:
        return go(z+1,c1,c2,c3,A)
    else:
        for i in range(1,10):
            if c1[x][i] == c2[y][i] == c3[square(x,y)][i] == False:
                c1[x][i] = c2[y][i] = c3[square(x,y)][i] = True
                A[x][y] = i
                if go(z+1,c1,c2,c3,A):
                    return True
                A[x][y] = 0
                c1[x][i] = c2[y][i] = c3[square(x, y)][i] = False
    return False
def square(x,y):
    return (x//3)*3 + (y//3)

def solution(A):
    n = 9
    c1 = [[False] * 10 for _ in range(n)]
    c2 = [[False] * 10 for _ in range(n)]
    c3 = [[False] * 10 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if A[i][j] != 0:
                c1[i][A[i][j]] = True
                c2[j][A[i][j]] = True
                c3[square(i, j)][A[i][j]] = True
    go(0,c1,c2,c3,A)

if __name__ == '__main__':
    A = []
    for _ in range(9):
        A.append(list(map(int, input().split())))
    solution(A)