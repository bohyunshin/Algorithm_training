from collections import deque, defaultdict

def bfs(coin):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q = deque()
    visited = {}
    (x1,y1), (x2,y2) = coin
    visited[((x1,y1),(x2,y2))] = 0
    q.append(coin)
    while q:
        (x1, y1), (x2, y2) = q.popleft()
        for i in range(4):
            nx1,ny1 = x1+dx[i], y1+dy[i]
            nx2,ny2 = x2+dx[i], y2+dy[i]
            # 둘다 밖으로 나가면 패쓰.
            if (nx1 < 0 or nx1 >= n or ny1 < 0 or ny1 >= m) and \
                (nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= m):
                continue
            # 둘 중 하나만 밖으로 나갔으면 바로 빠져나옴.
            # 연산자를 or로 하면, 둘 모두 해당하는 것은 위에서 처리해줬으니 둘 중 하나만 해당되는 것에 걸림.
            if (nx1 < 0 or nx1 >= n or ny1 < 0 or ny1 >= m) or \
                (nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= m):
                return -1 if visited[((x1,y1),(x2,y2))]+1 > 10 else visited[((x1,y1),(x2,y2))]+1
            # 범위 내에 있다면,
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                # 두 동전이 가야할 곳 모두가 벽이라면, 안가봄
                if A[nx1][ny1] == '#' and A[nx2][ny2] == '#':
                    continue
                try:
                    tmp = visited[((nx1,ny1),(nx2,ny2))]
                except KeyError:
                    # 두 곳 모두 벽이 아니고, 처음 가보는 곳이라면,
                    if A[nx1][ny1] != '#' and A[nx2][ny2] != '#':
                        visited[((nx1,ny1),(nx2,ny2))] = visited[((x1,y1),(x2,y2))]+1
                        q.append(((nx1,ny1),(nx2,ny2)))
                    # 둘 중 하나만 벽이라면, 한곳만 이동시켜야 함.
                    # 첫 번째 동전이 갈 곳만 벽이라면,
                    elif A[nx1][ny1] == '#' and A[nx2][ny2] != '#':
                        visited[((x1,y1), (nx2,ny2))] = visited[((x1,y1), (x2,y2))] + 1
                        q.append(((x1,y1), (nx2,ny2)))
                    # 두 번째 동전이 갈 곳만 벽이라면,
                    elif A[nx1][ny1] != '#' and A[nx2][ny2] == '#':
                        visited[((nx1,ny1), (x2,y2))] = visited[((x1,y1), (x2,y2))] + 1
                        q.append(((nx1,ny1), (x2,y2)))
    return -1

def solution(n,m,A):
    coin = []
    for i in range(n):
        for j in range(m):
            if A[i][j] == 'o':
                coin.append((i, j))
    ans = bfs(coin)
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    A = []
    for _ in range(n):
        A.append([i for i in input()])

    ans = solution(n,m,A)
    print(ans)