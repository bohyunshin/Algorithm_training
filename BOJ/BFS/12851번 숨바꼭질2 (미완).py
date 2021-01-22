from collections import deque

n,k = map(int, input().split())
graph = [0]*100001
ways = [0]*100001
# 현재 수빈이의 위치를 표시해줌
# graph[n] = 1
# 좌,우,순간이동 좌표를 표시
def bfs(graph, start):

    queue = deque()
    queue.append(start)
    while queue:
        x = queue.popleft()

        # if x == k:
        #     break

        nxs = [x-1, x+1, x * 2]

        # 인접한 세 좌표를 돈다
        for nx in nxs:
            # 주어진 범위를 벗어나는 경우는 제외
            if 0 <= nx < 100001:
                # 처음 가본 곳이라면
                # 그곳으로 가보고 1을 더해줌
                if graph[nx] == 0 or graph[nx] >= graph[x]+1:
                    queue.append(nx)
                    ways[nx] += 1
                    graph[nx] = graph[x] + 1
    print(graph[k])
    print(ways[k])
bfs(graph,n)