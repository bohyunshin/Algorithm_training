from itertools import combinations
from copy import deepcopy
from collections import deque
n,m,g,r = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
possible = []
for i in range(n):
    for j in range(m):
        if A[i][j] == 2:
            possible.append((i,j))
ans = -1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def check(A,B):
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return True
    return False
for c1 in combinations(possible,g):
    rest = [i for i in possible if i not in c1]
    for x,y in c1:
        A[x][y] = 'g'
    for c2 in combinations(rest,r):
        # 하나의 경우 시작 #
        tmp = 0
        for x,y in c2:
            A[x][y] = 'r'
        # green 부터 이동시킴.
        after = deepcopy(A)

        green_list,red_list = list(c1),list(c2)

        while True:
            same_time = []
            next_green_list,next_red_list = [],[]
            for x,y in green_list:
                for k in range(4):
                    nx,ny = x+dx[k],y+dy[k]
                    if 0 <= nx < n and 0 <= ny < m and after[nx][ny] not in [0,'r','g','f']:
                        after[nx][ny] = 'g'
                        same_time.append((nx,ny))
                        next_green_list.append((nx,ny))
            # red 이동시킬 때에는 동시간대에 움직인 green 조건에 주의해야 함.
            for x,y in red_list:
                for k in range(4):
                    nx,ny = x+dx[k],y+dy[k]
                    if 0 <= nx < n and 0 <= ny < m and after[nx][ny] not in [0,'r','f']:
                        if after[nx][ny] == 'g' and (nx,ny) in same_time:
                            after[nx][ny] = 'f'
                            tmp += 1
                            # next_green_list에서 (nx,ny)을 제거해줘야 함.
                            del next_green_list[next_green_list.index((nx,ny))]
                        if after[nx][ny] in [1,2]:
                            after[nx][ny] = 'r'
                            next_red_list.append((nx, ny))
            # if ans == 3:
            #     for i in after:
            #         print(i)
            #     print(tmp)
            # print()

            green_list,red_list = next_green_list[:],next_red_list[:]
            # before, after에 달라진 원소가 하나라도 존재한다면,
            # if check(before,after):
            #     before = deepcopy(after)
            # print(green_list,red_list)
            if len(green_list) >= 1 or len(red_list) >= 1:
                continue
            # 존재하지 않는다면 ㅃ함.
            else:
                break
        ans = max(ans,tmp)
        # if tmp == 5:
        #     print(c1,c2)
        #     for i in after:
        #         print(i)
        # print()
        # 빨간색 배양액 다시 원래대로
        for x,y in c2:
            A[x][y] = 2
    # 초록색 배양액 다시 원래대로
    for x,y in c1:
        A[x][y] = 2
print(ans)

"""
5 5 2 2
0 0 0 0 1
0 0 0 0 2
1 2 2 1 1
2 1 2 0 1
0 1 0 0 1

3 3 1 1
1 1 2
1 1 2
1 1 1
"""