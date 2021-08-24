n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
result = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(m):
        x = i
        y = j
        tmp = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if A[x][y] > A[nx][ny]:
                    result += A[x][y] - A[nx][ny]
            else:
                result += A[x][y]
print(result + 2*n*m)

