from collections import deque
import copy

n = int(input())
indegree = [0]*(n+1)
time = [0]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(1,n+1):
    lst = [int(j) for j in input().split()]
    time[i] = lst[0]
    if len(lst) == 2:
        continue
    else:
        v = lst[0]
        indeg = lst[1:-1]
        for j in indeg:
            indegree[i] += 1
            graph[j].append(i)

def topology_sort():
    q = deque()
    result = copy.deepcopy(time)


    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])
topology_sort()

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""