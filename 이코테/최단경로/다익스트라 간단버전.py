import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n,m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [ [] for i in range(n+1)]
# 방문 여부를 담는 리스트
visited = [False]*(n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서, 최단 거리를 가지는 노드의 번호를 반환
def get_smallest_node():
    min_dist = INF
    min_index = 0
    for i in range(n+1):
        if distance[i] < min_dist and visited[i] is False:
            min_dist = distance[i]
            min_index = i
    return min_index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우 INF으로 출력
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])