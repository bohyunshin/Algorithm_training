from itertools import combinations
from collections import deque
n,k = input().split()
k = int(k)
locs = [i for i in range(len(n))]
q = deque()
visited = [[False]*1000001 for _ in range(k+1)]
q.append((0,n))
visited[0][int(n)] = False
while q:
    cnt,n = q.popleft()
    if cnt == k:
        continue
    for c in combinations(locs,2):
        x,y = c
        if n[y] == '0' and x == 0:
            continue
        next_n = [i for i in n]
        next_n[x], next_n[y] = next_n[y], next_n[x]
        next_n = ''.join(next_n)
        if visited[cnt+1][int(next_n)] == False:
            visited[cnt+1][int(next_n)] = True
            q.append((cnt+1,next_n))
ans = -1
for i in range(1000001):
    if visited[k][i]:
        ans = i
print(ans)