from collections import deque

# DFS 정의
def dfs(graph, v, visited, result):
    # 현재 노드를 방문 처리
    visited[v] = True
    # 현재 노드를 출력
    print(v, end=' ')
    result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited,result)
    return result

# def bfs(graph, start, visited):
#     queue = deque([start])
#     # 현재 위치를 방문 처리함
#     visited[start] = True
#     # 큐가 빌때까지 반복함
#     while queue:
#         # 큐에서 가장 먼저 들어온애를 빼내고 출력함
#         v = queue.popleft()
#         print(v, end=' ')
#         # 출력된 애와 인접하면서 방문되지 않은 애들을 돌며 방문함
#         # 그리고 걔네를 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# 그래프 자료형 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False]*9
result = []
a = dfs(graph,1,visited,result)
print(a)

# bfs(graph, 1, visited)