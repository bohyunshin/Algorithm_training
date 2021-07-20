from collections import deque
n = int(input())
miro = list(map(int, input().split()))
dist = [0]*n
current = 0
visited = [-1]*n

visited[current] = 0
q = deque()
q.append(current)

while q:
    x = q.popleft()
    for i in range(1,miro[x]+1):
        nx = x + i
        if 0 <= nx < n:
            if visited[nx] == -1 or visited[nx] > visited[x] + 1:
                visited[nx] = visited[x] + 1
                q.append(nx)
print(-1 if visited[n-1] == -1 else visited[n-1])