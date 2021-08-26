from copy import deepcopy
n,m,r = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
final_result = [[0]*m for _ in range(n)]
x,y = (0,0)
cnt = 0

for _ in range(r):
    while True:
        n = len(A)
        m = len(A[0])
        result = [[0] * m for _ in range(n)]
        # (0,0)부터 돌리기.
        # 왼쪽 돌리기.
        while x < n-1:
            result[x+1][y] = A[x][y]
            x += 1
        # 아래쪽 돌리기.
        while y < m-1:
            result[x][y+1] = A[x][y]
            y += 1
        # 오른쪽 돌리기.
        while x > 0:
            result[x-1][y] = A[x][y]
            x -= 1
        # 위쪽 돌리기.
        while y > 0:
            result[x][y-1] = A[x][y]
            y -= 1

        for i in range(n):
            for j in range(m):
                if result[i][j] != 0:
                    final_result[cnt+i][cnt+j] = result[i][j]


        A = [A[i][1:-1] for i in range(1,n-1)]
        cnt += 1

        if len(A) <= 1:
            break

    A = deepcopy(final_result)
    cnt = 0

for i in final_result:
    print(' '.join(list(map(str, i))))