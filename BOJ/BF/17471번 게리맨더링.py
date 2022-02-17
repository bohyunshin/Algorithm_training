from itertools import combinations
n = int(input())
population = [0] + list(map(int,input().split()))
graph = [[]]
for _ in range(n):
    info = list(map(int,input().split()))
    graph.append(info[1:])
mid = n // 2 if n % 2 == 0 else (n // 2) + 1
choice = [k for k in range(1,mid+1)]
def dfs(x,region):
    global cnt,visited
    if visited[x]:
        return
    visited[x] = True
    cnt += 1
    for v in graph[x]:
        if v in region:
            dfs(v,region)
ans = -1
for k in choice:
    for a in combinations(range(1,n+1),k):
        b = [i for i in range(1,n+1) if i not in a]
        regions = [a,b]
        regions_pop = []
        flag = 0
        for region in regions:
            cnt = 0
            visited = [False]*(n+1)
            dfs(region[0],region)
            if cnt == len(region):
                flag += 1
                tmp = 0
                for i in region:
                    tmp += population[i]
                regions_pop.append(tmp)
        if flag == 2:
            x,y = regions_pop
            tmp = abs(x-y)
            if ans == -1 or ans > tmp:
                ans = tmp
print(ans)

# from itertools import combinations
#
# n = int(input())
# population = [0] + list(map(int, input().split()))
# graph = [[]]
# for _ in range(n):
#     info = list(map(int, input().split()))
#     graph.append(info[1:])
# mid = n // 2 if n % 2 == 0 else (n // 2) + 1
# choice = [k for k in range(1, mid + 1)]
#
#
# def dfs(x, region):
#     global cnt, visited
#     if visited[x]:
#         return
#     visited[x] = True
#     cnt += 1
#     for v in graph[x]:
#         if v in region:
#             dfs(v, region)
#
#
# ans = -1
# for k in choice:
#     for a in combinations(range(1, n + 1), k):
#         b = [i for i in range(1, n + 1) if i not in a]
#         regions = [a, b]
#
#         cnt = 0
#         visited = [False] * (n + 1)
#         dfs(a[0], a)
#         if cnt != len(a):
#             continue
#         cnt = 0
#         visited = [False] * (n + 1)
#         dfs(b[0], b)
#         if cnt != len(b):
#             continue
#         # print(a,b)
#         pop_a = 0
#         pop_b = 0
#         for i in a:
#             pop_a += population[i]
#         for i in b:
#             pop_b += population[i]
#         tmp = abs(pop_a - pop_b)
#         if ans == -1 or ans > tmp:
#             ans = tmp
# print(ans)