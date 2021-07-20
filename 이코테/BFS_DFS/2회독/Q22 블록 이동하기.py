from collections import deque


def move(robot, i):
    x1, y1 = robot[0]
    x2, y2 = robot[1]
    if i == 0:
        return (x1 - 1, y1), (x2 - 1, y2)
    elif i == 1:
        return (x1 + 1, y1), (x2 + 1, y2)
    elif i == 2:
        return (x1, y1 - 1), (x2, y2 - 1)
    else:
        return (x1, y1 + 1), (x2, y2 + 1)


def rotate_h(robot, i):
    x1, y1 = robot[0]
    x2, y2 = robot[1]
    # returns: 로봇파트1, 로봇파트2, 체크해야할 좌표
    # 왼쪽 기준, 위로 90도
    if i == 0:
        return (x1 - 1, y1), (x1, y1), (x1 - 1, y1 + 1)
    # 왼쪽 기준, 아래로 90도
    elif i == 1:
        return (x1, y1), (x1 + 1, y1), (x1 + 1, y1 + 1)
    # 오른쪽 기준, 위로 90도
    elif i == 2:
        return (x2 - 1, y2), (x2, y2), (x1 - 1, y1 - 1)
    # 오른쪽 기준, 아래로 90도
    else:
        return (x2, y2), (x2 + 1, y2), (x2 + 1, y2 - 1)


def rotate_v(robot, i):
    x1, y1 = robot[0]
    x2, y2 = robot[1]
    # returns: 로봇파트1, 로봇파트2, 체크해야할 좌표
    # 위쪽 기준, 오른쪽으로 90도
    if i == 0:
        return (x1, y1), (x1, y1 + 1), (x1 + 1, y1 + 1)
    # 위쪽 기준, 왼쪽으로 90도
    elif i == 1:
        return (x1, y1 - 1), (x1, y1), (x1 + 1, y1 - 1)
    # 아래쪽 기준, 오른쪽으로 90도
    elif i == 2:
        return (x2, y2), (x2, y2 + 1), (x2 - 1, y2 + 1)
    # 아래쪽 기준, 왼쪽으로 90도
    else:
        return (x2, y2 - 1), (x2, y2), (x2 - 1, y2 - 1)


def solution(board):
    n = len(board)
    start = ((0, 0), (0, 1))
    q = deque()
    q.append(start)

    myhash = {}
    myhash[start] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        robot = q.popleft()
        # 단순 이동
        for i in range(4):
            moved_robot = move(robot, i)
            # 우선 board 안에 있어야 함
            if 0 <= moved_robot[0][0] <= n - 1 and 0 <= moved_robot[0][1] <= n - 1 and \
                    0 <= moved_robot[1][0] <= n - 1 and 0 <= moved_robot[1][1] <= n - 1:
                # 처음 방문이라면
                if moved_robot not in myhash.keys():
                    # 벽이 없을 때만 방문함
                    if board[moved_robot[0][0]][moved_robot[0][1]] == 0 and board[moved_robot[1][0]][
                        moved_robot[1][1]] == 0:
                        myhash[moved_robot] = myhash[robot] + 1
                        q.append(moved_robot)
                # 처음 방문이 아니라면 이전에 방문한 값보다 현재 방문한 시간이 적어야 함
                else:
                    if myhash[moved_robot] > myhash[robot] + 1:
                        myhash[moved_robot] = myhash[robot] + 1
                        q.append(moved_robot)
        direction = 'h' if robot[0][0] == robot[1][0] else 'v'
        # 90도 회전
        for i in range(4):
            if direction == 'h':
                rotated_robot = rotate_h(robot, i)[:2]
                coord_check = rotate_h(robot, i)[2]
            else:
                rotated_robot = rotate_v(robot, i)[:2]
                coord_check = rotate_v(robot, i)[2]
            # 우선 board 안에 있어야 함
            if 0 <= rotated_robot[0][0] <= n - 1 and 0 <= rotated_robot[0][1] <= n - 1 and \
                    0 <= rotated_robot[1][0] <= n - 1 and 0 <= rotated_robot[1][1] <= n - 1:
                # 회전할때 벽이 없어야 함
                if board[coord_check[0]][coord_check[1]] == 0:
                    # 처음 방문이라면
                    if rotated_robot not in myhash.keys():
                        # 벽이 없을 때만 방문함
                        if board[rotated_robot[0][0]][rotated_robot[0][1]] == 0 and board[rotated_robot[1][0]][
                            rotated_robot[1][1]] == 0:
                            myhash[rotated_robot] = myhash[robot] + 1
                            q.append(rotated_robot)
                    # 처음 방문이 아니라면 이전에 방문한 값보다 현재 방문한 시간이 적어야 함
                    else:
                        if myhash[rotated_robot] > myhash[robot] + 1:
                            myhash[rotated_robot] = myhash[robot] + 1
                            q.append(rotated_robot)

    result = []
    for key in myhash.keys():
        if (n - 1, n - 1) in key:
            result.append(myhash[key])
    return min(result)