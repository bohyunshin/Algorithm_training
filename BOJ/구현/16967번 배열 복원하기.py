h,w,x,y = map(int, input().split())
B = []
for _ in range(h+x):
    B.append(list(map(int, input().split())))
A = [(i,j) for i in range(h) for j in range(w)]
moved_A = [(i+x,j+y) for i in range(h) for j in range(w)]
only_A = set(A) - set(moved_A)
only_moved_A = set(moved_A) - set(A)

ans = [[0]*w for _ in range(h)]
for i,j in only_A:
    ans[i][j] = B[i][j]
for i,j in only_moved_A:
    ans[i-x][j-y] = B[i][j]

for i in range(h):
    for j in range(w):
        if ans[i][j] == 0:
            ans[i][j] = B[i][j] - ans[i-x][j-y]
for i in ans:
    print(' '.join(list(map(str, i))))
