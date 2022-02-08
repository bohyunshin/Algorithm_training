from collections import deque
n,k,m = map(int,input().split())
if n == 1:
    print(1)
    exit()
station = [[] for _ in range(n+1)]
ht = [[] for _ in range(m)]
for tube in range(m):
    # row = list(map(int,input().split()))
    for vertex in map(int,input().split()):
        station[vertex].append(tube)
        ht[tube].append(vertex)
visited_station = [-1]*(n+1)
visited_ht = [False]*m
q = deque()
visited_station[1] = 1
for tube in station[1]:
    visited_ht[tube] = True
    for v in ht[tube]:
        if v == 1:
            continue
        visited_station[v] = visited_station[1]+1
        q.append(v)
while q:
    current = q.popleft()
    if current == n:
        print(visited_station[current])
        exit()
    next_ht = []
    for tube in station[current]:
        if visited_ht[tube] == False:
            next_ht.append(tube)
            visited_ht[tube] = True
    for h in next_ht:
        for v in ht[h]:
            if visited_station[v] == -1 and v != current:
                visited_station[v] = visited_station[current]+1
                q.append(v)
print(-1)

# for i in map(int,input().split()):
#     print(i)