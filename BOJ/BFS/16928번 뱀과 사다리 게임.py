from collections import deque

n,m = map(int, input().split())
graph = [0] * 101
ladder = {}
snake = {}
for _ in range(n):
    _from, _to = map(int, input().split())
    ladder[_from] = _to
for _ in range(m):
    _from, _to = map(int, input().split())
    snake[_from] = _to

dxs = [1,2,3,4,5,6]

q = deque()
start = 1
q.append(start)
while q:
    x = q.popleft()
    if x == 100:
        break
    for dx in dxs:
        nx = x + dx
        # 100번칸보다 크면 이동할 수 없음
        if nx > 100:
            continue
        # 만약 이동한 칸이 사다리이고 사다리로 이동한 곳이 최초방문이라면
        # 이전 주사위 던진 수에 1을 더해서 방문 표시를 해줌
        # 큐에도 넣어줌
        if nx in ladder.keys() and graph[nx] == 0:
            nx_ladder = ladder[nx]
            if graph[nx_ladder] == 0:
                graph[nx_ladder] = graph[x] + 1
                q.append(nx_ladder)
            continue
        # 뱀에 이동한다면 똑같이 해줌
        if nx in snake.keys() and graph[nx] == 0:
            nx_snake = snake[nx]
            if graph[nx_snake] == 0:
                graph[nx_snake] = graph[x] + 1
                q.append(nx_snake)
            continue
        # 뱀 사다리 둘다 아니라면
        if graph[nx] == 0:
            graph[nx] = graph[x] + 1
            q.append(nx)
print(graph[100])