n,m = map(int, input().split())
r,c,d = map(int, input().split())

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
direction = {0:3, 1:0, 2:1, 3:2}

dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 로봇 청소기 시작하는 칸은 항상 빈칸이니까 1로 시작함.
answer = 1
# 청소처리 해줌.
A[r][c] = 2

while True:
    FLAG = False
    cnt = 0
    for _ in range(4):
        # 2-(a)
        d = direction[d]
        nr = r + dr[d]
        nc = c + dc[d]
        if A[nr][nc] == 0:
            FLAG = True
            answer += 1
            A[nr][nc] = 2
            break
        if A[nr][nc] == 1 or A[nr][nc] == 2:
            cnt += 1

    if FLAG:
        r = nr
        c = nc
        continue

    if cnt == 4:
        if d == 0:
            if A[r+1][c] == 1:
                break
            else:
                r += 1
        if d == 1:
            if A[r][c-1] == 1:
                break
            else:
                c -= 1
        if d == 2:
            if A[r-1][c] == 1:
                break
            else:
                r -= 1
        if d == 3:
            if A[r][c+1] == 1:
                break
            else:
                c += 1
print(answer)