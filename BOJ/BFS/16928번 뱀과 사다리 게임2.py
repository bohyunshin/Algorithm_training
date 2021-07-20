from collections import deque

n,m = map(int, input().split())
ladder = {}
for _ in range(n):
    x,y = map(int, input().split())
    ladder[x] = y
snake = {}
for _ in range(m):
    u,v = map(int, input().split())
    snake[u] = v

visited = [False]*101
dice = [0]*101

q = deque()
start = 1
q.append(start)
visited[start] = True

# 똑같이 bfs 구현하는데
# snake, ladder 조건만 추가해주면 됨.
# snake, ladder의 key에 현재 위치가 포함될때 nx를 바꿔줄 위치로 지정해주고
# 원래 해주던대로 bfs 조건을 해주면 됨
while q:
    x = q.popleft()
    for i in range(1,7):
        nx = x + i
        if nx <= 100:
            if nx in snake.keys():
                nx = snake[nx]
            if nx in ladder.keys():
                nx = ladder[nx]
            if visited[nx] is False or dice[nx] > dice[x] + 1:
                visited[nx] = True
                dice[nx] = dice[x] + 1
                q.append(nx)
print(dice[100])
