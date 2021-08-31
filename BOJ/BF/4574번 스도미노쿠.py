
def square(x,y):
    return (x//3)*3 + (y//3)

def go(z,c1,c2,c3,A,d):
    if z >= 81:
        for row in A:
            print(''.join(list(map(str,row))))
        return True
    n = len(A)
    x,y = z // n, z % n
    dx = [0,1]
    dy = [1,0]
    if A[x][y] != 0:
        return go(z+1,c1,c2,c3,A,d)
    else:
        for k in range(2):
            nx,ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<n and A[nx][ny] == 0:
                for i in range(1,10):
                    for j in range(1,10):
                        if i == j or d[i][j] == True:
                            continue
                        if c1[x][i] == c2[y][i] == c3[square(x,y)][i] == False and \
                            c1[nx][j] == c2[ny][j] == c3[square(nx,ny)][j] == False:
                            c1[x][i] = c2[y][i] = c3[square(x,y)][i] = True
                            c1[nx][j] = c2[ny][j] = c3[square(nx, ny)][j] = True
                            A[x][y] = i
                            A[nx][ny] = j
                            d[i][j] = d[j][i] = True
                            if go(z+1,c1,c2,c3,A,d):
                                return True
                            A[x][y] = 0
                            A[nx][ny] = 0
                            d[i][j] = d[j][i] = False
                            c1[x][i] = c2[y][i] = c3[square(x, y)][i] = False
                            c1[nx][j] = c2[ny][j] = c3[square(nx, ny)][j] = False
    return False

def solution(n,dominos,nums):
    m = 10
    A = [[0]*9 for _ in range(9)]
    alpha = ['A','B','C','D','E','F','G','H','I']
    c1 = [[False] * m for _ in range(m)]
    c2 = [[False] * m for _ in range(m)]
    c3 = [[False] * m for _ in range(m)]
    d = [[False] * m for _ in range(m)]
    for domino in dominos:
        U,LU,V,LV = domino
        x1,y1 = alpha.index(LU[0]), int(LU[1])-1
        x2,y2 = alpha.index(LV[0]), int(LV[1])-1
        A[x1][y1] = int(U)
        A[x2][y2] = int(V)
        d[int(U)][int(V)]= d[int(V)][int(U)] = True
    for i,num in enumerate(nums):
        x,y = alpha.index(num[0]), int(num[1])-1
        A[x][y] = i+1
    for i in range(9):
        for j in range(9):
            if A[i][j] != 0:
                c1[i][A[i][j]] = True
                c2[j][A[i][j]] = True
                c3[square(i, j)][A[i][j]] = True
    go(0,c1,c2,c3,A,d)

if __name__ == '__main__':
    a = 1
    while True:
        n = int(input())
        if n == 0:
            break
        dominos = []
        for _ in range(n):
            dominos.append(input().split())
        nums = input().split()
        print(f'Puzzle {a}')
        solution(n,dominos,nums)
        a += 1