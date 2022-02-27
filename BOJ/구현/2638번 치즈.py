from collections import deque

n, m = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
ans = 0
while True:
    queue = deque()
    ch = [[0 for _ in range(m)] for _ in range(n)]
    ch[0][0] = 1
    queue.append([0, 0])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and not ch[nx][ny]:
                if cheeze[nx][ny]:
                    cheeze[nx][ny] += 1
                else:
                    ch[nx][ny] = 1
                    queue.append([nx, ny])

    flag = 0
    for i in range(n):
        for j in range(m):
            if cheeze[i][j] >= 3:
                cheeze[i][j] = 0
            elif 0 < cheeze[i][j]:
                flag = 1
                cheeze[i][j] = 1
    ans += 1

    if not flag:
        print(ans)
        break