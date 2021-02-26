from itertools import combinations
from copy import deepcopy
n = int(input())
array = []
for _ in range(n):
    array.append(input().split())

teacher = []
student = []
blank = []
# 선생님의 위치
for i in range(n):
    for j in range(n):
        if array[i][j] == 'T':
            teacher.append((i,j))
        elif array[i][j] == 'S':
            student.append((i,j))
        else:
            blank.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for c in combinations(blank, 3):
    whether_no = 0
    array_copy = deepcopy(array)
    # 벽세우기
    for i,j in c:
        array_copy[i][j] = 'O'

    for t in teacher:
        # 한쪽으로만 가는 bfs
        for i in range(4):
            x, y = t
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    break
                if array_copy[nx][ny] == 'O':
                    break
                if array_copy[nx][ny] == 'S':
                    whether_no += 1
                    break
                if array_copy[nx][ny] == 'X':
                    array_copy[nx][ny] = 'X'
                x,y = nx,ny

    if whether_no == 0:
        print('YES')
        exit(0)
print('NO')