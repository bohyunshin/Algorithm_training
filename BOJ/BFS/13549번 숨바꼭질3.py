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
            if nx == 2*x:
                dist = visited[x]
            else:
                dist = visited[x] + 1
            if visited[nx] == -1 or visited[nx] > dist:
                visited[nx] = dist
                q.append(nx)
print(visited[k])

