from collections import deque


def rotate_1(a, b, i, n, board):
    x1, y1 = a
    x2, y2 = b
    # 장애물을 체크하는 순서대로 회전한 결과를 반환함
    # 헷갈리지 마셈!
    if i == 0:
        result = ((x2 - 1, y2), (x2, y2))
    elif i == 1:
        result = ((x1 - 1, y1), (x1, y1))
    elif i == 2:
        result = ((x2, y2), (x2 + 1, y2))
    else:
        result = ((x1, y1), (x1 + 1, y1))
    c, d = result
    nx1, ny1 = c
    nx2, ny2 = d
    # 회전한 결과 또한 맵 범위 안에 있어야 하고
    # 거기에 벽이 없어야 한다
    if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
        if board[nx1][ny1] != 1 and board[nx2][ny2] != 1:
            return result
    else:
        return None


def rotate_2(a, b, i, n, board):
    x1, y1 = a
    x2, y2 = b
    # 장애물을 체크하는 순서대로 회전한 결과를 반환함
    # 헷갈리지 마셈!
    if i == 0:
        result = ((x2, y2 - 1), (x2, y2))
    elif i == 1:
        result = ((x2, y2), (x2, y2 + 1))
    elif i == 2:
        result = ((x1, y1 - 1), (x1, y1))
    else:
        result = ((x1, y1), (x1, y1 + 1))
    c, d = result
    nx1, ny1 = c
    nx2, ny2 = d
    # 회전한 결과 또한 맵 범위 안에 있어야 하고
    # 거기에 벽이 없어야 한다
    if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
        if board[nx1][ny1] != 1 and board[nx2][ny2] != 1:
            return result
    else:
        return None


def solution(board):
    n = len(board)
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = {}
    start = ((0, 0), (0, 1))
    # 시작지점까지 가는데 걸리는 시간은 0
    visited[start] = 0
    q = deque()
    q.append(start)
    while q:
        a, b = q.popleft()
        x1, y1 = a
        x2, y2 = b

        # 상하좌우
        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            c = (nx1, ny1)
            d = (nx2, ny2)
            edge = sorted((c, d))
            edge = (edge[0], edge[1])
            if 0 <= nx1 < n and 0 <= ny1 < n and 0 <= nx2 < n and 0 <= ny2 < n:
                if board[nx1][ny1] != 1 and board[nx2][ny2] != 1:
                    FLAG = edge in visited.keys()
                    if FLAG is True and visited[edge] > visited[(a, b)] + 1:
                        visited[edge] = visited[(a, b)] + 1
                        q.append(edge)
                    if FLAG is False:
                        visited[edge] = visited[(a, b)] + 1
                        q.append(edge)

        # 기준점 달리하면서 회전하기
        # 가로로 놓여져 있다면
        check_walls_x = [x1 - 1, x1 - 1, x1 + 1, x1 + 1]
        check_walls_y = [y1, y2, y1, y2]
        if x1 == x2:
            print('yes')
            # 왼쪽을 기준으로 회전하기
            # 반시계 방향
            for i in range(4):
                # 우선 회전할때 대각선 방향에 벽이 있는지 확인
                nx = check_walls_x[i]
                ny = check_walls_y[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] != 1:
                        # 벽이 없다면 회전을 시킴
                        edge = rotate_1(a, b, i, n, board)
                        if edge is not None:
                            FLAG = edge in visited.keys()
                            if FLAG is True and visited[edge] > visited[(a, b)] + 1:
                                visited[edge] = visited[(a, b)] + 1
                                q.append(edge)
                            if FLAG is False:
                                visited[edge] = visited[(a, b)] + 1
                                q.append(edge)
        # 세로로 놓여져 있다면
        check_walls_x = [x1, x1, x2, x2]
        check_walls_y = [y1 - 1, y1 + 1, y2 - 1, y2 + 1]
        if y1 == y2:
            # 왼쪽을 기준으로 회전하기
            # 반시계 방향
            for i in range(4):
                nx = check_walls_x[i]
                ny = check_walls_y[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] != 1:
                        edge = rotate_2(a, b, i, n, board)
                        if edge is not None:
                            FLAG = edge in visited.keys()
                            if FLAG is True and visited[edge] > visited[(a, b)] + 1:
                                visited[edge] = visited[(a, b)] + 1
                                q.append(edge)
                            if FLAG is False:
                                visited[edge] = visited[(a, b)] + 1
                                q.append(edge)
    # (n-1,n-1)에 방문하는 경우의 수는 (n-1,n-2), (n-1,n-1) 이거나 (n-2,n-1), (n-1,n-1)
    try:
        answer1 = visited[((n - 1, n - 2), (n - 1, n - 1))]
    except:
        answer1 = 0
    try:
        answer2 = visited[((n - 2, n - 1), (n - 1, n - 1))]
    except:
        answer2 = 0
    if answer1 == 0:
        return answer2
    elif answer2 == 0:
        return answer1
    else:
        return min(answer1, answer2)