n,m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)

"""
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""