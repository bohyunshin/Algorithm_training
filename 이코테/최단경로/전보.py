import heapq
n,m,start = map(int, input().split())
INF = int(1e9)
visited = [False]*(n+1)
distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def djks(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
djks(start)
count = 0
time = []
for i in range(1, n+1):
    if distance[i] != INF:
        count += 1
        time.append(distance[i])
print(count-1, max(time), end=' ')
