def go(step, x1, y1, x2, y2,n,m,A):
    if step == 11:
        return -1
    fall1 = False
    fall2 = False
    if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m:
        fall1 = True
    if x2 < 0 or x2 >= n or y2 < 0 or y2 >= m:
        fall2 = True
    if fall1 and fall2:
        return -1
    if fall1 or fall2:
        return step
    ans = -1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for k in range(4):
        nx1,ny1 = x1+dx[k],y1+dy[k]
        nx2,ny2 = x2+dx[k],y2+dy[k]
        if 0 <= nx1 < n and 0 <= ny1 < m and A[nx1][ny1] == '#':
            nx1,ny1 = x1,y1
        if 0 <= nx2 < n and 0 <= ny2 < m and A[nx2][ny2] == '#':
            nx2,ny2 = x2,y2
        temp = go(step+1,nx1,ny1,nx2,ny2,n,m,A)
        if temp == -1:
            continue
        if ans == -1 or ans > temp:
            ans = temp
    return ans

def solution(A,n,m):
    coin =  []
    for i in range(n):
        for j in range(m):
            if A[i][j] == 'o':
                coin.append((i,j))
    (x1,y1),(x2,y2) = coin[0], coin[1]
    ans = go(0,x1,y1,x2,y2,n,m,A)
    return ans

if __name__ == '__main__':
    n,m = map(int, input().split())
    A = []
    for _ in range(n):
        A.append([i for i in input()])
    ans = solution(A,n,m)
    print(ans)