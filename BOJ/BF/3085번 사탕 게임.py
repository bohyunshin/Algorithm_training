n = int(input())
A = []
for _ in range(n):
    A.append([i for i in input()])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = -1

for x in range(n):
    for y in range(n):
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                a = A[x][y]
                b = A[nx][ny]
                if a != b:
                    A[x][y],A[nx][ny] = A[nx][ny],A[x][y]
                    # print(x,y,nx,ny)
                    # print(A)

                    # 행 체크해보기
                    for j in range(n):
                        cnt = 1
                        before = A[j][0]
                        for k in range(1,n):
                            after = A[j][k]
                            if before == after:
                                cnt += 1
                                ans = max(ans, cnt)
                            else:
                                ans = max(ans,cnt)
                                before = after
                                cnt = 1

                    # 열 체크해보기
                    for k in range(n):
                        cnt = 1
                        before = A[0][k]
                        for j in range(1, n):
                            after = A[j][k]
                            if before == after:
                                cnt += 1
                                ans = max(ans, cnt)
                            else:
                                ans = max(ans, cnt)
                                before = after
                                cnt = 1

                    # 원상복구
                    A[x][y], A[nx][ny] = A[nx][ny], A[x][y]
print(ans)
# print(A)