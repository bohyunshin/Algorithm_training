from collections import deque
n,k = map(int, input().split())
visited = [-1]*100001
q = deque()
q.append(n)
visited[n] = 0
while q:
    x = q.popleft()
    # print(x, end=' ')
    if x == k:
        break
    nxs = [x-1, x+1, 2*x]
    for nx in nxs:
        if 0 <= nx < len(visited):
            if visited[nx] == -1 or visited[nx] > visited[x] + 1:
                visited[nx] = visited[x] + 1
                q.append(nx)
print(visited[k])

