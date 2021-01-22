from collections import deque

n,k = map(int, input().split())
bigger = max(n,k)
graph = [0]*100001
visited = [False]*100001
# 현재 수빈이의 위치를 표시해줌
# graph[n] = 1
# 좌,우,순간이동 좌표를 표시
secs = 0
def bfs(graph, start):

    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()

        # print(x)

        # 만약에 수빈이가 위치한 곳이라면
        # 바로 탈출
        if x == k:
            print(graph[k])
            exit(0)

        nxs = [x-1, x+1, x * 2]

        # 인접한 세 좌표를 돈다
        for i,nx in enumerate(nxs):
            # 주어진 범위를 벗어나는 경우는 제외
            if nx < 0 or nx >= 100001:
                continue
            # 처음 가본 곳이라면
            # 그곳으로 가보고 1을 더해줌
            if visited[nx] is False:
                queue.append(nx)
                visited[nx] = True
                if i == 2:
                    graph[nx] = graph[x]
                else:
                    graph[nx] = graph[x] + 1


bfs(graph,n)