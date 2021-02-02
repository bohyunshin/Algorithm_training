INF = int(1e9)

n,m = map(int, input().split())
# 노드의 개수가 n개인데 인덱스를 1부터 시작하려고 n+1로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 대각선은 모두 0으로 초기화
for i in range(1,n+1):
    graph[i][i] = 0

# 간선에 대한 정보 받음
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 수행 결과를 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print('INFINITY', end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

"""
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""