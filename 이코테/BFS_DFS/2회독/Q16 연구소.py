from itertools import combinations
from copy import deepcopy

n,m = map(int, input().split())
map_ = []
for _ in range(n):
    map_.append( list(map(int, input().split())) )
virus = []
blank = []
for i in range(n):
    for j in range(m):
        if map_[i][j] == 0:
            blank.append((i,j))
        elif map_[i][j] == 2:
            virus.append((i,j))

def dfs(map_,x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return map_
    # 위치가 벽이 아니고 이미 방문하지 않았다면 감염
    if map_[x][y] != 1 and map_[x][y] != 2:
        map_[x][y] = 2
    else:
        return map_
    # 상하좌우 살펴봄
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(map_, nx, ny)
    return map_
safety_zone = []
# 가능한 모든 조합에 대해서
for c in combinations(blank,3):
    # 빈 곳에 우선 벽 세우고
    for x,y in c:
        map_[x][y] += 1
    # dfs을 실행한다.
    # virus가 있는 곳이 시작점임
    result = deepcopy(map_)
    for x,y in virus:
        result[x][y] -= 2
        result = dfs(result,x,y)
    # 안전 영역의 크기 확인
    zone = 0
    for i in range(n):
        for j in range(m):
            if result[i][j] == 0:
                zone += 1
    safety_zone.append(zone)
    # 세웠던 벽 허물기
    for x,y in c:
        map_[x][y] -= 1

    # for l in result:
    #     print(l)
    # break
print(max(safety_zone))


