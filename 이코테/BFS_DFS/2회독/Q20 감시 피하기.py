from itertools import combinations
n = int(input())
array = []
for _ in range(n):
    array.append(list(input().split()))
blank = []
teacher = []
student = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 'X':
            blank.append((i,j))
        if array[i][j] == 'T':
            teacher.append((i,j))
        if array[i][j] == 'S':
            student.append((i,j))

def dfs(x,y,direction):
    if x < 0 or y < 0 or x >= n or y >= n:
        return 'YES'
    if array[x][y] == 'O':
        return 'YES'
    if array[x][y] == 'S':
        return 'NO'

    if array[x][y] == 'T' or array[x][y] == 'X':
        # direction:0,1,2,3 [동 서 남 북]
        if direction == 0:
            return dfs(x,y+1,direction)
        elif direction == 1:
            return dfs(x,y-1,direction)
        elif direction == 2:
            return dfs(x+1,y,direction)
        else:
            return dfs(x-1,y,direction)
    # return 'YES'

for c in combinations(blank, 3):
    # 벽 세우기
    for x,y in c:
        array[x][y] = 'O'
    POSSIBLE = 0
    for a,b in teacher:
        if dfs(a,b,direction=0) == 'NO':
            POSSIBLE += 1
            break
        if dfs(a,b,direction=1) == 'NO':
            POSSIBLE += 1
            break
        if dfs(a,b,direction=2) == 'NO':
            POSSIBLE += 1
            break
        if dfs(a,b,direction=3) == 'NO':
            POSSIBLE += 1
            break
    if POSSIBLE == 0:
        print('YES')
        exit(0)
    # 벽 허물기
    for x,y in c:
        array[x][y] = 'X'
print('NO')