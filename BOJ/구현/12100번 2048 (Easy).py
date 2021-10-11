from copy import deepcopy
n = int(input())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def move(A,d):
    # 위쪽으로 옮기기.
    A = deepcopy(A)
    added = [[False] * n for _ in range(n)]
    for _ in range(n):
        for x in range(n):
            if d == 1:
                x = n-(x+1)
            for y in range(n):
                if d == 3:
                    y = n-(y+1)
                x_origin,y_origin = x,y
                if A[x][y] == 0:
                    continue
                # print(x,y,A[x][y])
                nx,ny = x+dx[d],y+dy[d]
                while 0 <= nx < n and 0 <= ny < n:
                    # 비어있을 때, 블록 옮기기.
                    if A[nx][ny] == 0:
                        A[nx][ny] = A[x][y]
                        A[x][y] = 0
                        x,y = nx,ny
                        nx,ny = x+dx[d],y+dy[d]
                        continue
                    # 비어있지 않다면
                    else:
                        # 같은 수라면.
                        if A[nx][ny] == A[x][y]:
                            # 아직 합쳐진 적이 없다면 합치기.
                            if added[nx][ny] == False and added[x][y] == False:
                                A[nx][ny] *= 2
                                A[x][y] = 0
                                added[nx][ny] = True
                            # 합쳐진 적이 있다면 바로 합치면 안됨.
                            break
                        # 같은 수가 아니라면, 합치면 안됨.
                        else:
                            break
                x,y = x_origin,y_origin
    # for i in added:
    #     print(i)
    return A
# for d in range(4):
#     print('##################')
#     for i in A:
#         print(i)
#     print()
#     B = move(A,d)
#     for i in B:
#         print(i)
#     print()

ans = -1
def go(index,m,A):
    global ans
    if index == m:
        for i in range(n):
            for j in range(n):
                ans = max(ans,A[i][j])
        return
    for d in range(4):
        # 상호 참조가 문제였음!!!!
        # A = move(A,d)
        go(index+1,m,deepcopy(move(A,d)))
go(0,5,A)
print(ans)

"""
<이동 검사>
4
2 0 0 0
0 2 0 0
0 0 2 0
0 0 0 2

5
2 0 0 0 0
2 0 0 0 0
2 0 0 0 0
2 0 0 0 0
4 0 0 0 0

<반례> (아래쪽으로)
5
2 0 0 0 0
2 0 0 0 0
0 0 0 0 0
4 0 0 0 0
4 0 0 0 0

(오른쪽으로)
5 
2 2 0 4 4
2 0 0 0 0
0 0 0 0 0
4 0 0 0 0
4 0 0 0 0

5 
2 2 0 4 4
0 0 0 0 0
2 0 0 0 0
4 0 0 0 0
4 0 0 0 0

5
4 2 0 4 4
8 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

6
2 2 2 2 2 2
2 2 2 2 2 2
2 2 2 2 2 2
2 2 2 2 2 2
2 2 2 2 2 2
2 2 2 2 2 2
"""