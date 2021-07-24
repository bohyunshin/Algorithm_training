from collections import defaultdict
from copy import deepcopy
import heapq
n,m,k_ = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))
yangboon = [[5]*n for _ in range(n)]
live_t = defaultdict(list)
dead_t = defaultdict(list)
for _ in range(m):
    x,y,z = map(int, input().split())
    # index 맞춰주기
    # O(logN)
    heapq.heappush(live_t[(x-1,y-1)], z)

year = 0
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
while True:
    # 봄
    for k,v in live_t.items():
        x,y = k[0],k[1]
        new_trees = []
        while v:
            tree = heapq.heappop(v)
            if yangboon[x][y] >= tree:
                yangboon[x][y] -= tree
                new_trees.append(tree+1)
            else:
                heapq.heappush(dead_t[(x,y)], tree)
        live_t[k] = new_trees

    # 여름
    for k,v in dead_t.items():
        x,y = k[0],k[1]
        for dead_tree in v:
            yangboon[x][y] += dead_tree // 2
        dead_t[k] = []

    # 가을.
    live_t_copy = deepcopy(live_t)
    for k,v in live_t.items():
        x,y = k[0],k[1]
        for tree in v:
            if tree % 5 == 0:
                for i in range(8):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        heapq.heappush(live_t_copy[(nx,ny)],1)
    live_t = deepcopy(live_t_copy)

    # 겨울
    for i in range(n):
        for j in range(n):
            yangboon[i][j] += A[i][j]

    year += 1

    if year == k_:
        break
final_tree = 0
for k,v in live_t.items():
    final_tree += len(v)
print(final_tree)
