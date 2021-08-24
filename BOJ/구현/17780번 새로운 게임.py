import sys

class Piece:
    def __init__(self, no, direction):
        self.no = no
        self.direction = direction
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def opposite(direction):
    if direction == 0:
        return 1
    if direction == 1:
        return 0
    if direction == 2:
        return 3
    return 2


def go(a, where, x, y, nx, ny):
    for p in a[x][y]:
        a[nx][ny].append(p)
        where[p.no] = (nx, ny)
    a[x][y].clear()


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
a = [[[] for j in range(n)] for i in range(n)]
where = [None] * m

for i in range(m):
    x, y, direction = map(int, input().split())
    a[x - 1][y - 1].append(Piece(i, direction - 1))
    where[i] = (x - 1, y - 1)

for turn in range(1, 1001):
    for k in range(m):
        x, y = where[k]
        if a[x][y][0].no == k:  # bottom
            direction = a[x][y][0].direction
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n:  # in
                if board[nx][ny] == 2:
                    a[x][y][0].direction = opposite(direction)
            else:
                a[x][y][0].direction = opposite(direction)
            direction = a[x][y][0].direction
            nx = x + dx[direction]
            ny = y + dy[direction]

            if 0 <= nx < n and 0 <= ny < n:  # in
                if board[nx][ny] == 0:
                    go(a, where, x, y, nx, ny)
                elif board[nx][ny] == 1:
                    a[x][y].reverse()
                    go(a, where, x, y, nx, ny)
                if len(a[nx][ny]) >= 4:
                    print(turn)
                    sys.exit(0)
            else:  # out
                pass
print(-1)

