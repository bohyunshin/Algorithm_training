n = int(input())
A = [[0]*100 for _ in range(100)]
S = [[0]*100 for _ in range(100)]
for _ in range(n):
    a,b = map(int, input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            A[i][j] = 1
for i in range(1,100):
    for j in range(1,100):
        if A[i][j] == 1:
            S[i][j] = S[i][j-1] + A[i][j]
ans = 0
for i in range(1,100):
    for j in range(1,100):
        if A[i][j] == 0:
            continue
        height = 0
        width = S[i][j]
        for k in range(i,0,-1):
            if S[k][j] == 0:
                break
            height += 1
            width = min(width, S[k][j])
            if ans < width*height:
                ans = width*height
print(ans)