from collections import deque, defaultdict

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(input())
for i in range(n):
    for j in range(m):
        if a[i][j] == '0':
            x, y = i, j
# visited = [[[-1]*7 for _ in range(m)] for _ in range(n)]
visited = {}
keys = ['a', 'b', 'c', 'd', 'e', 'f']
doors = ['A', 'B', 'C', 'D', 'E', 'F']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
# visited[x][y][6] = 0
visited[(x, y, '')] = 0
q.append((x, y, ''))
while q:
    x, y, k = q.popleft()
    if a[x][y] == '1':
        print(visited[(x, y, k)])
        exit()
        break
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and a[nx][ny] != '#':
            if a[nx][ny] in keys:
                if a[nx][ny] in k:
                    new_k = k
                else:
                    new_k = k + a[nx][ny]
                    new_k = ''.join(sorted([j for j in new_k]))
                if (nx, ny, new_k) not in visited.keys():
                    visited[(nx, ny, new_k)] = visited[(x, y, k)] + 1
                    q.append((nx, ny, new_k))
            elif a[nx][ny] in doors:
                for owned_key in k:
                    if owned_key == a[nx][ny].lower():
                        new_k = k
                        if (nx, ny, new_k) not in visited.keys():
                            visited[(nx, ny, new_k)] = visited[(x, y, k)] + 1
                            q.append((nx, ny, new_k))
            else:
                if (nx, ny, k) not in visited.keys():
                    visited[(nx, ny, k)] = visited[(x, y, k)] + 1
                    q.append((nx, ny, k))
print(-1)
