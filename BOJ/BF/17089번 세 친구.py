n, m = map(int,input().split())
a = [[False]*(n+1) for _ in range(n+1)]
degree = [0] * (n+1)
for _ in range(m):
    x, y = map(int,input().split())
    a[x][y] = a[y][x] = True
    degree[x] += 1
    degree[y] += 1

ans = -1

for i in range(1, n+1):
    for j in range(1, n+1):
        if a[i][j]:
            for k in range(1, n+1):
                if a[i][k] and a[j][k]:
                    s = degree[i] + degree[j] + degree[k] - 6
                    if ans == -1 or ans > s:
                        ans = s

print(ans)

# import sys
# from collections import defaultdict
# sys.setrecursionlimit(10**5)
# n,m = map(int,input().split())
# relation = {}
# for i in range(n):
#     relation[i] = defaultdict(bool)
# for _ in range(m):
#     x,y = map(int,input().split())
#     x -= 1
#     y -= 1
#     relation[x][y] = True
#     relation[y][x] = True
# a = [-1]*3
# ans = -1
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         if relation[i][j]:
#             for k in range(n):
#                 if j == k:
#                     continue
#                 if relation[i][k] and relation[j][k]:
#                     tmp = len(relation[i]) + len(relation[j]) + len(relation[k]) - 6
#                     print(i,j,k)
#                     if ans == -1 or ans > tmp:
#                         ans = tmp
# print(ans)
# def go(index,i):
#     global ans
#     if index == 3:
#         tmp = 0
#         cnt = 0
#         for chosen in a:
#             rest = list(set(a) - set([chosen]))
#             FLAG = False
#             for fr in rest:
#                 if relation[chosen][fr] == False:
#                     FLAG = True
#                     break
#             if FLAG:
#                 return
#             tmp += len(relation[chosen].keys())-2
#         if ans == -1 or ans > tmp:
#             ans = tmp
#         # print(a)
#         return
#     if i == n:
#         return
#     if index == 2:
#         x,y = a[0],a[1]
#         if relation[x][y] == False:
#             return
#     a[index] = i
#     go(index+1,i+1)
#     a[index] = -1
#     go(index,i+1)
# go(0,0)
# print(ans)