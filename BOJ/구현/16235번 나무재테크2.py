dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
n, m, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
d = [[5]*n for _ in range(n)] # 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
tree = [[[] for j in range(n)] for i in range(n)]
for _ in range(m):
    x, y, age = map(int, input().split())
    tree[x-1][y-1].append(age)

# 봄 -> 나무 처리, 여름 -> 나무 처리, 가을 -> 나무 처리, 겨울 -> 나무 처리
# 로 하면 터짐
# 나무별로 돌면서 봄 -> 여름 -> 가을 -> 겨울을 처리해줌
# 이걸 왜 할수 있냐면? 봄, 여름, 겨울의 연산은 서로 다른 나무에 영향을 주지 않음
# 가을의 연산이 다음 계절의 나무에 영향을 주는데, 이는 따로 p라는 배열을 만들어서 계산해줌


for _ in range(l):
    p = [[0]*n for _ in range(n)]
    # 나무별로 봄, 여름, 가을, 겨울 계산을 해줌
    for i in range(n):
        for j in range(n):
            temp = []
            # 어린 나무부터 양분을 먹으니까 정렬해줌
            tree[i][j].sort()
            dead = 0
            for x in tree[i][j]:
                if x <= d[i][j]:
                    # 봄 계산
                    d[i][j] -= x # 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
                    temp.append(x+1)
                    if (x+1) % 5 == 0: # 번식하는 나무는 나이가 5의 배수이어야 하며,
                        for k in range(8):
                            nx,ny = i+dx[k],j+dy[k]
                            if 0 <= nx < n and 0 <= ny < n: #상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
                                # 가을 계산
                                p[nx][ny] += 1 # 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
                else:
                    # 여름 계산
                    dead += x//2
            # 나무 업데이트
            tree[i][j] = temp
            d[i][j] += dead
            # 겨울 계산
            d[i][j] += a[i][j] # 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
    # 연산을 다 해주고 나서 가을에 있었던 나무 계산을 원래 나무에 더해줌
    for i in range(n):
        for j in range(n):
            for k in range(p[i][j]):
                tree[i][j].append(1)
ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)