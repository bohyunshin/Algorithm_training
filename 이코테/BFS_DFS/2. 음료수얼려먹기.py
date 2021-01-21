n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(graph, x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False

    # graph의 값이 0이라면, 즉 아직 방문되지 않았다면
    if graph[x][y] == 0:
        # 현재 노드를 방문 처리
        graph[x][y] = 1

        # 상, 하, 좌, 우에 대해서 탐색함
        # 만약 0인 값인 애들이 있으면 1로 채워둠

        dfs(graph, x-1, y)
        dfs(graph, x+1, y)
        dfs(graph, x, y-1)
        dfs(graph, x, y+1)

        # 여기까지 끝냈으면 어떤 시작 노드에서
        # 주변 노드의 빈 값을 모두 1로 채운 것임
        return True
    # graph의 값이 0이 아니라면, 이미 채운 것이니까 빠져나온다
    else:
        return False

icecream = 0

for i in range(n):
    for j in range(m):
        if dfs(graph,i,j) == True:
            icecream += 1

print(icecream)