from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**6)

n,k = map(int, input().split())
visited = [-1]*100001
q = deque()
q.append(n)
visited[n] = 0
myhash = {}

while q:
    x = q.popleft()

    if len(myhash.keys()) == 0:
        myhash[x] = x

    if x == k:
        break

    nxs = [x-1, x+1, 2*x]
    for nx in nxs:
        if 0 <= nx < len(visited):
            if visited[nx] == -1 or visited[nx] > visited[x] + 1:
                visited[nx] = visited[x] + 1
                q.append(nx)
                myhash[nx] = x

print(visited[k])
answer = [str(k)]
while k != n:
    answer.append(myhash[k])
    k = myhash[k]
print(' '.join(map(str, answer[::-1])))
