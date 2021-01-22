from collections import deque

n,k = map(int, input().split())
graph = [0]*100001
# 현재 수빈이의 위치를 표시해줌
# graph[n] = 1
# 좌,우,순간이동 좌표를 표시
def bfs(graph, start):

    queue = deque()
    queue.append(start)
    min = []
    count = 0
    while queue:
        x = queue.popleft()
        # print(x)

        # 만약에 수빈이가 위치한 곳이라면
        # 바로 탈출
        if x == k:
            count += 1
            min.append(graph[k])
            graph[k] -= 1


        nxs = [x-1, x+1, x * 2]

        # 인접한 세 좌표를 돈다
        for nx in nxs:
            # 주어진 범위를 벗어나는 경우는 제외
            if nx < 0 or nx >= 100001:
                continue
            # 처음 가본 곳이라면
            # 그곳으로 가보고 1을 더해줌
            if graph[nx] == 0:
                queue.append(nx)
                graph[nx] = graph[x] + 1

                # if nx == k:
                #     count += 1
                #     min.append(graph[nx])
                #     graph[nx] = 0

    return min, count

print(bfs(graph,n))