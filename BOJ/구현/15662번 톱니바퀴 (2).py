from copy import deepcopy
T = int(input())
A = []
for _ in range(T):
    A.append([int(i) for i in input()])
K = int(input())

for _ in range(K):
    n,d = map(int,input().split())
    n -= 1

    nx = n
    nd = d
    B = deepcopy(A)
    # 우선 n번째 톱니바퀴 돌려주고,
    # 반시계라면,
    if d == -1:
        B[n] = A[n][1:] + [A[n][0]]
    # 시계방향이라면,
    else:
        B[n] = [A[n][-1]] + A[n][:-1]

    # 톱니바퀴 아래쪽 돌리기.
    while nx >= 1:
        # 극이 같으면 그 이하는 볼 필요가 없음.
        # break로 빠져나옴.
        if A[nx-1][2] == A[nx][6]:
            break
        else:
            nd = -1 if nd == 1 else 1
            if nd == -1:
                B[nx-1] = A[nx-1][1:] + [A[nx-1][0]]
            else:
                B[nx-1] = [A[nx-1][-1]] + A[nx-1][:-1]
            nx -= 1
    # 톱니바퀴 위쪽 돌리기.
    nx = n
    nd = d
    while nx <= T-2:
        # 극이 같으면 그 이상은 볼 필요가 없음.
        # break로 빠져나옴.
        if A[nx][2] == A[nx+1][6]:
            break
        else:
            nd = -1 if nd == 1 else 1
            if nd == -1:
                B[nx+1] = A[nx+1][1:] + [A[nx+1][0]]
            else:
                B[nx+1] = [A[nx+1][-1]] + A[nx+1][:-1]
            nx += 1

    A = deepcopy(B)

answer = 0
for i in range(T):
    if A[i][0] == 1:
        answer += 1
print(answer)