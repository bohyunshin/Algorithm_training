from collections import defaultdict
from itertools import combinations
from copy import deepcopy
n,m,h = map(int,input().split())
ladder = [[False]*n for _ in range(h)]
graph = defaultdict(list)
for _ in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    graph[(a,b)].append((a,b+1))
    graph[(a,b+1)].append((a,b))
for i in range(h):
    for j in range(n):
        graph[(i,j)].append((i+1,j))

def ladder_game(x,y,graph,h):
    visited = [[False]*n for _ in range(h+1)]
    while x != h:
        # print(x,y)
        visited[x][y] = True
        tmp = []
        for i,j in graph[(x,y)]:
            if visited[i][j]:
                continue
            tmp.append((i,j))
        tmp.sort(key=lambda x: (x[0]))
        x,y = tmp[0]
    return x,y

def check(graph):
    for i in range(n):
        x,y = ladder_game(0,i,graph,h)
        if i != y:
            return False
    return True

def valid(graph):
    for i in range(h):
        for j in range(n-1):
            if len(graph[(i,j)]) == 3:
                return False
    return True

if check(graph):
    print(0)
    exit()

ans = 1e100
points = []
for i in range(h):
    for j in range(n-1):
        points.append((i,j))
print(len(points))
for cnt in range(1,4):
    for c in combinations(points,cnt):
        # print(c)
        # if c == ((0,2),(2,3),(3,1)):
        #     print(c)
        # graph_cp = deepcopy(graph)
        FLAG = False
        for x,y in c:
            # if c == ((0, 2), (2, 3), (3, 1)):
            #     print(c,graph[(x,y)])
            #     print(x,y)
            # # 이미 사다리가 건설되어 있다면 이 경우는 패스.
            # if len(graph[(x,y)]) == 2:
            #     FLAG = True
            #     break
            # 사다리를 건설.
            graph[(x,y)].append((x,y+1))
            graph[(x,y+1)].append((x,y))
        # if FLAG:
        #     continue

        if valid(graph) and check(graph):
            ans = min(ans,cnt)
            if ans == 2:
                print(c)

        # 사다리 파괴.
        for x,y in c:
            # 사다리를 파괴.
            graph[(x,y)].pop(-1)
            graph[(x,y+1)].pop(-1)

print(ans)

"""
5 5 6
1 1
3 2
2 3
5 1
5 4

5 8 6
1 1
3 2
2 3
5 1
5 4
1 3
3 4
4 2

5 6 6
1 1
1 2
3 2
2 3
5 1
5 4
"""