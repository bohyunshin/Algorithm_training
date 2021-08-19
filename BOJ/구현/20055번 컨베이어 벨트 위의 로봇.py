from collections import deque
n,k = map(int, input().split())
A = list(map(int, input().split()))
robot = [0]*(2*n)
step = 0
zero = 0
q = deque()
while zero < k:

    step += 1

    # 컨베이어 벨트, 로봇 이동.
    A = [A[-1]] + A[:-1]
    # 로봇 이동.
    q2 = deque()
    robot = [0] * (2 * n)
    while q:
        x = q.popleft()
        # 로봇 내리기.
        if x+1 == n-1:
            continue
        else:
            robot[x+1] += 1
            q2.append(x+1)

    q3 = deque()
    while q2:
        x = q2.popleft()
        if robot[x+1] == 0 and A[x+1] >= 1:
            if x+1 != n-1:
                q3.append(x+1)
                A[x+1] -= 1
                robot[x] -= 1
                robot[x+1] += 1
            else:
                A[x+1] -= 1
                robot[x] -= 1
        else:
            q3.append(x)

    # 올리는 위치에 로봇 올리기.
    if A[0] >= 1:
        robot[0] += 1
        A[0] -= 1
        q3.append(0)

    q = q3.copy()

    zero = 0
    for i in A:
        if i == 0:
            zero += 1
print(step)