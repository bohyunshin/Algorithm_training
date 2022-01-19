from itertools import combinations
from copy import deepcopy
n,m,d = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
a_copy = deepcopy(a)
def get_monster_loc(x,y):
    candi = []
    for i in range(n):
        for j in range(m):
            dist = abs(i - x) + abs(j - y)
            if a[i][j] == 1 and dist <= d:
                candi.append((dist,i,j))
    candi.sort(key=lambda x: (x[0],x[2]))
    if len(candi) == 0:
        return None
    else:
        x,y = candi[0][1], candi[0][2]
        return (x,y)
def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                return True
    return False
def move():
    for i in range(n-1,-1,-1):
        for j in range(m):
            if a[i][j] == 1:
                if i == n-1:
                    a[i][j] = 0
                else:
                    a[i][j] = 0
                    a[i+1][j] = 1
ans = -1
for c in combinations(range(m),3):
    a = deepcopy(a_copy)
    caught = 0
    shooters = []
    for i in c:
        shooters.append((n,i))
    while check():
        # 먼저 궁수가 활쏘기.
        # 활을 쏠 몬스터 추려내기.
        dead = set()
        for shooter in shooters:
            x,y = shooter
            monster = get_monster_loc(x,y)
            if monster is not None:
                dead.add(monster)
        # print(dead)
        for x,y in dead:
            a[x][y] = 0
            caught += 1
        # 몬스터 이동시키기.
        move()
        # for i in a:
        #     print(i)
    if ans == -1 or ans < caught:
        ans = caught
print(ans)

"""
5 5 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 0 0 0 0
"""