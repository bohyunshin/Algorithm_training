from collections import defaultdict
from copy import deepcopy
n = 9
seodoku = [list(int(i) for i in input()) for _ in range(n)]
rows = [
    [0,0,0,1,1,1,2,2,2],[3,3,3,4,4,4,5,5,5],[6,6,6,7,7,7,8,8,8]
]
number = [row for row in rows for _ in range(3)]
rects = defaultdict(list)
for i in range(n):
    for j in range(n):
        rects[number[i][j]].append((i,j))
def get_candidate(x,y,seodoku):
    exists = set()
    for k in range(n):
        if seodoku[k][y] != 0:
            exists.add(seodoku[k][y])
        if seodoku[x][k] != 0:
            exists.add(seodoku[x][k])
    for k,l in rects[number[x][y]]:
        if seodoku[k][l] != 0:
            exists.add(seodoku[k][l])
    ans = []
    for i in range(1,10):
        if i not in exists:
            ans.append(i)
    return ans
def check(seodoku):
    for i in range(n):
        for j in range(n):
            if seodoku[i][j] == 0:
                return False
    return True
def go(seodoku):
    print(seodoku)
    if check(seodoku):
        print(answer)
        answer.append(seodoku)
    flag = False
    for i in range(n):
        for j in range(n):
            if seodoku[i][j] == 0:
                cands = get_candidate(i,j,seodoku)
                if len(cands) >= 1:
                    for k in cands:
                        seodoku[i][j] = k
                        go(deepcopy(seodoku))
                    seodoku[i][j] = 0
                else:
                    flag = True
                    break
        if flag:
            break
answer = []
go(seodoku)
print(answer)
"""
000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000
000000000
"""
