n = int(input())
A = [[0]*100 for _ in range(100)]
for _ in range(n):
    a,b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            A[99-(b+i)][a+j] += 1

# for i in A[80:]:
#     print(i[:30])

def cutting(x,y,A):
    nx,ny = x,y
    while A[x][ny] >= 1:
        ny += 1
    ny -= 1
    garo = ny-y+1
    # print(garo)
    while all([i >= 1 for i in A[nx][y:ny+1]]):
        nx += 1
    nx -= 1
    sero = nx-x+1
    if garo >= 1 and sero >= 1:
        return garo*sero
        # print(garo*sero,nx,x,ny,y)
ans = []
for i in range(100):
    for j in range(100):
        # cutting(i,j,A)
        if A[i][j] != 0:
            ans.append(cutting(i,j,A))
        # break
print(max(ans))