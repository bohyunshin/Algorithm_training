dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
n, m, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[5]*n for _ in range(n)] # 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
tree = [[[] for j in range(n)] for i in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    tree[x-1][y-1].append(age)
for _ in range(l):
    p = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = []
            tree[i][j].sort()
            dead = 0
            for x in tree[i][j]:
                if x <= d[i][j]:
                    d[i][j] -= x # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
                    temp.append(x+1)
                    if (x+1) % 5 == 0: # 번식하는 나무는 나이가 5의 배수이어야 하며,
                        for k in range(8):
                            nx,ny = i+dx[k],j+dy[k]
                            if 0 <= nx < n and 0 <= ny < n: #상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
                                p[nx][ny] += 1 # 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
                else:
                    dead += x//2
            tree[i][j] = temp
            d[i][j] += dead
            d[i][j] += a[i][j] # 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
    for i in range(n):
        for j in range(n):
            for k in range(p[i][j]):
                tree[i][j].append(1)
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)